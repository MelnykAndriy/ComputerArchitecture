/**
 * Created by mandriy on 3/3/15.
 */

function getUkrainianLetters() {
    var specialUkrainianLetters = ['\u0491', '\u0454', '\u0456', '\u0457' ];
    var specialRussianLetters = ['\u044A', '\u044B', '\u044D', '\u0451'];
    var onlyUkrainianLetters = [];
    for (var i = 1072; i < 1104; i++) {
        if (specialRussianLetters.join().search(String.fromCharCode(i)) === -1 ) {
            onlyUkrainianLetters.push(String.fromCharCode(i))
        }
    }
    return onlyUkrainianLetters.concat(specialUkrainianLetters)
}

function getNames(text) {
    var l = "";
    var ukrLettersList = getUkrainianLetters();
    for (var i in ukrLettersList) {
        l += ukrLettersList[i]
    }
    var searchRegEx = RegExp("[" + l.toUpperCase() + "][" + l.toLowerCase() + "’]*[" + l.toLowerCase()
                             + "]\\s[" + l.toUpperCase() + "]\\.\\s?[" + l.toUpperCase() + "]\\.", "g");
    return text.match(searchRegEx)
}

function createRequest() {
    var xhttp;
    if (typeof XMLHttpRequest !== 'undefined'){
       xhttp=new XMLHttpRequest()
    } else {
       xhttp=new ActiveXObject("Microsoft.XMLHTTP")
    }
    return xhttp
}

function sendResultAsJSON(result) {
    var request = createRequest();
    request.open('POST', '/result', true);
    var json_obj = { "result": result };
    request.send(JSON.stringify(json_obj))
}

function workCycle() {
    var request = createRequest();
    var result = false;
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            result = getNames(request.responseText)
        }
    };
    request.open('GET', '/get-text', false);
    request.send();
    if (result) {
        sendResultAsJSON(result)
    }
}

function doWork() {
    for (var i = 0; i < 3; i++ ) {
        workCycle()
    }
}


doWork();