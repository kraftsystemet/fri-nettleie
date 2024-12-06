
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

const tariff = {
    "grunnpris" : 3.0,
    "unntak" : [{
        "timer" : "6-21",
        "pris" : 4
    }]
}


const unntak = tariff.unntak[0];
hours = rangeStringToList(unntak.timer);

const localeStartOfDat = moment().startOf('day')
const timeSeriesData = [];
const timeSeriesLabels = [];
let max = 0;

for (let i = 0; i < 24*7; i++) {
const h = new Date(localeStartOfDat);
h.addHours(i);

timeSeriesLabels.push(h);
if (hours.includes(h.getHours())) {
    pris = unntak.pris;
} else {
    pris = tariff.grunnpris;
}

timeSeriesData.push(pris);
if (pris > max) {
    max = pris;
}
}

new Chart(ctx, {
    type: 'line',
    data: {
        labels: timeSeriesLabels,
        datasets: [{
        label: 'Energiledd (øre)',
        data: timeSeriesData,
        borderWidth: 1
        }]
    },
    options: {
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
            stacked: true
        }
        }
    }
});
