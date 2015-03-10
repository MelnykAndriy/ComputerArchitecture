/**
 * Created by mandriy on 3/9/15.
 */

 var worker

 function propagate() {
    alert('propagate')
    if(typeof(Worker) !== "undefined") {
        if(typeof(w) == "undefined") {
            worker = new Worker("js/cluster.js");
        }
    } else {
        alert("Sorry, web workers are not supported in your browser. Please, check out fro new versions.")
    }
 }

 function finishWork() {
    worker.terminate()
 }