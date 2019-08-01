# Web Visualization Dashboard (Weather worldwide across all Latitude)

## Background

Data is more powerful when we share it with others! Let's use HTML and CSS to create a dashboard showing the analysis we've done.

![Images/landingResize.png](Images/output_image/landing_page.png)

## Latitude - Latitude Analysis Dashboard with Attitude

In this work, a visualization dashboard website is created using visualizations previously created in [Python API](https://github.com/EstellaYu/Data_Science_Certificate_Projects/tree/master/Python_API). Specifically, we'll be plotting [weather data](Images/img/cities.csv): weather across `500+` cities across the world and plotting the various attributes, `Temprature`, `Windspeed`, `Cloudiness`, `Windspeed` and its relation with `latitude`.

In building this dashboard, individual pages are created for each plot in a means that clients can navigate between them. These pages will contain the visualizations and their corresponding explanations. We'll also have a landing page, a page where we can see a comparison of all of the plots, and another page where we can view the data used to build them.

### Website Description

The website consists 7 pages in total, including:

* A [landing page](#landing-page) containing:
  * An explanation of the project.
  * Links to each visualizations page.
* Four [visualization pages](#visualization-pages), each with:
  * A descriptive title and heading tag.
  * The plot/visualization itself for the selected comparison.
  * A paragraph describing the plot and its significance.
* A ["Comparisons" page](#comparisons-page) that:
  * Contains all of the visualizations on the same page so we can easily visually compare them.
  * Uses a bootstrap grid for the visualizations.
    * The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.
* A ["Data" page](#data-page) that:
  * Displays a responsive table containing the data used in the visualizations.
    * The table must be a bootstrap table component.
    * The data must come from exporting the `.csv` file as HTML, or converting it to HTML. In this application, the `.csv` file is converted to `.html` via `pandas`, and a javascript is written to include the converted HTML into the "Data" page.

The website must, at the top of every page, have a navigation menu that:

* Has the name of the site on the left of the nav which allows users to return to the landing page from any page.
* Contains a dropdown on the right of the navbar named "Plots" which provides links to each individual visualization page.
* Provides two more links on the right: "Comparisons" which links to the comparisons page, and "Data" which links to the data page.
* Is responsive (using media queries). The nav changes background color as window size changes.

The website is deployed [here](http://estellayu.github.io).

When finished, submit to BootcampSpot the links to 1) the deployed app and 2) the GitHub repository.

