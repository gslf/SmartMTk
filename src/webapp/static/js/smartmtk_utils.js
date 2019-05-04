// /////////////////////////////////
// SmartMTk Utils
// Monster track movement functions


var runForward = false
var runBackward = false
var runLeft = false
var runRight = false

// Manage throttle
function forward(){
	
	if(!runForward){
		runForward = true;
		runBackward = false;
	
		$.ajax({
		url: '/forward',
		type: 'POST'  });
	}
}

function backward(){
	if(!runBackward){
		runBackward = true;
		runForward = false;
	
		$.ajax({
		url: '/backward',
		type: 'POST'  });
	}
}

function shortBrake(){
	runBackward = false;
	runForward = false;

	$.ajax({
		url: '/shortbrake',
		type: 'POST'  });
}


// Manage steering
function left(){
	$.ajax({
		url: '/left',
		type: 'POST'  });
}

function right(){
	$.ajax({
		url: '/right',
		type: 'POST'  });
}

function straight(){
	$.ajax({
		url: '/center',
		type: 'POST'  });
}
