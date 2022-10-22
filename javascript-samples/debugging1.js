/*
 * debugging1.js
 * Jeff Ondich, 9 November 2021
 */

window.onload = initialize;

function initialize() {
    let element = document.getElementById('submit_button');
    element.onclick = onSubmitButtonClicked;
}

function onSubmitButtonClicked() {
    let languageSelector = document.getElementById('language_selector');
    let language = languageSelector.value;
    let numberElement = document.getElementById('number');
    let number = numberElement.value;
    let url = 'http://api.ultralingua.com/api/2.0/numbers/'
                + language + '/' + number
                + '?key=cs257';

    fetch(url, {method: 'get'})

    .then((response) => response.json()

    .then(function(translation) {
        let translationElement = document.getElementById('translation');
        translationElement.innerHTML = 'Translation: ' + translation;
    })

    .catch(function(error) {
        console.log(error);
    });
}

