# Flask App 
# 1. Constructing Scraping Function 
# 2. Store Data in MongoDB
# 3. Format webpage
# 4. run Web on Flask app

########### 1. Dependencies #################
from flask import Flask, redirect ,render_template
from datetime import datetime as dt
import pymongo

import scrape_mars

########## 2. Connection with MongoDB #######
# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
# create DataBase 'marsData'
db = client.marsData

########## 3. Flask App ####################

app = Flask(__name__)

@app.route("/")
def index():
	mongo_dict = db.mars_Data_Collection.find()
	for dict in mongo_dict:
		return render_template("index.html", dict = dict)
	
@app.route("/scrape")
def scrape_data():
	scrape_dict = scrape_mars.scrape()
	# Drops collection if available to remove duplicates
	db.mars_Data_Collection.drop()

	# store data to MongoDB server
	db.mars_Data_Collection.insert(scrape_dict)

	# Redirect back to home page
	return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

########## sample data dict #################
# data_dict = {'mars_news': {'date': '2019-8-5', 
# 							'title': "NASA 'Optometrists' Verify Mars 2020 Rover's 20/20 Vision", 
# 							'weblink': 'https://mars.nasa.gov/news/8499/nasa-optometrists-verify-mars-2020-rovers-2020-vision/', 
# 							'abstract': 'Mars 2020 rover underwent an eye exam after several cameras were installed on the rover.'
# 							}, 
# 			'featured_image_url': 'https://www.jpl.nasa.gov/spaceimages/images/wallpaper/PIA18297-1920x1200.jpg', 
# 			'mars_weather': 'InSight sol 233 (2019-07-23) low -98.8ºC (-145.9ºF) high -25.7ºC (-14.2ºF)\nwinds from the SE at 4.6 m/s (10.2 mph) gusting to 16.2 m/s (36.2 mph)\npressure at 7.60 hPa', 
# 			'mars_fact': '<table border="1" class="dataframe">\n  <thead>\n    <tr style="text-align: right;">\n      <th></th>\n      <th>Profile</th>\n      <th>Value</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Equatorial Diameter</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Polar Diameter</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Mass</td>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Moons</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Orbit Distance</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Orbit Period</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Surface Temperature</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>First Record</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Recorded By</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>', 
# 			'hemisphere_url': [{'title': 'Cerberus Hemisphere Enhanced', 
# 								'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
# 								},
# 								{'title': 'Schiaparelli Hemisphere Enhanced', 
# 								'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
# 								}, 
# 								{'title': 'Syrtis Major Hemisphere Enhanced', 
# 								'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
# 								}, 
# 								{'title': 'Valles Marineris Hemisphere Enhanced', 
# 								'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'
# 								}
# 							]}