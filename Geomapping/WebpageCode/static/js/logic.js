// ///////////////////////////////// //
// CREATE BASE LAYERS  ///////////// //
// ///////////////////////////////// //

// 1. SATALITE MAP
var satalite_map = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.satellite",
  accessToken: API_KEY
})
// 2. LIGHT MAP
var light_map = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
})
// 3. OUTDOOR MAP
var outdoors_map = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: API_KEY
})
// create a base map
var baseMaps = {
    Satellite: satalite_map,
    GreaySacale: light_map,
    Outddor: outdoors_map
}

// ///////////////////////////////// //
// ADD DATA POINTS ON MAP ////////// //
// ///////////////////////////////// //
// retrieve earthquake data .geojson
var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
var boundary_link = "static/data/Plates_GeoJSON/PB2002_boundaries.json"

// main function 
d3.json(url, function(eq_data){      
    d3.json(boundary_link, function(b_data){
    var earthquake_Layer = create_Earthquake_Layer(eq_data);
    var plateBoundary_Layer = create_PlateBoundary_Layer(b_data);
    myMap = L.map("map", {
        center : [34, -0.7129],
        zoom : 2,
        layers: [outdoors_map, plateBoundary_Layer,earthquake_Layer]
    });

    var overlayMaps = {
        Earthquake: earthquake_Layer,
        PlateBounary : plateBoundary_Layer
    };
    
    L.control.layers(baseMaps, overlayMaps, {collapsed: false}).addTo(myMap)
    addLegend();
})
})


// ///////////////////////////////// //
// FUNCTIONS  ////////////////////// //
// ///////////////////////////////// //
// markerColor
function markerColor(mag){
    if (mag < 1) return "green";
    else if (mag < 2) return "#A0E500";
    else if (mag < 3) return "#E1E000";
    else if (mag < 4) return "#DD9A00";
    else if (mag < 5) return "#D95600";
    else return "#D51400";
}
// markerSize
function markerSize(mag){
    if (mag <= 6) {
        return 20 * (1-(6 - mag)/(6-1));}
    else return 20;
}

// generate earthquate layer -- add earthquake data
function create_Earthquake_Layer(eq_data){
    var earthquakeLayer = L.geoJson(eq_data.features, {
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
    })
    return earthquakeLayer;
}

// generate plate boundary layer 
function create_PlateBoundary_Layer(b_data){
    console.log(b_data)
    var myStyle = {
        "color": "#ff7800",
        "weight": 3,
        "opacity": 0.7
    };
    var boundaryLayer = L.geoJson(b_data.features, {
        style: myStyle
    })
    return boundaryLayer;
}
// addLegend
function addLegend(){
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
    }