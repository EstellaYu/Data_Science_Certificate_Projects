# Data Science Certificate Projects
Homework and Project works, working towards a certificate  
* [**VBA & Excel**](https://github.com/EstellaYu/Data_Science_Certificate_Projects#vba--excel)  
| Pivot Table | VBA Macro |  

* [**Python and Jupyter Notebook**](https://github.com/EstellaYu/Data_Science_Certificate_Projects#python-and-jupyter-notebook)  
| Python | Pandas | Matplotlib | API |  

* [**SQL**](https://github.com/EstellaYu/Data_Science_Certificate_Projects#sql)  
| SQL script | SQLAlchemy |

* [**Web-Design -- HTML and CSS**](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/README.md#web-developement)  
| HTML | CSS | Bootstrap | Webscraping | Splinter | Flask | MongoDb |

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
