# Belly Button Biodiversity

In this work, an interactive dashboard will be built to explore the [Belly Button Biodiversity DataSet](http://robdunnlab.com/projects/belly-button-biodiversity/).

### Do you know what lives in your belly button? 

![Bacteria by filterforge.com](Images/Web_image.png)

## 1 - Build Flask API using Plotly.js

Use `Plotly.js` to build interactive charts for the dashboard.
* Display the sample metadata from the route `/metadata/<sample>`
  * Display each key/value pair from the metadata JSON object somewhere on the page.
  ![Meta Chart](Images/metadata.png)

* Create a `PIE chart` that uses data from samples route (`/samples/<sample>`) to display the top 10 samples.
  ![PIE Chart](Images/pie_chart.png)

* Create a `Bubble Chart` that uses data from samples route (`/samples/<sample>`) to display each sample.

  ![Bubble Chart](Images/bubble_chart.png)
  
* Adapt the `Gauge Chart` to plot the Weekly Washing Frequency obtained from the `/metadata/<sample>`route.
  ![Weekly Washing Frequency Gauge](Images/gauge.png)


* Update all of the plots any time that a new sample is selected.
* Test the routes by visiting each one in the browser.


## 2 - Heroku

Deploy the Flask app to Heroku.



