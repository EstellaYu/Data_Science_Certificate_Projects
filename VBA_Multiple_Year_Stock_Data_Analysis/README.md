VBA/Macro analysis on multiple years (2014 - 2016) stocks data

### Description of Raw Data

* [test data file](alphabetical_testing.xlsx) - test file with tickers sorted in alphabetical order
* [Stock data file](Multiple_year_stock_data.xlsx) - contains real stock data for years 2014, 2015 and 2016

  - The each worksheet contains the stocks data for 1 year (2014, 2015 or 2016)
  - ~3,000 stocks are contained in each worksheet (depending on each year)
  - data at every row: <ticker>, <date>, <open price>, <high>, <low>, <close price>, <volume>

 ### Analysis done in this work

 * Easy 
  - sum up the annual stock volume for each ticker
  - tabulate resuls in a summary table next to the raw data 

 * Moderate, for each ticker: 
  - sum up the annual stock volume 
  - calcualte the annual price difference
  - calcualte the annual percentaage price change
  - tabulate resuls in a summary table next to the raw data 
  - lable the cell with annual price difference with different fill color
  		- green if net price is positive
  		- red if net price is negative

 * "Difficult", for each ticker: 
  - finish all requirements in Moderate level
  - add a second summary table, showing the ticker & value for the stock
  		-  with the greatest % increase
  		-  with the greatest % decrease
  		-  with the greatest total annual volume 

### Result for the "Difficult" level
* [2014 result](2014_VBA_Multiple_years_Stocks_Data_Analysis.png)
* [2015 result](2015_VBA_Multiple_years_Stocks_Data_Analysis.png)
* [2016 result](2016_VBA_Multiple_years_Stocks_Data_Analysis.png)

