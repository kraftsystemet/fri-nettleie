"""Lag blinde, nummererte arbeidsmapper til en manuell OpenCode-kjøring (macOS).

Bruk repoets venv: klargjor_gpt.py <ny mappe utenfor repoet> [saksnavn ...]
"""

import json
import os
import shlex
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path

import yaml

EVAL = Path(__file__).resolve().parent
REPO = EVAL.parents[1]
SKILL = Path(".agents/skills/samle-tariff")


def klargjor(rot, nummer, sak):
    ramme = rot / f"case-{nummer:02}"
    arbeid = ramme / "arbeid"
    arbeid.mkdir(parents=True)
    subprocess.run(["git", "init", "-q", arbeid], check=True)
    for fil in (
        "tariff.cue", "tariff-eksempel.yml", ".yamlfmt.yml", "scripts/prissignal.py",
        "scripts/check_increasing_levels.py", "scripts/check_overlap_and_gap.py", SKILL / "SKILL.md",
    ):
        (arbeid / fil).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(REPO / fil, arbeid / fil)
    shutil.copytree(REPO / SKILL / "references", arbeid / SKILL / "references")
    for fil in sorted((REPO / SKILL / "scripts").iterdir()):
        if fil.suffix in {".py", ".sh"}:
            (arbeid / SKILL / "scripts").mkdir(exist_ok=True)
            shutil.copy(fil, arbeid / SKILL / "scripts")
    meta = yaml.safe_load((sak / "case.yml").read_text())
    oppgave = {k: meta[k] for k in ("selskap", "oppgave", "fra", "sone")}
    (arbeid / "oppgave.yml").write_text(yaml.safe_dump(oppgave, allow_unicode=True, sort_keys=False))
    shutil.copy(sak / "input.md", arbeid)
    (arbeid / "tariffer").mkdir()
    shutil.copy(sak / "eksisterende.yml", arbeid / "tariffer" / f"{meta['selskap']}.yml")

    konfigurer_skall(arbeid, ramme, rot)
    return arbeid


def konfigurer_skall(arbeid, ramme, rot):
    # Kun modellklienten trenger nett. Skallet får ikke lese fasit eller de andre sakene.
    tmp = arbeid / ".tmp"
    tmp.mkdir()
    lib = rot / "pythonlib"
    q = json.dumps
    profil = f'''(version 1)
(allow default)
(deny network*)
(deny file-read* file-write* (subpath "/Users") (subpath "/Volumes") (subpath "/private/var/folders") (subpath "/private/tmp") (subpath {q(str(REPO))}) (subpath {q(str(rot))}))
(allow file-read* (subpath {q(str(lib))}))
(allow file-read* file-write* (subpath {q(str(arbeid))}))
'''
    shell = ramme / "zsh"
    sti = os.pathsep.join([str(Path(sys._base_executable).parent), str(Path(shutil.which("cue")).parent),
                           "/opt/homebrew/bin", "/usr/local/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin"])
    cmd = ["/usr/bin/env", "-i", f"HOME={tmp}", f"TMPDIR={tmp}", f"PATH={sti}", "LANG=en_US.UTF-8",
           f"PYTHON={sys._base_executable}", f"PYTHONPATH={lib}", "PYTHONDONTWRITEBYTECODE=1",
           "/usr/bin/sandbox-exec", "-p", profil, "/bin/zsh", "-f"]
    shell.write_text("#!/bin/sh\nexec " + shlex.join(cmd) + ' "$@"\n')
    shell.chmod(0o755)
    # Konfigurasjonen ligger utenfor agentens git-rot.
    regler = [{"action": "*", "resource": "*", "effect": "deny"}]
    for action in ("read", "glob", "grep", "edit", "shell"):
        regler.append({"action": action, "resource": "*", "effect": "allow"})
    config = {"shell": str(shell), "snapshots": False, "agents": {"build": {"permissions": regler}}}
    (ramme / "opencode.json").write_text(json.dumps(config, indent=2))


def main():
    if len(sys.argv) < 2 or sys.platform != "darwin" or not shutil.which("cue"):
        sys.exit(__doc__)
    rot = Path(sys.argv[1]).resolve()
    if rot.is_relative_to(REPO) or REPO.is_relative_to(rot):
        sys.exit("Arbeidsmappene må ligge utenfor repoet.")
    rot.mkdir(mode=0o700)
    lib = rot / "pythonlib"
    lib.mkdir()
    site = Path(sysconfig.get_path("purelib"))
    pakker = [site / navn for navn in ("yaml", "dateutil", "holidays", "six.py")]
    for src in pakker + list(site.glob("holidays-*.dist-info")):
        if src.is_dir():
            shutil.copytree(src, lib / src.name, ignore=shutil.ignore_patterns("__pycache__"))
        else:
            shutil.copy(src, lib)
    saker = {sak.name: sak for sak in (EVAL / "caser").iterdir() if sak.is_dir()}
    for i, navn in enumerate(sorted(sys.argv[2:] or saker), 1):
        print(f"{navn}\t{klargjor(rot, i, saker[navn])}")


if __name__ == "__main__":
    main()
