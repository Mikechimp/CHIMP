```bash
curl -sSik https://198.248.86.124:443/
```

[/home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_curl.html](file:///home/kali/rp1/results/198.248.86.124/scans/tcp443/tcp_443_https_curl.html):

```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Fri, 02 May 2025 23:40:14 GMT
Content-Type: text/html
Content-Length: 10382
Last-Modified: Wed, 15 Nov 2017 17:43:48 GMT
Connection: keep-alive
ETag: "5a0c7cd4-288e"
Accept-Ranges: bytes

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=no" />
<title>Speedtest | Kansas State University</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Kansas State University official speedtest.">

    <meta name="author" content="Kansas State University">
    <link rel="profile" href="http://microformats.org/profile/hcard">
    <link rel="shortcut icon" href="https://s.ksucloud.net/k-state-static/2011/favicon.ico">
    <link rel="icon" sizes="192x192" href="https://s.ksucloud.net/k-state-static/touch-icon-192x192.png">
    <link rel="apple-touch-icon-precomposed" sizes="180x180" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-180x180-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-152x152-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-120x120-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="76x76" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-76x76-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://s.ksucloud.net/k-state-static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="https://s.ksucloud.net/k-state-static/2011/apple-touch-icon-precomposed.png"><!-- 57×57px -->
    <meta property="og:site_name" content="Kansas State University">
    <meta property="og:title" content="">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://s.ksucloud.net/k-state-static/2011/touch-icon-192x192.png">
    <meta property="og:url" content="">
    <meta property="og:description" content="">

    <link rel="stylesheet" href="https://s.ksucloud.net/k-state-static/dist/4.5.0/css/2011/2011.min.css">

<style type="text/css">
	html,body{
		border:none; padding:0; margin:0;
		background:#FFFFFF;
		color:#202020;
	}
	body{
		text-align:center;
		font-family:"Roboto",sans-serif;
	}
	h1{
		color:#404040;
	}
	#startStopBtn{
		display:inline-block;
		margin:0 auto;
		color:#6060AA;
		background-color:rgba(0,0,0,0);
		border:0.15em solid #6060FF;
		border-radius:0.3em;
		transition:all 0.3s;
		box-sizing:border-box;
		width:8em; height:3em;
		line-height:2.7em;
		cursor:pointer;
		box-shadow: 0 0 0 rgba(0,0,0,0.1), inset 0 0 0 rgba(0,0,0,0.1);
	}
	#startStopBtn:hover{
		box-shadow: 0 0 2em rgba(0,0,0,0.1), inset 0 0 1em rgba(0,0,0,0.1);
	}
	#startStopBtn.running{
		background-color:#FF3030;
		border-color:#FF6060;
		color:#FFFFFF;
	}
	#startStopBtn:before{
		content:"Start";
	}
	#startStopBtn.running:before{
		content:"Abort";
	}
	#test{
		margin-top:2em;
		margin-bottom:12em;
	}
	div.testArea{
		display:inline-block;
		width:16em;
		height:12.5em;
		position:relative;
		box-sizing:border-box;
	}
	div.testName{
		position:absolute;
		top:0.1em; left:0;
		width:100%;
		font-size:1.4em;
		z-index:9;
	}
	div.meterText{
		position:absolute;
		bottom:1.55em; left:0;
		width:100%;
		font-size:2.5em;
		z-index:9;
	}
	div.meterText:empty:before{
		content:"0.00";
	}
	div.unit{
		position:absolute;
		bottom:2em; left:0;
		width:100%;
		z-index:9;
	}
	div.testArea canvas{
		position:absolute;
		top:0; left:0; width:100%; height:100%;
		z-index:1;
	}
	div.testGroup{
		display:inline-block;
	}
	@media all and (max-width:65em){
		body{
			font-size:1.5vw;
		}
	}
	@media all and (max-width:40em){
		body{
			font-size:0.8em;
		}
		div.testGroup{
			display:block;
			margin: 0 auto;
		}
	}

</style>
<script type="text/javascript">
function I(id){return document.getElementById(id);}
var meterBk="#E0E0E0";
var dlColor="#6060AA",
	ulColor="#309030",
	pingColor="#AA6060",
	jitColor="#AA6060";
var progColor="#EEEEEE";

//CODE FOR GAUGES
function drawMeter(c,amount,bk,fg,progress,prog){
	var ctx=c.getContext("2d");
	var dp=window.devicePixelRatio||1;
	var cw=c.clientWidth*dp, ch=c.clientHeight*dp;
	var sizScale=ch*0.0055;
	if(c.width==cw&&c.height==ch){
		ctx.clearRect(0,0,cw,ch);
	}else{
		c.width=cw;
		c.height=ch;
	}
	ctx.beginPath();
	ctx.strokeStyle=bk;
	ctx.lineWidth=16*sizScale;
	ctx.arc(c.width/2,c.height-58*sizScale,c.height/1.8-ctx.lineWidth,-Math.PI*1.1,Math.PI*0.1);
	ctx.stroke();
	ctx.beginPath();
	ctx.strokeStyle=fg;
	ctx.lineWidth=16*sizScale;
	ctx.arc(c.width/2,c.height-58*sizScale,c.height/1.8-ctx.lineWidth,-Math.PI*1.1,amount*Math.PI*1.2-Math.PI*1.1);
	ctx.stroke();
	if(typeof progress !== "undefined"){
		ctx.fillStyle=prog;
		ctx.fillRect(c.width*0.3,c.height-16*sizScale,c.width*0.4*progress,4*sizScale);
	}
}
function mbpsToAmount(s){
	return 1-(1/(Math.pow(1.3,Math.sqrt(s))));
}
function msToAmount(s){
	return 1-(1/(Math.pow(1.08,Math.sqrt(s))));
}

//SPEEDTEST AND UI CODE
var w=null; //speedtest worker
var data=null; //data from worker
function startStop(){
	if(w!=null){
		//speedtest is running, abort
		w.postMessage('abort');
		w=null;
		data=null;
		I("startStopBtn").className="";
		initUI();
	}else{
		//test is not running, begin
		w=new Worker('speedtest_worker.min.js');
                //w.postMessage('start'); //Add optional parameters as a JSON object to this command
		w.postMessage('start {"telemetry_level":"basic"}'); //Add optional parameters (see doc.md)
		I("startStopBtn").className="running";
		w.onmessage=function(e){
			data=e.data.split(';');
			var status=Number(data[0]);
			if(status>=4){
				//test completed
				I("startStopBtn").className="";
				w=null;
				updateUI(true);
                        }
			I("ip").textContent=data[4];
			I("dlText").textContent=(status==1&&data[1]==0)?"...":data[1];
			I("ulText").textContent=(status==3&&data[2]==0)?"...":data[2];
			I("pingText").textContent=data[3];
			I("jitText").textContent=data[5];
		};
	}
}
//this function reads the data sent back by the worker and updates the UI
function updateUI(forced){
	if(!forced&&(!data||!w)) return;
	var status=Number(data[0]);
	I("ip").textContent=data[4];
	I("dlText").textContent=(status==1&&data[1]==0)?"...":data[1];
	drawMeter(I("dlMeter"),mbpsToAmount(Number(data[1]*(status==1?oscillate():1))),meterBk,dlColor,Number(data[6]),progColor);
	I("ulText").textContent=(status==3&&data[2]==0)?"...":data[2];
	drawMeter(I("ulMeter"),mbpsToAmount(Number(data[2]*(status==3?oscillate():1))),meterBk,ulColor,Number(data[7]),progColor);
	I("pingText").textContent=data[3];
	drawMeter(I("pingMeter"),msToAmount(Number(data[3]*(status==2?oscillate():1))),meterBk,pingColor,Number(data[8]),progColor);
	I("jitText").textContent=data[5];
	drawMeter(I("jitMeter"),msToAmount(Number(data[5]*(status==2?oscillate():1))),meterBk,jitColor,Number(data[8]),progColor);
}
function oscillate(){
	return 1+0.02*Math.sin(Date.now()/100);
}
//poll the status from the worker (this will call updateUI)
setInterval(function(){
	if(w) w.postMessage('status');
},200);
//update the UI every frame
window.requestAnimationFrame=window.requestAnimationFrame||window.webkitRequestAnimationFrame||window.mozRequestAnimationFrame||window.msRequestAnimationFrame||(function(callback,element){setTimeout(callback,1000/60);});
function frame(){
	requestAnimationFrame(frame);
	updateUI();
}
frame(); //start frame loop
//function to (re)initialize UI
function initUI(){
	drawMeter(I("dlMeter"),0,meterBk,dlColor,0);
	drawMeter(I("ulMeter"),0,meterBk,ulColor,0);
	drawMeter(I("pingMeter"),0,meterBk,pingColor,0);
	drawMeter(I("jitMeter"),0,meterBk,jitColor,0);
	I("dlText").textContent="";
	I("ulText").textContent="";
	I("pingText").textContent="";
	I("jitText").textContent="";
	I("ip").textContent="";
}

</script>
</head>
<body>


<header role="banner" id="ksu-header" class="ksu-wrapper--header">
        <nav id="ksu-masthead" class="ksu-nav--top">

  <iframe width="100%" height="50" align="top" style="margin: 0; padding: 0; border:none; overflow: hidden; background: transparent;" allowtransparency="true" frameborder="0" src="https://itsbar.web.k-state.edu/bar/?inline=1"></iframe>

            <a href="http://www.k-state.edu/" class="ksu-wordmark">Kansas State <i>University</i></a>
            <a href="http://search.k-state.edu/" id="ksu-search" class="ksu-search">K-State Search</a>
            <form role="search" id="ksu-search-box" class="ksu-search__box" method="get" action="https://search.k-state.edu/">
                <label for="search">Search web, people, directories</label>
                <input type="search" id="search" name="qt" value="" placeholder="Search web, people, directories">
                <a href="http://www.k-state.edu/directories/">Browse A‐Z</a>
            <a href="#" class="js-close">×</a></form>


        </nav>
</header>



<h1>Kansas State University Speedtest</h1>
<div id="startStopBtn" onclick="startStop()"></div>
<div id="test">
	<div class="testGroup">
		<div class="testArea">
			<div class="testName">Download</div>
			<canvas id="dlMeter" class="meter"></canvas>
			<div id="dlText" class="meterText"></div>
			<div class="unit">Mbps</div>
		</div>
		<div class="testArea">
			<div class="testName">Upload</div>
			<canvas id="ulMeter" class="meter"></canvas>
			<div id="ulText" class="meterText"></div>
			<div class="unit">Mbps</div>
		</div>
	</div>
	<div class="testGroup">
		<div class="testArea">
			<div class="testName">Ping</div>
			<canvas id="pingMeter" class="meter"></canvas>
			<div id="pingText" class="meterText"></div>
			<div class="unit">ms</div>
		</div>
		<div class="testArea">
			<div class="testName">Jitter</div>
			<canvas id="jitMeter" class="meter"></canvas>
			<div id="jitText" class="meterText"></div>
			<div class="unit">ms</div>
		</div>
	</div>
	<div id="ipArea">
		IP Address: <span id="ip"></span>
	</div>
</div>
<!-- <a href="https://github.com/adolfintel/speedtest">Source code</a>   -->
<script type="text/javascript">setTimeout(initUI,100);</script>
</body>
</html>


```
