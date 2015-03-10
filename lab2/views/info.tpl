
% rebase('base.tpl', title='Processing info')
<div class="container">
  <script src="js/infoManager.js" />
  <h1>Processing info.</h1>
  </br> </br>
  <p style="font-size:20px">Nodes running:  <b id="nodesNumber">0</b> </p>
  <p style="font-size:20px">Percentage of done work:  <b id="doneWorkPercentage">0%</b> </p>
  <p>Progress bar:</p>
  <div class="progress">
    <div class="progress-bar progress-bar-success" role="progressbar" style="width:0%">
      Done
    </div>
    <div class="progress-bar progress-bar-warning progress-bar-striped active" role="progressbar" style="width:0%">
      In progress
    </div>
    <div class="progress-bar progress-bar-danger" role="progressbar" style="width:100%">
      Remaining work
    </div>
  </div>
</div>