// /////////////////////////////////
// Keyboard Utils
// Bind keys to monster track movement functions


function initKeyboard(){

	// Bind keys
	$(document).keydown(function(e) {

		// W KEY
		if(e.keyCode==87){
			forward();
		}		
		
		// S KEY
		else if(e.keyCode==83){
			backward();
		}

		// D KEY
		else if(e.keyCode==68){
			right();
		}

		// A KEY
		else if(e.keyCode==65){
			left();
		}
		

	});

	$(document).keyup(function(e) {

		// W KEY
		if(e.keyCode==87){
			shortBrake();
		}		
		
		// S KEY
		else if(e.keyCode==83){
			shortBrake();
		}

		// D KEY
		else if(e.keyCode==68){
			straight();
		}

		// A KEY
		else if(e.keyCode==65){
			straight();
		}else{
		}

	});

}
