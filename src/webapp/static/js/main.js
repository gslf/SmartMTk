// ////////////////////////////
// SmartMTk controls managemant


// Create & bind joystick
initJoystick();
bindJoystick1();
bindJoystick2();


// Bind keyboard
initKeyboard()


//////////////////////////////
// Alarm managemant

// Status loop
function mainLoop(){
	// Check alarm status
	$.getJSON('/status', function(data){
		console.log(data);
		if(data.alarm){
			$('#alarm_text').html('ALARM');
			$('#alarm_text').addClass('red_text').removeClass('green_text');
			$('#alarm_defuse').prop('disabled', false);
		}
	});

	// Loop
	setTimeout(mainLoop, 1000);
}
mainLoop();


// Defuse Alarm button
$('#alarm_defuse').click(function(){
	// Switch tracking option
	$.ajax({
		url: '/defusealarm',
		type: 'POST'  });
	
	$('#alarm_text').html('NO ALARM');
	$('#alarm_text').addClass('green_text').removeClass('red_text');
	$this.prop('disabled', true);

});

// Motion Detection button
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
