/*
 * sql-injection.js
 * Jeff Ondich, 13 November 2020
 *
 * This is a part of an example of how SQL Injection can occur.
 */

window.onload = initialize;

function initialize() {
    var element = document.getElementById('search_button');
    if (element) {
        element.onclick = onSearchButtonClicked;
    }
}

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    return '/api';
}

function onSearchButtonClicked() {
    var url = getAPIBaseURL() + '/authors/dangerous';
    
    // This is sending user-generated data to the API. Let the ominous music begin.
    var element = document.getElementById('search_text');
    if (element) {
        url += '/' + element.value;
    }

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(authorsList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < authorsList.length; k++) {
            tableBody += '<tr>';
            tableBody += '<td>' + authorsList[k]['given_name'] + ' ' + authorsList[k]['surname'] + '</td>\n';
            tableBody += '</tr>';
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })

    // Log the error if anything went wrong during the fetch.
    .catch(function(error) {
        console.log(error);
    });
}

