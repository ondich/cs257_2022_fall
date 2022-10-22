/*
    sample.js
    Jeff Ondich, 5 May 2016

    A small demo of some simple Javascript techniques.
    For CS257 Software Design, Carleton College
 */
function onChangeWordButton() {
    var colorBoxElement = document.getElementById('colorbox');
    var magicWordElement = document.getElementById('magicword');
    colorBoxElement.innerHTML = 'The magic word is "' + magicWordElement.value + '"';
}

function initialize() {
    var button = document.getElementById('changewordbutton');
    button.onclick = onChangeWordButton;
}

window.onload = initialize;

