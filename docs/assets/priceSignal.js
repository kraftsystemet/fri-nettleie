
// https://stackoverflow.com/a/1050782
Date.prototype.addHours = function(h) {
    this.setTime(this.getTime() + (h*60*60*1000));
    return this;
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

const unntak = energiLedd.unntak ? energiLedd.unntak[0] : null;

let hours = [];
if (unntak) {
    hours = rangeStringToList(unntak.timer);
}

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
    if (hours.includes(h.getHours())) {
        pris = unntak.pris;
    } else {
        pris = energiLedd.grunnpris;
    }

    timeSeriesPrice.push(pris);
    timeSeriesPriceMVA.push(0.25*pris);
    timeSeriesEnova.push(1);
    timeSeriesEnovaMVA.push(0.25);
    timeSeriesForbruk.push(16.44);
    timeSeriesForbrukMVA.push(16.44*0.25);
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
