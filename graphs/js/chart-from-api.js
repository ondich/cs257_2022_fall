/*
 * chart-from-api.js
 * Jeff Ondich, 12 November 2020
 *
 * Script for a sample showing how to take data from an API
 * and build a bar chart with tooltips.
 *
 * Uses the Chartist library: https://gionkunz.github.io/chartist-js/
 * Copyright © 2019 Gion Kunz
 * Free to use under either the WTFPL license or the MIT license.
 *
 * Data from the COVID Tracking Project: https://covidtracking.com/data/api
 * The COVID Tracking Project at The Atlantic’s data and website content is
 * published under a Creative Commons CC BY 4.0 license, which requires users
 * to attribute the source and license type (CC BY 4.0) when sharing our data
 * or website content.
 */

window.onload = initialize;

function initialize() {
    populateStateSelector();
}

function populateStateSelector() {
    // Populate the the drop-down list with the list of states from the API.
    var url = 'https://api.covidtracking.com/v1/states/info.json';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(states) {
        var stateSelector = document.getElementById('state-select');
        if (stateSelector) {
            // Populate it with states from the API
            var stateSelectorBody = '<option value="US">United States</option>\n';
            for (var k=0; k < states.length; k++) {
                var state = states[k];
                stateSelectorBody += '<option value="' + state['state'] + '">' + state['name'] + '</option>\n';
            }
            stateSelector.innerHTML = stateSelectorBody;

            // Set the new-selection handler
            stateSelector.onchange = onStateSelectorChanged;

            // Start us out looking at Minnesota.
            stateSelector.value = 'MN';
            createStateChart('Minnesota', 'MN');
        }

    })
    .catch(function(error) {
        console.log(error);
    });
}

function onStateSelectorChanged() {
    var stateSelector = document.getElementById('state-select');
    if (stateSelector) {
        var stateName = stateSelector.options[stateSelector.selectedIndex].text
        var stateAbbreviation = stateSelector.value;
        createStateChart(stateName, stateAbbreviation);
    }
}

function createStateChart(stateName, stateAbbreviation) {
    // Set the title
    var stateTitle = document.getElementById('state-new-cases-title');
    if (stateTitle) {
        stateTitle.innerHTML = 'New cases for ' + stateName;
    }

    // Create the chart
    var url = '';
    if (stateAbbreviation.toLowerCase() == 'us') {
        url = 'https://api.covidtracking.com/v1/us/daily.json';
    } else {
        url = 'https://api.covidtracking.com/v1/states/' + stateAbbreviation.toLowerCase() + '/daily.json';
    }

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(days) {
        // Use the API response (days), which is a list of dictionaries like this:
        //
        //   {date: '20200315', positiveIncrease: 2345, ... }
        //
        // to assemble the data my bar-chart will need. That data looks like a
        // list of dictionaries (newCasesData). Each dictionary in the list will look
        // like this:
        //
        //   {meta:'2020-03-15', value: 2345}
        //
        // Here, meta is the date, which Chartist will use in a popup window that appears
        // if you hover over a bar in the bar chart, and value is the number of new COVID
        // cases for that date, which will, of course, determine the height of the bar
        // in the bar chart.
        //
        // In this same loop, we're also creating a list (labels) of labels to be used
        // along the x-axis of the bar chart.

        // This code assumes results are sorted in descending order by date, which is
        // indeed how the API returns the data as of this writing.
        var labels = [];
        var newCasesData = [];
        for (var k = 0; k < days.length; k++) {
            // Assumes YYYYMMDD int
            var date = '' + days[days.length - k -1].date;
            date = date.slice(0, 4) + '-' + date.slice(4, 6) + '-' + date.slice(-2);
            labels.push(date);
            newCasesData.push({meta: date, value: days[days.length - k - 1].positiveIncrease});
        }

        // We set some options for our bar chart. seriesBarDistance is the width of the
        // bars. axisX allows us to specify a bunch of options related to the x-axis.
        // The one we're picking is labelInterpolationFnc, which allows us to control
        // which bars have x-axis labels. Here, we're saying "write the date of the bar
        // on the x-axis every 7 days". Otherwise, the axis just gets too crowded.
        var options = { seriesBarDistance: 25,
                        axisX: { labelInterpolationFnc: function(value, index) {
                                    return index % 7 === 0 ? value : null;
                                }
                        },
                      };

        // Here's the form in which Chartist expects its data to be specified. Not that
        // series is a list, since you might want to have two or more differently colored
        // sets of bars, or line graphs, etc. on the same chart.
        var data = { labels: labels, series: [newCasesData] };

        // Finally, we create the bar chart, and attach it to the desired <div> in our HTML.
        var chart = new Chartist.Bar('#state-new-cases-chart', data, options);

        // HERE COMES THE MESS THAT IS TOOLTIPS! FEEL FREE TO IGNORE!
        // Tooltips are those little sometimes-informative popups that give you a little
        // information about something your mouse is hovering over. We want them on this
        // bar chart so we can get the exact number of new cases on a particular day, not
        // just an estimate (which is what you'll get from just looking at the bar's height).
        //
        // I got a lot of help from here.
        // https://stackoverflow.com/questions/34562140/how-to-show-label-when-mouse-over-bar
        //
        // Note that all of this code uses jQuery notation. I wrote everything above here
        // in vanilla Javascript, but I don't feel like rewriting the following more complicated code.

        chart.on('created', function(bar) {
            var toolTipSelector = '#state-new-cases-tooltip';
            $('.chart-container .ct-bar').on('mouseenter', function(e) {  // Set a "hover handler" for every bar in the chart
                var value = $(this).attr('ct:value'); // value and meta come ultimately from the newCasesData above
                var label = $(this).attr('ct:meta');
                var caption = '<b>Date:</b> ' + label + '<br><b>New cases (' + stateName + '):</b> ' + value;
                $(toolTipSelector).html(caption);
                $(toolTipSelector).parent().css({position: 'relative'});
                // bring to front, https://stackoverflow.com/questions/3233219/is-there-a-way-in-jquery-to-bring-a-div-to-front
                $(toolTipSelector).parent().append($(toolTipSelector));

                var x = e.clientX;
                var y = e.clientY;
                $(toolTipSelector).css({top: y, left: x, position:'fixed', display: 'block'});
            });

            $('.state-new-cases-chart .ct-bar').on('mouseout', function() {
                $(toolTipSelector).css({display: 'none'});
            });
        });
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

/*
For reference, this is what the "day" dictionaries returned by the COVID API look like.

{
    "date":20200607,
    "state":"MN",
    "positive":27886,
    "negative":316317,
    "pending":null,
    "hospitalizedCurrently":450,
    "hospitalizedCumulative":3367,
    "inIcuCurrently":199,
    "inIcuCumulative":1044,
    "onVentilatorCurrently":null,
    "onVentilatorCumulative":null,
    "recovered":22992,
    "dataQualityGrade":"A",
    "lastUpdateEt":"6/6/2020 17:00",
    "dateModified":"2020-06-06T17:00:00Z",
    "checkTimeEt":"06/06 13:00",
    "death":1197,
    "hospitalized":3367,
    "dateChecked":"2020-06-06T17:00:00Z",
    "fips":"27",
    "positiveIncrease":385,
    "negativeIncrease":10334,
    "total":344203,
    "totalTestResults":344203,
    "totalTestResultsIncrease":10719,
    "posNeg":344203,
    "deathIncrease":16,
    "hospitalizedIncrease":31,
    "hash":"5f4eb67ca77d3ebc7d7b111b20fbd5476b182a45",
    "commercialScore":0,
    "negativeRegularScore":0,
    "negativeScore":0,
    "positiveScore":0,
    "score":0,
    "grade":""
}
*/

