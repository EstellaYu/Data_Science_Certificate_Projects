# Data Analysis and Advanced Data Visualization

Practice Practice Practice (makes perfect).. 

* [**VBA & Excel**](https://github.com/EstellaYu/Data_Science_Certificate_Projects#vba--excel)  
| Pivot Table | VBA Macro |  

* [**Python and Jupyter Notebook**](https://github.com/EstellaYu/Data_Science_Certificate_Projects#python-and-jupyter-notebook)  
| Python | Pandas | Matplotlib | API |  

* [**SQL**](https://github.com/EstellaYu/Data_Science_Certificate_Projects#sql)  
| SQL script | SQLAlchemy |

* [**Web-Design -- HTML, CSS and Javascript**](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/README.md#web-developement)  
| HTML | CSS | Bootstrap | Webscraping | Splinter | Flask | MongoDb | Javascript

* [**Interactive Web Visualization**](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/README.md#interactive-web-visualization)  
| Javascript | Plotly.js | D3.js | Flask | Heroku | Leaflet

* [**Tableau**](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/README.md#tableau)  
| Tableau Dashboards |

## VBA & Excel
| Pivot Table | VBA Macro |
1. [Multiple Years Stock Data Analysis in **VBA**](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/VBA_Multiple_Year_Stock_Data_Analysis)  
    * Analyze `~3,000 stocks` between `2014`-`2016`, including `annual exchange volumn`, `price difference`, `percentage difference`.
    * `Conditional formatting` results, and output `top performers` and `worst performers` across multiple criteria.

## Python and Jupyter Notebook
| Python | Pandas | Matplotlib | API | 
1. [**Python** Script](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Python_Challenge) :  
    1) [Profit/Loss analysis on Banking data](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Python_Challenge/PyBank)
        * determine timestamps (in months) for the data provided
        * obtain monthly average Profit/Loss, output the month with `greatest profit` and `biggest loss`
    2) [Voting Count analysis](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Python_Challenge/PyPoll)  
        * analyze voting results of size `38,000,000+`
        * obtain available `candidate list`, `voting counts` for each candidate, and `output overall winners` 
    
    
2. [**Pandas** Data Wrangling](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Pandas_Data_Wrangling)
    1)  [Game Sales Analysis](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Pandas_Data_Wrangling/Game_Sale_Analysis)  
        * analyze the sale of a digial game, obtain player stats, including palyers' gender and age
        * analyze game sales based on players' `gender`, `age group`, as well as the `most popular` and `profitable items`
    2)  [Standard Test result and School Performance](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Pandas_Data_Wrangling/School_Analysis)  
        * analyze the standard test results across a local district, obtain `district-wise test result summary`, and `summary for each school`
        * analyze school performances both for `top performing schools` and `worst performing schools`, and provide insights on test result based on `school budget`, `school type`, `school size`, etc.


3. [**Matplotlib** Data Visualization](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Matplotlib_Visualization): 
    1)  [Car Rides data visualization](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Matplotlib_Visualization/Pyber)  
         * visulize relationship between `number of rides` in each city, and `cost of rides`
         * analyze car rides data based on `city type`, `driver numbers`, `ride cost`, ect.
         
    
    2)  [Clinical trial results analysis](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Matplotlib_Visualization/Pymaceuticals)  
         * analyze `drug effects` on **mice's tumor size** across the `clinital trials` of `9 different drugs`
         * obtain `drug performance` based on `survival rate`, `Metastatic spread`, and `tumor size response over time`
    
    
4. [**API** requests with Python](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Python_API)
    1)  [Weather variation across differnt latitudes](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Python_API)  
         * use `CityPy` and `OpenWeatherMap` API, randomly obtain local weather for **500+** cities worldwide
         * analyze weather variation acorss differnt **latitude**, including `temperature`, `humidity`, `cloudiness`, and `wind speed`

## SQL
| SQL script | SQLAlchemy |
1. [**SQL** Script](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/SQL) :  
   * Analyze `employment, title, and salary data` from a coporate from 1980s to 1990s, with `~30k` employee records.
   * **Design** Database structure, **create** SQL _tables_, **customized query** through different tables
   * **Visualize** and analyze data in `SQLAlchemy`
   
## Web Developement
| HTML | CSS | Bootstrap | Webscraping | Splinter | Flask | MongoDb |
1. [**Web dashboard** Data Visaulization](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Web-development):
   * Create web-dashboard for data visulization 
   * Extract the weather across `500+` cities across the world and plotting various attributes, including `Temprature`, `Windspeed`, `Cloudiness`, `Windspeed` and its relation with `latitude`.
   * Combine **HTML**, **CSS** and **Bootstrap** for webpage formatting
   
2. [**Web Scraping** Mission to Mars](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Web-Scraping-and-Document-Databases)
   * **Web scraping** from 5 different websites, and EXTRACT information related to `Mission to Mars`
   * TRANSFORM the information into a `dictionary`, and store the input into **MongoDb**
   * RETRIEVE and LOAD data from database, and use **Flask** to deploy the content in a single HTML file
   
3. [**Javascript** UFO record -- interactive filter](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Javascript)
   * Load UFO data from `data.js`
   * Create interactive filter result by constraining `Datetime`, `Country`, `State`, `City` and `Shape`    

## Interactive Web Visualization
| Flask | Javascript | Plotly.js | D3.js | Heroku | Leaflet
1. [**Flask, Plotly.js, and Heroku** -- Interactive Web Dashboard](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Interactive-web-Dashboard)
   * Analyze `Belly Button Biodiversity data` from 135 individuals, where over `~3k` microorganisms are identified.
   * **Create** Interactive Dashboards using `Plotly.js`, including _Pie chart_, _Guage plot_, and _Bubble plot_.
   * Each selection correspond to the data of a different individual, **retrieve** data from `SQLite database`, **Update** visualization base on use's selection
   * [**Deploy** interactive dashboard on Heroku](https://belly-button-biodiversity-ply.herokuapp.com) 
   
2. [**D3.js** -- US Health Index](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Interactive_Data_Journalism-D3)
   * **Create** interactive bubble plot visualization with `switchable axes`
   * Each x-axis and y-axis can be **clicked independantly**, and the data points are displayed coordingly, with smooth **transition effects** on the `data point`, `state abbreviation`, and `axis range display`
   * **Create** interactive tooltip on each data point, with transition effects during `mouse over` and `mouse out` events
   * [**Deploy** interactive dashboard on page](https://estellayu.github.io/Image/Projects/D3_interactive_vis/index.html) 

3. [**Leaflet** -- World Earthquake GeoJSON Visualization](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Geomapping)
   * **Query** `live world earthquake` data and `tectonic plate boundary` data in `.geijson` format
   * **Create** interactive Geomapping visualization, with swithable baseMaps, and independent controllable overlayMaps
   * [**Deploy** interactive dashboard on page](https://estellayu.github.io/Image/Projects/geomapping/index.html) 
   
## Tableau
| Tableau Visualization |
1. [**NYC Citibike Analysis**](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Tableau)
   * **Create** dashboard and story analyzing Citibike user statistics, rush hour, most popular routes & stations, ect. 
