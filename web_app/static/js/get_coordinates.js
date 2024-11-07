
$(document).ready(function () {
    var sat_id=document.getElementById("sat-coord").dataset.satId;
    get_coordinates(sat_id);
    setInterval(function () {
        get_coordinates(sat_id);
    }, 5000);
});



/**
 * Makes a POST request to "/get_coordinates/" with the given sat_id.
 * If the server returns a 200 status, updates the innerText of the
 * "alt", "lat", and "lng" elements with the values provided by the server.
 * If the server returns a different status, does nothing.
 * @param {number} sat_id - the id of the satellite to get coordinates for
 */
function get_coordinates(sat_id) {
    ajax = new XMLHttpRequest();
    ajax.open("POST", "/get_coordinates/", true);
    ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    ajax.send("sat_id=" + sat_id);
    ajax.onreadystatechange = function () {
        if (ajax.readyState == 4 && ajax.status == 200) {
            var data = JSON.parse(ajax.responseText);
            console.log(data);
            document.getElementById("alt").innerText = data.alt;
            document.getElementById("lat").innerText = data.lat;        
            document.getElementById("lng").innerText = data.lng;
        }
        else {
            ;
        }
    };
}
