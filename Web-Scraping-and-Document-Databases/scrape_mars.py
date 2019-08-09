# Scrape Mars information 

########## 1. import dependencies ###########
import pandas as pd
from datetime import datetime as dt

from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

############# 2. scrape data ##############

### 2.1 Launch Driver
# launch chromedriver -- get an empty page
def launch_browser():
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path, headless=False)
	return browser


############# data scraping functions ##############
### 2.2 NASA Mars News Site (https://mars.nasa.gov/news/)
def scrape_mars_news(isPrint, browser):
	url_mars_news = 'https://mars.nasa.gov/news/'
	browser.visit(url_mars_news)
	time.sleep(2)

	# collect the latest News Title and Paragraph Text
	soup = bs(browser.html, 'html.parser')

	content = soup.body.find_all('li', class_='slide')

	news = []

	for cont in content:
	    # find article_title
	    title_div = cont.find('div', class_='content_title')
	    weblink = 'https://mars.nasa.gov' + title_div.a['href']
	    title = title_div.a.text.strip()
	    
	    # find article teaser (abstract)
	    abstract_div = cont.find('div', class_='article_teaser_body')
	    abstract = abstract_div.text
	    
	    # find article publish date
	    list_date = cont.find('div', class_='list_date')
	    date = dt.strptime(list_date.text, '%B %d, %Y')
	    
	    # built a dictionary
	    dict = {"date": date, "title": title, "weblink": weblink, "abstract": abstract}
	    
	    news.append(dict)

	# print an example from scraping
	if isPrint == True: 
		print("\nExample Scraped Content:")
		print('---------------------------------')
		print("{")
		for key in news[0]:
		    print("    ", key, ":", news[0][key])
		print("}\n")  

	print('\nMars News Scraped!')

	return news[0]


### 2.3 Scrap `JPL Mars Space Feature Images` (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
def scrape_jpl_img(isPrint, browser):
	# use the same browser (same tag) to visit another url
	url_jpl_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(url_jpl_img)
	time.sleep(2)

	# collect the Feature Image HTML
	soup = bs(browser.html, 'html.parser')

	content = soup.body.find('section', class_='primary_media_feature').find('article', class_="carousel_item")

	img_href = content['style'].split("url('")[1].split("')")[0]
	featured_image_url = 'https://www.jpl.nasa.gov' + img_href

	# print an example from scraping
	if isPrint == True:  
		print("\nExample Scraped Content:")
		print('---------------------------------')
		print(featured_image_url,'\n')

	print("\nFeature Image url Scraped!") 

	return featured_image_url

### 2.4 Scrap Mars Weather Twitter (https://twitter.com/marswxreport?lang=en)
def scrape_mars_weather(isPrint, browser):
	# use the same browser (same tag) to visit another url
	url_mars_weather = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(url_mars_weather)
	time.sleep(2)
	# collect the latest News Title and Paragraph Text
	soup = bs(browser.html, 'html.parser')
	tweets = soup.body.find_all('li', class_='stream-item')
	weather_post_by_MarsWxReport = []

	for tweet in tweets:
	    post = tweet.find('div', class_='tweet')
	    if post['data-screen-name'] == "MarsWxReport":
	        post_text = post.find('p', class_='tweet-text').text
	        if "InSight sol" in post_text:
	            weather_post_by_MarsWxReport.append(post_text.split('hPa')[0] + 'hPa')

	# print an example from scraping
	if isPrint == True:
		print("\nExample Scraped Content:")
		print('---------------------------------')
		print(weather_post_by_MarsWxReport[0],'\n')

	print('\nWeather Data Scraped!')

	return weather_post_by_MarsWxReport[0]


### 2.5 Scrap Mars Fact (https://space-facts.com/mars/)
def scrape_mars_fact(isPrint, browser):
	# use the same browser (same tag) to visit another url
	url_mars_fact = 'https://space-facts.com/mars/'
	browser.visit(url_mars_fact)
	time.sleep(2)

	mars_fact = pd.read_html(browser.html)

	# get the MARS FACT table
	mars_fact_df = mars_fact[1]

	for i in range(len(mars_fact_df)):
	    mars_fact_df.iloc[i,0] = mars_fact_df.iloc[i,0][0:-1] # get rid of the ":"

	mars_fact_df.columns = ["Profile", 'Value']
	# mars_fact_df.set_index('Profile', inplace = True)
	mars_fact_html = mars_fact_df.to_html()

	# some process to make the table looks better
	# 1. make it a real "table"
	mars_fact_html = mars_fact_html.replace("dataframe","table table-striped table-hover table-sm ").replace("<thead", '''<thead class="thead-dark"''')
	print(mars_fact_html)
	file = open("templates/mars_fact.html",'w+')
	file.write(mars_fact_html)
	file.close()

	if isPrint == True: 
		print("\nExample Scraped Content:")
		print('---------------------------------')
		print(mars_fact_html)
		print()

	print("\nMars Fact HTML Scraped!")

	return mars_fact_html


### 2.6 Scrap USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
# use the (same tag) to visit another url
def scrape_hemispere(isPrint, browser):
	
	url_mars_hemisphere = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(url_mars_hemisphere)
	time.sleep(2)

	soup = bs(browser.html, 'html.parser')

	content_div = soup.body.find('div', class_='collapsible results').find_all('div',class_='item')

	hemisphere_image_urls = []

	for i in range(len(content_div)):    
	    title = content_div[i].find('h3').text
	    
	    # click the image title
	    browser.find_link_by_partial_text(title).first.click()
	    soup_find_img = bs(browser.html, 'html.parser')
	    img_url = soup_find_img.find('div', class_='downloads').find('a')['href']

	    # add to dictionary
	    img_dict = {"title": title, "img_url": img_url}
	    hemisphere_image_urls.append(img_dict)
	    
	    # roll back to the previous img
	    browser.back()

	# print an example from scraping
	if isPrint == True: 
		print("\nExample Scraped Content:")
		print('---------------------------------')
		print("{")
		for key in hemisphere_image_urls[0]:
		    print("    ", key, ":", hemisphere_image_urls[0][key])
		print("}\n")  

	print("Mars Hemisphere Image Scraped")

	return hemisphere_image_urls 

def scrape():

	# would you prefer printing the sample scraped data?
	isPrint = False
	browser = launch_browser()

	mars_news = scrape_mars_news(isPrint, browser)
	jpl_feature_img = scrape_jpl_img(isPrint, browser)
	mars_weather = scrape_mars_weather(isPrint, browser)
	mars_fact = scrape_mars_fact(isPrint, browser)
	hemisphere_url = scrape_hemispere(isPrint, browser)

	browser.quit()

	scrape_dict = { "mars_news" : mars_news,
					"featured_image_url": jpl_feature_img,
					"mars_weather": mars_weather,
					"mars_fact" : mars_fact,
					"hemisphere_url": hemisphere_url}
	print("Data Scraping Finished!")
	return scrape_dict
