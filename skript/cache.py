# Cache is used to do local iterations on scripts w/o putting load on the external APIs.
# Clear cache with `rm -rf ~/.cache/raftsystemet-fri-nettleie`

import requests_cache
requests_cache.install_cache(
    'kraftsystemet-fri-nettleie',
    backend='filesystem',
    use_cache_dir=True
)
