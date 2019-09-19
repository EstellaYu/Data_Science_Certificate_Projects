// ///////////////////////////////// //
// CREATE BASE MAP  //////////////// //
// ///////////////////////////////// //
// create a base map
myMap = L.map("map", {
    center : [34, -0.7129],
    zoom : 2
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
}).addTo(myMap);

// ///////////////////////////////// //
// ADD DATA POINTS ON MAP ////////// //
// ///////////////////////////////// //
// retrieve earthquake data .geojson
var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// main function 
d3.json(url, function(data){
    // console.log(data.features)
    
    L.geoJson(data.features, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, 
                 {
                    radius: markerSize(+feature.properties.mag),
                    fillColor: markerColor(+feature.properties.mag),
                    color: "grey",
                    weight: 0.5,
                    opacity: 1,
                    fillOpacity: 0.8
                })
            },
        onEachFeature: function(feature, layer) {
            layer.bindPopup("<b>Magnitude:</b> <h1>"+ feature.properties.mag +"</h1><hr><b>Where:  </b>" + feature.properties.title + "<br><b>When:  </b>" + new Date(feature.properties.time));
        }
    }).addTo(myMap)
})

// add legends
// Create a legend to display information about our map

var info = L.control({
    position: 'bottomright'
  });
  
  // When the layer control is added, insert a div with the class of "legend"
  info.onAdd = function(myMap) {
    var div = L.DomUtil.create("div", "legend");
        grades = [0, 1, 2, 3, 4, 5],
        labels = [];
        // loop through our density intervals and generate a label with a colored square for each interval
	    for (var i = 0; i < grades.length; i++) {
		div.innerHTML +=
			'<i style="background-color:' + markerColor(grades[i]) + '"></i> ' +
			grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }
        
    return div;
  };
  // Add the info legend to the map
  info.addTo(myMap);

// ///////////////////////////////// //
// FUNCTIONS  ////////////////////// //
// ///////////////////////////////// //
function markerColor(mag){
    if (mag < 1) return "green";
    else if (mag < 2) return "#A0E500";
    else if (mag < 3) return "#E1E000";
    else if (mag < 4) return "#DD9A00";
    else if (mag < 5) return "#D95600";
    else return "#D51400";
}
function markerSize(mag){
    if (mag <= 6) {
        return 20 * (1-(6 - mag)/(6-1));}
    else return 20;
}