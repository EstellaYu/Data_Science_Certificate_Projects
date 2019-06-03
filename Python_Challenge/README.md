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

 #### PyPoll [38,000,000+ data points]
 
  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

### Result for both analysis
* [PyBank Result](PyBank/summary.txt)
* [PyPoll Result](PyPoll/summary.txt)
