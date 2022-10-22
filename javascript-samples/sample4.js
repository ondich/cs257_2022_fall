/*
    sample4.js
    Jeff Ondich, 5 May 2016
    For CS257 Software Design, Carleton College
 */
function initialize() {
    alert('Hi from initialize! The number is: ' + someNumber);

    var div = document.getElementById('somediv');
    if (div === null) {
        alert('somediv is not available yet in initialize');
    } else {
        alert('in initialize, somediv says: ' + div.innerHTML);
    }
}

window.onload = initialize;

