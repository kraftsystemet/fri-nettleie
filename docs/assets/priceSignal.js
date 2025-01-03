
// addHours allows us to add a number of hours to a date
// https://stackoverflow.com/a/1050782
Date.prototype.addHours = function(h) {
  this.setTime(this.getTime() + (h*60*60*1000));
  return this;
}

// checking norwegian holidays
var hd = new Holidays.default('NO')

class Unntak {
  constructor(timer, pris, dager, mnd) {
    this.timer = timer;
    this.pris = pris;
    this.dager = dager;
    this.mnd = mnd;
  }

  matcherDager(t) {
    if (this.dager.length === 0) return true;
    if (this.dager.includes("alle")) return true;

    const ukedag = t.getDay();
    const ukedagNavn = ["mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag"][ukedag];

    if (this.dager.includes(ukedagNavn)) return true;

    const erHelligdag = hd.isHoliday(t);
    const erHelg = ukedag === 0 || ukedag === 6;
    const erFridag = erHelg || erHelligdag;
    const erUkedag = ukedag >= 1 && ukedag <= 5;

    if (this.dager.includes("ukedag") && erUkedag) return true;
    if (this.dager.includes("helg") && erHelg) return true;
    if (this.dager.includes("helligdager") && erHelligdag) return true;
    if (this.dager.includes("fridag") && erFridag) return true;
    if (this.dager.includes("virkedag") && !erFridag) return true;

    return false;
  }

  matcherMnd(t) {
    if (this.mnd.length === 0) return true;
    if (this.mnd.includes("alle")) return true;

    const mnd = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"][t.getMonth()];
    return this.mnd.includes(mnd);
  }

  matcherTimer(t) {
    if (this.timer.length === 0) return true;
    return this.timer.includes(t.getHours());
  }

  matcher(t) {
    return this.matcherTimer(t) && this.matcherDager(t) && this.matcherMnd(t);
  }
}

// range string to list
function rangeStringToList(rangeStr) {
  if (rangeStr === '') {
    return [];
  }
  const [start, end] = rangeStr.split('-').map(Number);
  return Array.from({ length: end - start + 1 }, (_, i) => start + i);
}

const ctx = document.getElementById('priceSignal');

var unntakList = []
const unntakInput = energiLedd['unntak'] ?? []
for (const u of unntakInput){
  const ut = new Unntak(rangeStringToList(u['timer'] ?? ''), u['pris'], u['dager'] ?? [], u['mnd'] ?? [])
  unntakList.push(ut);
};
console.log(unntakList);

const elFee = 9.79 // 2025

const localeStartOfDat = moment().startOf('day')
const timeSeriesLabels = [];
const timeSeriesPrice = [];
const timeSeriesPriceMVA = [];
const timeSeriesEnova = [];
const timeSeriesEnovaMVA = [];
const timeSeriesForbruk = [];
const timeSeriesForbrukMVA = [];
let max = 0;

for (let i = 0; i < 24*7; i++) {
  const h = new Date(localeStartOfDat);
  h.addHours(i);

  timeSeriesLabels.push(h);

  pris = energiLedd.grunnpris;
  for (const u of unntakList) {
    if (u.matcher(h)) {
      pris = u.pris;
      break;
    }
  }

  timeSeriesPrice.push(pris);
  timeSeriesPriceMVA.push(0.25*pris);
  timeSeriesEnova.push(1);
  timeSeriesEnovaMVA.push(0.25);
  timeSeriesForbruk.push(elFee);
  timeSeriesForbrukMVA.push(elFee*0.25);
  if (pris > max) {
    max = pris + 44;
  }
}

new Chart(ctx, {
  type: 'line',

  data: {
    labels: timeSeriesLabels,
    datasets: [{
      label: 'Forbruksavgift (øre)',
      data: timeSeriesForbruk
    },{
      label: 'MVA Forbruksavgift (øre)',
      data: timeSeriesForbrukMVA
    },{
      label: 'Enova-avgift (øre)',
      data: timeSeriesEnova
    },{
      label: 'MVA Enova-avgift (øre)',
      data: timeSeriesEnovaMVA
    },{
      label: 'Energiledd (øre)',
      data: timeSeriesPrice
    },{
      label: 'MVA Energiledd (øre)',
      data: timeSeriesPriceMVA
    }

  ]
},
options: {
  pointStyle: false,
  stepped: true,
  interaction: {
    mode: 'index',
    intersect: false
  },
  fill: true,
  scales: {
    x: {
      type: 'timeseries',
      time: {
        displayFormats: {
          hour: 'YYYY-MM-DD HH:mm',
          day: 'YYYY-MM-DD HH:mm'
          // or any desired format
        }
      }
    },
    y: {
      max: max+2.0,
      beginAtZero: true,
      stacked: true,
    }
  }
}
});
