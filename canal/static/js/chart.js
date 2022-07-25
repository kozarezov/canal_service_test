$(document).ready(function () {

    "use strict";
    function loadJson(selector) {
        return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
      }
    
    var jsonData1 = loadJson('#jsonData1');
    var jsonData2 = loadJson('#jsonData2');

    var options = {
        chart: {
            height: 730,
            type: 'line',
            zoom: {
                enabled: false
            }
        },
        series: [{
            name: "Сумма",
            data: jsonData1
        }],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'straight'
        },
        title: {
            text: '',
            align: 'left'
        },
        grid: {
            row: {
                colors: ['#f3f3f3', 'transparent'],
                opacity: 0.5
            },
            borderColor: 'rgba(94, 96, 110, .5)',
            strokeDashArray: 4
        },
        xaxis: {
            categories: jsonData2,
            labels: {
                style: {
                    colors: 'rgba(94, 96, 110, .5)'
                }
            }
        }
    }

    var chart = new ApexCharts(
        document.querySelector("#apex1"),
        options
    );

    chart.render();
});