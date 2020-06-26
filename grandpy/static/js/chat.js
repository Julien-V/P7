$(document).ready(function() {
	$("#user-action").submit(function(e){
		e.preventDefault(e);
		ask($(this));
	});
	// global mapsNumber
	mapNumber = 0;
});

function displayInChat(msg) {
	$('#displayMsg').append(msg);
	var chat = document.querySelector('#displayMsg');
	chat.scrollTop = chat.scrollHeight - chat.clientHeight;
}

function processResponse(json) {
	// format grandpy's response
	console.log(json)
	var msg = "<div class='msg'>";
	msg += "<p>"+json.response+"</p>";
	msg += "</div>";
	displayInChat(msg);
	// get json.g_maps
	var param_map = json.g_maps;
	if (param_map != null) {
		var geometry = param_map.geometry;
		var name = param_map.name;
		var f_address = param_map.formatted_address;
		// display div map
		var mapId = "maps-"+mapNumber.toString();
		var msg = "<div class='msg map' id='"+mapId+"'>";
		msg += "</div>";
		displayInChat(msg);
		// display G Maps
		var map = new google.maps.Map(document.getElementById(mapId), {
			center: geometry.location,
			zoom: 4
		});
		// display marker
		var marker = new google.maps.Marker({position: geometry.location, map: map});
		mapNumber += 1;
	};
	// get json.wiki
	var param_wiki = json.wiki;
	if (param_wiki != null) {
		var wTitle = param_wiki.title;
		var wText = param_wiki.extract;
		var wUrl = param_wiki.url;
		var msg = "<div class='msg'>";
		msg += "<p>"+wText+"</p>";
		msg += "<a href='"+wUrl+"'>[En savoir plus sur Wikipedia]</a>"
		msg += "</div>";
		displayInChat(msg);
	};
	//return false;
};

function ask(form) {
	var url = form.attr('action');
	var data = form.serialize();
	// var text = data.substring(data.search("=")+1) faster ?
	var text = $('#inputText').val();
	$('#inputText').val('');
	// format text
	var msg = "<div class='msg user'>";
	msg += "<p>"+text+"</p>";
	msg += "</div>";
	// display msg
	displayInChat(msg);
	// ask grandpy
	$.post(
		url,
		data,
		processResponse,
		'json'
	);
};

