/* Forward button managemant */
$("#forward").on('mousedown touchstart',function(){
  $.ajax({
	url: '/forward',
	type: 'POST'  });
});

$("#forward").on('mouseup touchend', function(){
  $.ajax({
	url: '/shortbrake',
	type: 'POST'  });
});


/* Backward button managemant */
$("#backward").on('mousedown touchstart', function(){
  $.ajax({
	url: '/backward',
	type: 'POST'  });
});

$("#backward").on('mouseup touchend', function(){
  $.ajax({
	url: '/shortbrake',
	type: 'POST'  });
});


/* Right steering button managemant */
$("#right").on('mousedown touchstart', function(){
    $.ajax({
	url: '/right',
	type: 'POST'  });

});

$("#right").on('mouseup touchend', function(){
  $.ajax({
	url: '/center',
	type: 'POST'  });
});


/* Left steering button managemant */
$("#left").on('mousedown touchstart', function(){
  $.ajax({
	url: '/left',
	type: 'POST'  });

});
$("#left").on('mouseup touchend', function(){
  $.ajax({
	url: '/center',
	type: 'POST'  });
});
