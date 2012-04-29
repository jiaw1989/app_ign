$(document).ready(function(){
 $('body').append('<div id="screencss"></div>');
 adjustCSS();
 $(window).resize(function(){ adjustCSS() });
})


function adjustCSS(){
	var pageWidth = $(window).width();
	alert(pageWidth);
	if(pageWidth < '1280') 
	// This time we're targeting all resolutions between 800 and 1280 pixels wide
	{
	getcss('css/liquid_web.css');
	//And we want to load the .css file named "1024x768.css"
	}
	else 
	{
	getcss('css/big.css');
	//This else statement has "if" condition. If none of the following criteria are met, load 1280x1024.css
	}

}
function getcss(cssfile){
loadcss = document.createElement('link')
loadcss.setAttribute("rel", "stylesheet")
loadcss.setAttribute("type", "text/css")
loadcss.setAttribute("href", cssfile)
document.getElementsByTagName("head")[0].appendChild(loadcss)

}
