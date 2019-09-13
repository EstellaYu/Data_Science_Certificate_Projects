# D3 - Data Journalism

## Welcome to the newsroom! 
<p align="center">
  <img src = "https://media.giphy.com/media/v2xIous7mnEYg/giphy.gif">
</p>
<hr>

![Animation](https://github.com/EstellaYu/D3_Challenge---Interactive_Data_Journalism/blob/master/WebPageCode/static/data/animation.gif)

## Background

In this work, the goal is to analyze the current trends shaping people's lives, as well as creating charts, graphs, and interactive elements to help readers understand your findings.

A series of feature stories about the health risks facing particular demographics are produced, based on the information from the `U.S. Census Bureau` and the `Behavioral Risk Factor Surveillance System`.

The data set included with the assignment is based on `2014 ACS 1-year estimates`: [https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml](https://factfinder.census.gov/faces/nav/jsf/pages/searchresults.xhtml). The current data set incldes data on `rates of income`, `obesity`, `poverty`, etc. by state. 

MOE stands for "margin of error."

## The Task

### 1: D3 Dabbler

1. Create a sample scatter plot between two of the data variables, such as `Healthcare vs. Poverty`.

2. Using the D3 techniques, create a scatter plot that represents **each state** with **circle elements**. 

    1. pull in the data from `data.csv` by using the `d3.csv` function
    2. Creat an `index.html`, and code the graphic in the `app.js` file.

3. Include **state abbreviations** in the circles.

4. Create and situate axes and labels to the left and bottom of the chart.


- - -

### 2: More Data, More Dynamics

Why make a static graphic when D3 lets you interact with your data?

#### Switchable axes

1. Place additional labels in the scatter plot and give them **click events** so that users can decide which data to display. 
2. Animate the transitions for the circles' locations as well as the range of the axes. 

#### Incorporate d3-tip

1. Add tooltips to the circles and display each tooltip with the data that the user has selected.

