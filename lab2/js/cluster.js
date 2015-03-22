/**
 * Created by mandriy on 3/3/15.
 */

importScripts('utils.js');

function sendResultAsJSON(result) {
    var request = createRequest();
    request.open('POST', '/result', true);
    var json_obj = { result: result };
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

function doWork(e) {
    for (var i = 0; i < 3; i++ ) {
        workCycle()
    }
}

self.addEventListener('message', doWork);