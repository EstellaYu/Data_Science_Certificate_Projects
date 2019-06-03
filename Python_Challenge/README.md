Python data analysis 
(PyBank: analysis on monthly Profit/Loss data; 
 PyPoll: analysis on election result)

### Description of Raw Data

* [PyBank data file](PyBank/Resources/budget_data.csv) - monthly Profit/Loss data (header: Date, Profit/Losses)
* [PyPoll data file](PyPoll/Resources/election_data.csv) - votes (header: Voter ID, County, Candidate)


 ### Analysis done in this work

 #### PyBank
 
  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

 #### PyPoll
  - sum up the annual stock volume 
  - calcualte the annual price difference
  - calcualte the annual percentaage price change
  - tabulate resuls in a summary table next to the raw data 
  - lable the cell with annual price difference with different fill color
  		- green if net price is positive
  		- red if net price is negative 

### Result for both analysis
* [PyBank Result](PyBank/summary.txt)
* [PyPoll Result](PyPoll/summary.txt)
