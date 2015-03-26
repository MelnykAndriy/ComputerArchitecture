/**
 * Created by mandriy on 3/9/15.
 */


var worker;

function terminateWorker() {
    if (typeof worker !== 'undefined') {
        worker.terminate()
    }
}

function propagate() {
    if(typeof(Worker) !== "undefined") {
        if(typeof(worker) == "undefined") {
            document.getElementById("body_id").setAttribute('onunload', "terminateWorker");
            worker = new Worker("js/cluster.js");
            worker.postMessage('start');
        }
    } else {
        alert("Sorry, web workers are not supported in your browser. Please, check out fro new versions.")
    }
}

