function showContentW(url) {
 var iframe = document.getElementById("wheater-iframe");
     iframe.src = url;
}

function showContentW2(url) {
 var iframe = document.getElementById("wheater2-iframe");
     iframe.src = url;
}

function showContentWs(url) {
 var iframe = document.getElementById("wheaters-iframe");
     iframe.src = url;
}

function showContentWs2(url) {
 var iframe = document.getElementById("wheaters2-iframe");
     iframe.src = url;
}

function showContentpreciptation(url) {
 var iframe = document.getElementById("preciptation-iframe");
     iframe.src = url;
}

function showContentpreciptation2(url) {
 var iframe = document.getElementById("preciptation2-iframe");
     iframe.src = url;
}

function showContentjetstream(url) {
 var iframe = document.getElementById("jetstream-iframe");
     iframe.src = url;
}

function showContentjetstream2(url) {
 var iframe = document.getElementById("jetstream2-iframe");
     iframe.src = url;
}

function showContentwindspeedGlobal(url) {
 var iframe = document.getElementById("windspeed-iframe");
     iframe.src = url;
}

function showContentwindspeedGlobal2(url) {
 var iframe = document.getElementById("windspeed2-iframe");
     iframe.src = url;
}


function wheaterGlobal() {
	showContentW('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt_t2_d1.png');
	showContentW2('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt2_t2_d1.png');

}

function wheaterSeaGlobal() {
	showContentWs('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt_sst_d1.png');
	showContentWs2('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt2_sst_d1.png');

}

function preciptationGlobal() {
	showContentpreciptation('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt2_prcp-mslp_d1.png');
	showContentpreciptation2('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt_prcp-mslp_d1.png');

}

function jetstreamGlobal() {
	showContentjetstream('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt_ws250-mslp_d1.png');
	showContentjetstream2('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt2_ws250-mslp_d1.png');

}

function windspeedGlobal() {
	showContentwindspeedGlobal('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt2_ws10_d1.png');
	showContentwindspeedGlobal2('https://climatereanalyzer.org/wx/todays-weather/input/gfs_world-wt_ws10_d1.png');

}
// Security Cleaner
// Delete all items in localStorage
localStorage.clear();
