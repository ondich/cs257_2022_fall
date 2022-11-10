/*
 * map-sample-world.js
 * Jeff Ondich
 * 11 November 2020
 *
 * Simple sample using the Datamaps library to show how to incorporate
 * a US map in your project.
 *
 * Datamaps is Copyright (c) 2012 Mark DiMarco
 * https://github.com/markmarkoh/datamaps
 */

window.onload = initialize;

// This is example data that gets used in the click-handler below. Also, the fillColor
// specifies the color those countries should be. There's also a default color specified
// in the Datamap initializer below.
var extraCountryInfo = {
    GBR: {population: 66700000, jeffhasbeenthere: true, fillColor: '#2222aa'},
    USA: {population: 328000000, jeffhasbeenthere: true, fillColor: '#2222aa'},
    IND: {population: 1353000000, jeffhasbeenthere: false, fillColor: '#aa2222'},
    JPN: {population: 125500000, jeffhasbeenthere: true, fillColor: '#aa2222'},
    PRT: {population: 10300000, jeffhasbeenthere: true, fillColor: '#aa2222'},
};

function initialize() {
    initializeMap();
}

function initializeMap() {
    var map = new Datamap({ element: document.getElementById('map-container'), // where in the HTML to put the map
                            scope: 'world', // which map?
                            projection: 'equirectangular', // what map projection? 'mercator' is also an option
                            done: onMapDone, // once the map is loaded, call this function
                            data: extraCountryInfo, // here's some data that will be used by the popup template
                            fills: { defaultFill: '#999999' },
                            geographyConfig: {
                                //popupOnHover: false, // You can disable the hover popup
                                //highlightOnHover: false, // You can disable the color change on hover
                                popupTemplate: hoverPopupTemplate, // call this to obtain the HTML for the hover popup
                                borderColor: '#eeeeee', // state/country border color
                                highlightFillColor: '#99dd99', // color when you hover on a state/country
                                highlightBorderColor: '#000000', // border color when you hover on a state/country
                            }
                          });
}

// This gets called once the map is drawn, so you can set various attributes like
// state/country click-handlers, etc.
function onMapDone(dataMap) {
    dataMap.svg.selectAll('.datamaps-subunit').on('click', onCountryClick);
}

function hoverPopupTemplate(geography, data) {
    var population = 0;
    if (data && 'population' in data) {
        population = data.population;
    }

    var jeffHasLivedThere = 'Maybe. I dunno.';
    if (data && 'jeffhasbeenthere' in data) {
        if (data.jeffhasbeenthere) {
            jeffHasLivedThere = 'Yes';
        } else {
            jeffHasLivedThere = 'No';
        }
    }

    var template = '<div class="hoverpopup"><strong>' + geography.properties.name + '</strong><br>\n'
                    + '<strong>Population:</strong> ' + population + '<br>\n'
                    + '<strong>Has Jeff been there?</strong> ' + jeffHasLivedThere + '<br>\n'
                    + '</div>';

    return template;
}

function onCountryClick(geography) {
    // geography.properties.name will be the state/country name (e.g. 'Minnesota')
    // geography.id will be the state/country name (e.g. 'MN')
    var countrySummaryElement = document.getElementById('country-summary');
    if (countrySummaryElement) {
        var summary = '<p><strong>Country:</strong> ' + geography.properties.name + '</p>\n'
                    + '<p><strong>Abbreviation:</strong> ' + geography.id + '</p>\n';
        if (geography.id in extraCountryInfo) {
            var info = extraCountryInfo[geography.id];
            summary += '<p><strong>Population:</strong> ' + info.population + '</p>\n';
        }

        countrySummaryElement.innerHTML = summary;
    }
}

