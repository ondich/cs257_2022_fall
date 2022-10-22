/*
    sample1.js
    Jeff Ondich, 5 May 2016
    For CS257 Software Design, Carleton College
 */
function onButtonPress() {
    alert('Hi from onButtonPress!');
}

function initialize() {
    var button = document.getElementById('prizebutton');
    button.onclick = onButtonPress;
}

// This causes initialization to wait until after the HTML page and its
// resources are all ready to go, which is often what you want. This
// "window.onload" approach is a bit old-fashioned. See
// https://www.dyn-web.com/tutorials/init.php for an interesting and
// brief discussion of problems with this old-fashioned approach that
// can become relevant with more complex web pages than the ones
// we are writing.
window.onload = initialize;

