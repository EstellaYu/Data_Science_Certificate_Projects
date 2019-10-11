# Tableau - Citi Bike Analytics

### CITIBIKE, CITILIFE -- [Explore on Tableau Public](https://public.tableau.com/profile/estella.yu#!/vizhome/CitiBikeCitilife/CitibikeCitylife?publish=yes)

![Citi-Bikes](https://github.com/EstellaYu/Data_Science_Certificate_Projects/blob/master/Tableau/citibike.gif)

## About citibike and data source
[Citibike](https://en.wikipedia.org/wiki/Citi_Bike) is a privately owned public bicycle sharing system serving the New York City boroughs of Manhattan, Queens, and Brooklyn, as well as Jersey City, New Jersey. Named after lead sponsor Citigroup.Since established in May 2013, Citi Bike rapidly gain popularity in NYC due to its convenience. Up to date, Citibike as over `840+ stations`, `14,000+ bikes`, `380,000+ annual subscribers`, `4,000,000+ share rides` (in Aug 2019 alone!). 

#### Data Source: 
Since 2013, the Citi Bike Program has implemented a robust infrastructure for collecting data on the program's utilization. Through the team's efforts, each month bike data is collected, organized, and made public on the [Citi Bike Data](https://www.citibikenyc.com/system-data) webpage.

In this work, a Tableau dashboard will be implemented in order to provide answers to some curious audience (like you are) :)

## Task

1. aggregate the data found in the Citi Bike Trip History Logs. 
2. Design visualizations for discovered phenomena. 

**FAQ**
* Where are the bike stations located? 

* What are the most popular stations & routes in this month (Aug 2019)?

* What are the peak hours in which bikes are used during a week?

* What is the gender breakdown of active participants (Male vs. Female)?

* What are the membership breakdown of active participant (Customer vs. Subscriber)? 

* How does the average trip duration change by age?

**Next, as a chronic over-achiever:**

* Use visualizations (does not have to be all of them) to design a dashboard for each phenomena.
* The dashboards are accompanied with an analysis explaining why the phenomena may be occuring. 
* Create a Tableau story that brings together the visualizations, maps, and dashboards.

## Discoveries:
1. BIKE STATIONS & ROUTES
    * The bike stations are heavily centered around Manhattan, Jersey City, as well as part of downtown Brooklyn. 
    * The most popular stations in Aug 2019 is `Pershing Square North` (which is in downtown manhattan and near train station, and thus might contribute to its popularity)
    * The routes are generally in short distances, and short trip durations. Shorter routes, higher the popularity
2. RUSH HOURS
    * There are clear patterns in the bike usage at different times of the day: 
        -- on Monday to Fridays, peak hours are sync with rush hours (~7am and 6pm)
        -- on weekends, peak hours are around noon (just the right time to come out for lunch!)
3. USER TYPE STATISTICS
    * Clear patterns are observed in differnt user types as well, for example, Subscribers dominates the user group (80% of the users are subscribers, and only 20% users are customers)
    * Subscribers have an average age of 30 years old, while customers' average age is ~25 years old. 
    * Avearge trip duration/ride is relatively constant through out different age range, but Customers tends to ride a longer route compared to subscribers.
3. GENDER STATISTICS
    * Male user are domanent (only 25% users are female, and <10% users do not specify their gender)
    * Many of the customers do not specify their gender. And these gender-unspecified customers tend to have a longer ride. 

