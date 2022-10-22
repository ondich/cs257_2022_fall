/*
    sample.js
    Jeff Ondich, 5 May 2016

    A small demo of some simple Javascript techniques.
    For CS257 Software Design, Carleton College
 */
function onKeyPress(keyEvent) {
    // Uncomment to help learn about the difference between charCode and keyCode.
    //alert('charCode: ' + keyEvent.charCode + ', keyCode: ' + keyEvent.keyCode);

    var colorBoxElement = document.getElementById('colorbox');

    switch (keyEvent.keyCode) {
    case 98: // b -- I haven't found a standard way to do this more readably. Let me know if you do.
        colorBoxElement.style.backgroundColor = '#2222bb';
        colorBoxElement.innerHTML = 'This box is blue';
        break;

    case 114: // r
        colorBoxElement.style.backgroundColor = '#bb2222';
        colorBoxElement.innerHTML = 'This box is red';
        break;

    case 103: // g
        colorBoxElement.style.backgroundColor = '#22bb22';
        colorBoxElement.innerHTML = 'This box is green';
        break;
    }
}

function initialize() {
    document.onkeypress = onKeyPress;
}

window.onload = initialize;

