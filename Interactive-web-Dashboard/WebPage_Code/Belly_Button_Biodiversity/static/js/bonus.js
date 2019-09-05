function buildGauge(data){
var level = data;

// Trig to calc meter point
var degrees = 180-(level)*36/2;
    radius = 0.5;
var radians = degrees * Math.PI / 180;
var x = radius * Math.cos(radians);
var y = radius * Math.sin(radians);

// Path: may have to change to create a better triangle
var mainPath = 'M -.0 -0.035 L .0 0.035 L ',
     pathX = String(x),
     space = ' ',
     pathY = String(y),
     pathEnd = ' Z';
var path = mainPath.concat(pathX,space,pathY,pathEnd);

var data = [{ type: 'category',
   x: [0], y:[0],
    marker: {size: 28, color:'850000'},
    showlegend: false,
    name: 'weekly scrubs',
    text: level,
    hoverinfo: 'text+name'},
  { values: [3,3,3,3,3, 15],
  rotation: 90,
  
  text: ['8+', '6-8', '4-6', '2-4','0-2',  ''],
  textinfo: 'text',
  textposition:'inside',      
  marker: {colors:['rgba(14, 127, 0, .5)', 
                    'rgba(110, 154, 22, .5)',
                    'rgba(170, 202, 42, .5)', 
                    'rgba(202, 209, 95, .5)',
                    'rgba(210, 206, 145, .5)', 
                    'rgba(255, 255, 255, 0)']},
  labels: ['8+', '6-8', '4-6', '2-4','0-2'],
  hoverinfo: 'label',
  hole: 0.5,
  type: 'pie',
  showlegend: false
}];

var layout = {
  shapes:[{
      type: 'path',
      path: path,
      fillcolor: '850000',
      line: {
        color: '850000'
      }
    }],
  title: {
    text: '<b>Belly Button Washing Freqency</b><br>Scrubs per week',
  },
  titlefont: {size: 20},
  height: 500,
  width: 500,
  xaxis: {type:'category',zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]},
  yaxis: {type:'category',zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]}
};

Plotly.newPlot('gauge', data, layout);
}
