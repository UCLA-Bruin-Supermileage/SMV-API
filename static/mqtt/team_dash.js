
/*****************
MAP FUNCTION
******************/
document.addEventListener('DOMContentLoaded', () => {

    //Intialize Map
    var map = L.map('map', {
        center: [34.0699, -118.4438], //set to UCLA
        zoom: 15
    });

    //OSM Map tiles
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    var polyline;

 
/*****************
WEBSOCKET FUNCTION
******************/
//NEW: WebSocket
let chatSocket = 0;
if (window.location.protocol == "https:") {
    chatSocket = new WebSocket(
        'wss://'
        + window.location.host
        + '/ws/teamview'
    );
} else {
    chatSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/teamview'
    );
}
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    switch (data['module']) {
        case 'daq.speed':
            //Speed Data
            x_time.push(Date().getTime());
            y_time.push(data['content'])
            break;
        case 'daq.location':
            console.log(data['content'])
            coords = [data['content'].lat, data['content'].long]
            console.log(coords)
            if (polyline) {
                polyline.addLatLng([data['content'].lat, data['content'].long])
                map.fitBounds(polyline.getBounds());
            } else {
                var polyline = L.polyline([coords], {color: 'red'}).addTo(map);
                map.fitBounds(polyline.getBounds());
                
            }
        //TODO: implement rest of the cases for all dashboard modules
        default:
            break;
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
var polyline = L.polyline([[34.0583555,-118.4432201]], {color: 'red'}).addTo(map);
map.fitBounds(polyline.getBounds());
// polyline.addLatLng();
// L.marker([34.0709835,-118.4460503]).addTo(map);
})


