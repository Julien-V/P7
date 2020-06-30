function changeHeight() {
	let ih = window.innerHeight.toString();
	let html = document.querySelector('html');
	html.setAttribute('style', 'height:'+ih+'px;');
}

window.addEventListener('resize', changeHeight);
window.addEventListener('orientationchange', changeHeight);

changeHeight();