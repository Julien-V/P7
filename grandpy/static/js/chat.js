
var form = document.querySelector("#user-action");
form.addEventListener('submit', function(e) {
	e.preventDefault(e);
	ask(form);
});
// global mapsNumber
mapNumber = 0;

function displayInChat(msg) {
	var displayMsg = document.querySelector("#displayMsg");
	displayMsg.insertAdjacentHTML('beforeend', msg);
	displayMsg.scrollTop = displayMsg.scrollHeight - displayMsg.clientHeight;
}

function processResponse(json) {
	// format grandpy's response
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
		var msg_maps = "<div class='msg map' id='"+mapId+"'>";
		msg_maps += "</div>";
		displayInChat(msg_maps);
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
		let wTitle = param_wiki.title;
		let wText = param_wiki.extract;
		let wUrl = param_wiki.url;
		let msg = "<div class='msg'>";
		msg += "<p>"+wText+"</p>";
		msg += "<a href='"+wUrl+"'>[En savoir plus sur Wikipedia]</a>"
		msg += "</div>";
		displayInChat(msg);
	};
	//return false;
};

async function ask(form) {
	let url = form.getAttribute('action');
	let data = new FormData(form);
	let inputText = document.querySelector("#inputText");
	let text = inputText.value;
	inputText.value = '';
	// format text
	let msg = "<div class='msg user'>";
	msg += "<p>"+text+"</p>";
	msg += "</div>";
	// display msg
	displayInChat(msg);
	// ask grandpy
	let params = {
		method: 'POST',
		body: data
	};
	let response = await fetch(url, params);
	let rep = await response.json()
	processResponse(rep);
};

