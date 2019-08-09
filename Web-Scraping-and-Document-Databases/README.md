# Mission to Mars

![mission_to_mars](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/Web-Scraping-and-Document-Databases/templates/Images/image.jpeg)

In this work, a web application is built to scrape various websites for data related to the __`Mission to Mars`__ and displays the information in a single HTML page. The following outlines the detail process.

## 1 - Scraping

The initial scraping is performed using `Jupyter Notebook`, `BeautifulSoup`, `Pandas`, and `Splinter`.
see [`mission_to_mars.ipynb`](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Web-Scraping-and-Document-Databases/Scraping_notebook) for more detail. 

#### 1.1 NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 

```python
# Example:
news_title = "NASA 'Optometrists' Verify Mars 2020 Rover's 20/20 Vision"

news_p = "Mars 2020 rover underwent an eye exam after several cameras were installed on the rover."
```

#### 1.2 JPL Mars Space Images - Featured Image

* Visit the url for [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

* Obtain the image url to the full size `.jpg` image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA14884-1920x1200.jpg'
```

#### 1.3 Mars Weather

* Visit the [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'InSight sol 245 (2019-08-05) low -99.9ºC (-147.8ºF) high -25.6ºC (-14.1ºF) winds from the SSE at 4.6 m/s (10.2 mph) gusting to 17.7 m/s (39.5 mph) pressure at 7.60 hPa'
```

#### 1.4 Mars Facts

* Visit the [Mars Facts webpage](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Use Pandas to convert the data to a HTML table string, and saved as [`mars_fact.html`](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/Web-Scraping-and-Document-Databases/templates/mars_fact.html)

#### 1.5 Mars Hemispheres

* Visit the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Splinter will ask the browser to __click each of the links__ to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.

* Append the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## 2 - MongoDB and Flask Application

`MongoDB` and `Flask` are used to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Jupyter notebook is converted into a __Python script__ called [`scrape_mars.py`](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/Web-Scraping-and-Document-Databases/scrape_mars.py) with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, a route called `/scrape` is created that will import your `scrape_mars.py` script and call the `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called [`index.html`](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/Web-Scraping-and-Document-Databases/templates/index.html) that will take the mars data dictionary and display all of the data in the appropriate HTML elements.

And the resulting web page is displayed in the [beginning of the page](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Web-Scraping-and-Document-Databases#mission-to-mars) :)
