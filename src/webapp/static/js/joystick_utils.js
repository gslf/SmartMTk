// ///////////////////////////
// Joystick Utils
// Virtual Joystick managemant 


// Joystick reference var
var joystick1
var joystick2


// Init joystick
function initJoystick(){
	joystick1 = nipplejs.create({
		zone: document.getElementById('joystick_area1'),
		color: 'gray'
	});

	joystick2 = nipplejs.create({
		zone: document.getElementById('joystick_area2'),
		color: 'gray'
	});

}

// ---------------------------------------------
// Joystick 1
// Bind joystic events with handler function
function bindJoystick1(){
	joystick1.on('start end', function(evt, data) {
		manageJoystick1Movements(evt, data)
	}).on('plain:up plain:down', function(evt, data) {
		manageJoystick1Movements(evt, data);
	});
}


// Joystic event handler function
function manageJoystick1Movements(evt, data){
	
	// Brake if user release joystick
	if(evt.type == "end"){
		shortBrake();
	}else{
		if(data.direction != undefined){
		
			// Manage direction forward/backward
			if(data.direction.y == "up"){
				forward();
			}else if(data.direction.y == "down"){
				backward();
			}
		}
	}
	
}

// ---------------------------------------------
// Joystick 2
// Bind joystic events with handler function
function bindJoystick2(){
	joystick2.on('start end', function(evt, data) {
		manageJoystick2Movements(evt, data)
	}).on('plain:left plain:right', function(evt, data) {
		manageJoystick2Movements(evt, data);
	});
}


// Joystic event handler function
function manageJoystick2Movements(evt, data){
	
	// Brake if user release joystick
	if(evt.type == "end"){
		straight();
	}else{
		if(data.direction != undefined){
			
			// Manage direction left/right
			if(data.direction.x == "right"){
				right();
			}else if (data.direction.x == "left"){
				left();
			}
		}
	}
	
}
