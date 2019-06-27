# Python API - What's the Weather Like?

## Background

Whether financial, political, or social -- data's true power lies in its ability to answer questions definitively. So let's take what you've learned about Python requests, APIs, and JSON traversals to answer a fundamental question: "What's the weather like as we approach the equator?"

Now, we know what you may be thinking: _"Duh. It gets hotter..."_

But, if pressed, how would you **prove** it?


## WeatherPy

In this report, you'll see a Python script to visualize the weather of 500+ cities across the world of varying distance from the equator. 
* Citipy API will be used to gather the city names from randomly generated (Lat, Lng) coordinates, 
* OpenWeatherMap API will be used to obtain weather across world cities.

A series of scatter plots are generated to showcase the following relationships:

* Temperature (F) vs. Latitude
* Humidity (%) vs. Latitude
* Cloudiness (%) vs. Latitude
* Wind Speed (mph) vs. Latitude

