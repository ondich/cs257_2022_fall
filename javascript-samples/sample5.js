/*
    sample5.js
    Jeff Ondich
    17 November 2020

    This sample illustrates a technique for creating a sequence
    of menu/lists, where the selection of the first list determines the
    contents of the second list, etc.

    This code is intended to be simple-minded, to illustrate the basic
    technique (which is, essentially, CSS + click-handlers). The result
    is that there's code duplication here that could/should be generalized to
    handle a sequence of N dependent lists without having to have
    N nearly-identical functions. That generalization is left as an
    exercise for you, dear reader.
 */

window.onload = initialize;

function initialize() {
    loadFirstList();
}

function loadFirstList() {
    var firstList = document.getElementById('first-list');
    if (firstList) {
        // Load some <li> elements into the list. You could also
        // hard-code these into the HTML or obtain them from an API.
        var listBody = '<li>Ant</li>\n<li>Bat</li>\n<li>Cat</li>\n<li>Dog</li>\n<li>Emu</li>\n';
        firstList.innerHTML = listBody;
        
        // Give the <li> elements a click handler.
        for (var k=0; k < firstList.children.length; k++) {
            var child = firstList.children[k];
            child.onclick = function(e) {
                updateSelection(firstList, this); // See updateSelection and the CSS for .selected
                loadSecondListFor(this.innerHTML);
                clearList(document.getElementById('third-list'));
                updateResults();
            }
        }
    }
}

function loadSecondListFor(firstListSelection) {
    var secondList = document.getElementById('second-list');
    if (secondList) {
        // Load some <li> elements into the list. You could
        // obtain these from an API.
        var listBody = '';
        if (firstListSelection == 'Ant') {
            listBody = '<li>Hill</li>\n<li>Strength</li>\n<li>Picnic!</li>\n';
        } else if (firstListSelection == 'Bat') {
            listBody = '<li>Swoop</li>\n<li>Sonar</li>\n<li>Top-down</li>\n';
        } else if (firstListSelection == 'Cat') {
            listBody = '<li>Sleep</li>\n<li>Sleep more</li>\n<li>Purr-scratch</li>\n';
        } else if (firstListSelection == 'Dog') {
            listBody = '<li>Sleep</li>\n<li>Roll around on deer carcass</li>\n<li>Treat?</li>\n';
        } else if (firstListSelection == 'Emu') {
            listBody = '<li>Run</li>\n<li>Do not mess with the emu</li>\n';
        }
        secondList.innerHTML = listBody;

        // Give the <li> elements a click handler.
        for (var k=0; k < secondList.children.length; k++) {
            var child = secondList.children[k];
            child.onclick = function(e) {
                updateSelection(secondList, this);
                loadThirdListFor(this.innerText);
                updateResults();
            }
        }
    }
}

function loadThirdListFor(secondListSelection) {
    var thirdList = document.getElementById('third-list');
    if (thirdList) {
        // Load some <li> elements into the list. You could
        // obtain these from an API.
        var listBody = '';
        for (var k=0; k < 5; k++) {
            listBody += '<li>' + secondListSelection + ' #' + k + '</li>\n';
        }
        thirdList.innerHTML = listBody;

        // Give the <li> elements a click handler.
        for (var k=0; k < thirdList.children.length; k++) {
            var child = thirdList.children[k];
            child.onclick = function(e) {
                updateSelection(thirdList, this);
                updateResults();
            }
        }
    }
}

function updateResults() {
    var resultsElement = document.getElementById('results');
    if (resultsElement) {
        var firstSelection = '';
        var firstListElement = document.getElementById('first-list');
        if (firstListElement) {
            var selectedListItem = getSelectedListItem(firstListElement);
            if (selectedListItem) {
                firstSelection = selectedListItem.innerHTML;
            }
        }

        var secondSelection = '';
        var secondListElement = document.getElementById('second-list');
        if (secondListElement) {
            var selectedListItem = getSelectedListItem(secondListElement);
            if (selectedListItem) {
                secondSelection = selectedListItem.innerHTML;
            }
        }

        var thirdSelection = '';
        var thirdListElement = document.getElementById('third-list');
        if (thirdListElement) {
            var selectedListItem = getSelectedListItem(thirdListElement);
            if (selectedListItem) {
                thirdSelection = selectedListItem.innerHTML;
            }
        }

        resultsElement.innerHTML = 'First selection: ' + firstSelection + '<br>\n'
                                 + 'Second selection: ' + secondSelection + '<br>\n'
                                 + 'Third selection: ' + thirdSelection + '<br>\n';
    }
}

//////////// Utility functions ////////////

function clearList(listElement) {
    listElement.innerHTML = '';
}

function updateSelection(listElement, listItemToSelect) {
    // Assuming listElement is a <ul> or <ol>, this function will mark
    // listItemToSelect with class="selected", and ensure that no other
    // <li> elements have class="selected".
    for (var k=0; k < listElement.children.length; k++) {
        listElement.children[k].classList.remove('selected');
    }
    listItemToSelect.classList.add('selected');
}

function getSelectedListItem(listElement) {
    var selection = null;
    for (var k=0; k < listElement.children.length; k++) {
        if (listElement.children[k].classList.contains('selected')) {
            selection = listElement.children[k];
            break;
        }
    }
    return selection;
}

