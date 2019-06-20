// ////////////////////////////
// SmartMTk controls managemant


// Create & bind joystick
initJoystick();
bindJoystick1();
bindJoystick2();


// Bind keyboard
initKeyboard()


// Functions
$('#motion_detection').click(function(){
	// Change button text
	if( $(this).attr('data-status') == "off"){
		$(this).html('STOP');
	  	$(this).attr('data-status', 'on')
		$('#motion_detection_text').html('ACTIVE');
		$('#motion_detection_text').addClass('green_text').removeClass('red_text');
	}else{
		$(this).html('START');
		$(this).attr('data-status', 'off')
		$('#motion_detection_text').html('INACTIVE');
		$('#motion_detection_text').addClass('red_text').removeClass('green_text');
	}

	// Switch tracking option
	$.ajax({
		url: '/motiondetection',
		type: 'POST'  });
});
