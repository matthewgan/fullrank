$(document).ready(function() {
	//Global settings
	var urlBase="http://www.fullrank.cc:8000/iot/";
	var deviceName = "neonlights/";
	var opType = {"shake":"shake","swipeLeft":"swipeleft","swipeRight":"swiperight"};
	var opSet = {"open":"On", "close":"Off"};
	var validStr = "success";
	var kState = "close";
	var delayTime = 5000;

	function sleep(ms) {
		return new Promise(resolve => setTimeout(resolve, ms));
	}

	function sendUrlMsg(kType, kSet) {
		var newUrl = urlBase + deviceName + opType[kType] + opSet[kSet];
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.timeout = 30000;
		xmlhttp.onreadystatechange=function() {
		  if (xmlhttp.readyState==4 && xmlhttp.status==200) {
				var response = xmlhttp.responseText; //if you need to do something with the returned value
				if(response.indexOf(validStr) !== -1){
					if(kSet.indexOf("open") !== -1 ){
						kState = kSet;
						if(kType.indexOf("shake") !== -1){
							document.body.style.backgroundColor = "#00ae6a";
						}
						if(kType.indexOf("swipeLeft") !== -1){
							document.body.style.backgroundColor = "#f17700";
						}
						if(kType.indexOf("swipeRight") !== -1){
							document.body.style.backgroundColor = "#fd447d";
						}
					}
				} else {
					alert(response + ", please try again");
				}
		  }
		}
		xmlhttp.open("GET",newUrl,true);
		xmlhttp.send();
	}

	async function OpShake(){
		sendUrlMsg("swipeLeft","close");
		sendUrlMsg("swipeRight","close");
		sendUrlMsg("shake","open");
		await sleep(delayTime);
		if(kState == "open"){
			sendUrlMsg("shake","close");
			kState = "close";
			document.body.style.backgroundColor = "#2aa6c5";
		};
	}

	async function OpSwipeLeft() {
		sendUrlMsg("shake","close");
		sendUrlMsg("swipeRight","close");
		sendUrlMsg("swipeLeft","open");
		await sleep(delayTime);
		if(kState == "open"){
			sendUrlMsg("swipeLeft","close");
			kState = "close";
			document.body.style.backgroundColor = "#2aa6c5";
		};
	}

	async function OpSwipeRight() {
		sendUrlMsg("shake","close");
		sendUrlMsg("swipeLeft","close");
		sendUrlMsg("swipeRight","open");
		await sleep(delayTime);
		if(kState == "open"){
			sendUrlMsg("swipeRight","close");
			kState = "close";
			document.body.style.backgroundColor = "#2aa6c5";
		};
	}

  $(this).gShake(OpShake);

	swipe({
		onSwipeRight: function(){OpSwipeLeft()},
		onSwipeLeft: function(){OpSwipeRight()},
		onSwipeDown: function(){},
		onSwipeUp: function(){},
		minDistance: '10%',
		unselectable: true
	});
});
