/*
 * simple-charts.js
 * Jeff Ondich, 12 November 2020
 *
 * Adapted from the Chartist library samples.
 *   https://gionkunz.github.io/chartist-js/examples.html
 */

window.onload = initialize;

function initialize() {
    createLineChart();
    createBarChart();
    createPieChart();
}

function createLineChart() {
    // Data & x-axis labels
    var data = {
        labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
        series: [
            { data: [17, -2, 4, 9, 11, 7, 2] },
            { data: [1, 2, 3, 5, 8, 13, 21] }
        ]
    };

    // There are many options you can add to a chart. For this
    // sample we're not using any. The documentation at Chartist's website
    // says "check the samples for a complete list", but honestly, they do
    // a mediocre job of pointing you to them.
    // https://gionkunz.github.io/chartist-js/
    var options = {}

    /* Initialize the chart with the above settings */
    new Chartist.Line('#sample-line-chart', data, options);
}

function createBarChart() {
    var data = {
        labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
        series: [
            { data: [17, -2, 4, 9, 11, 7, 2] },
            { data: [1, 2, 3, 5, 8, 13, 21] }
        ]
    };

    var options = {}

    new Chartist.Bar('#sample-bar-chart', data, options);
}

function createPieChart() {
    var data = {
        labels: ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'],
        series: [17, 6, 4, 9, 11, 7, 2]
    };

    var options = {}

    new Chartist.Pie('#sample-pie-chart', data, options);
}
