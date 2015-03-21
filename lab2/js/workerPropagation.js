/**
 * Created by mandriy on 3/9/15.
 */


include('/js/utils.js');

function include(url) {
    var script = document.createElement('script');
    script.src = url;
    document.getElementsByTagName('head')[0].appendChild(script)
}

 var worker

 function propagate() {
    if(typeof(Worker) !== "undefined") {
        if(typeof(worker) == "undefined") {
            worker = new Worker("js/cluster.js")
        }
    } else {
        alert("Sorry, web workers are not supported in your browser. Please, check out fro new versions.")
    }
 }

 function finishWork() {
    worker.terminate()
 }