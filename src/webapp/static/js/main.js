/* Forward button managemant */
$("#forward").mousedown(function(){
  $.ajax({
	url: '/forward',
	type: 'POST'  });
});

$("#forward").mouseup(function(){
  $.ajax({
	url: '/shortbrake',
	type: 'POST'  });
});


/* Backward button managemant */
$("#backward").mousedown(function(){
  $.ajax({
	url: '/backward',
	type: 'POST'  });
});

$("#backward").mouseup(function(){
  $.ajax({
	url: '/shortbrake',
	type: 'POST'  });
});


/* Right steering button managemant */
$("#right").mousedown(function(){
    $.ajax({
	url: '/right',
	type: 'POST'  });

});

$("#right").mouseup(function(){
  $.ajax({
	url: '/center',
	type: 'POST'  });
});


/* Left steering button managemant */
$("#left").mousedown(function(){
  $.ajax({
	url: '/left',
	type: 'POST'  });

});
$("#left").mouseup(function(){
  $.ajax({
	url: '/center',
	type: 'POST'  });
});
