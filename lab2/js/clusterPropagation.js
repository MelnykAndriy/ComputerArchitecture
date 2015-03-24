/**
 * Created by mandriy on 3/9/15.
 */


 var worker;

 function propagate() {
     document.getElementById("body_id").setAttribute('onunload', "worker.terminateWorker()");
    if(typeof(Worker) !== "undefined") {
        if(typeof(worker) == "undefined") {
            worker = new Worker("js/cluster.js");
            worker.addEventListener('message', function(e) {

            });
            worker.postMessage('start');
        }
    } else {
        alert("Sorry, web workers are not supported in your browser. Please, check out fro new versions.")
    }
 }

