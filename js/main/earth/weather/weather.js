function showContentW(url) {
 var iframe = document.getElementById("wheater-iframe");
     iframe.src = url;
}

function showContentW2(url) {
 var iframe = document.getElementById("wheater2-iframe");
     iframe.src = url;
}

function wheaterGlobal() {
	showContentW('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt_t2_d1.png');
	showContentW2('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt2_t2_d1.png');

}

// Security Cleaner
// Delete all items in localStorage
localStorage.clear();
