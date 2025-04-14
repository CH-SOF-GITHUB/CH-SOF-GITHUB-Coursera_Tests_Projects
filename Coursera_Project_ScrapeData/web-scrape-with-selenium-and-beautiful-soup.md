The Plan
Our goal is to assemble data from the disparate tables of Olympedia into one concise [CSV], 
housing all the stats we require and nothing more. In broad strokes we will need to:

Identify the page(s) with the information we want and review the source code.
Outline a path for navigating the pages and forms to access the data we’re targeting.
Implement the Selenium methods to navigate the course we’ve chosen.
Pass the content of each page to Beautiful Soup to parse.
Export all the data we’ve collected with the csv standard Python library.

The [Olympedia.org] site has a fairly simple layout structured around a navigation bar at the top, 
as the main way finding element, with dropdowns for several categories such as “Athletes” and “Countries”.

![Olympedia site]

Under the “Statistics” dropdown we can select “Medals by Country”, which leads us to a page with 
a table of medal counts by country for every Olympic games ever contested. 
Above the table are several dropdowns that we can use to filter the results 
(e.g. Olympic year, discipline, gender, etc).

By selecting the year of a given Olympics, and a gender, 
we can highlight the total medals won as well as the breakdown by medal type for that year. 
To collect the data required for our chart we must extract the values for team USA 
for every summer Olympics, by gender. In other words, we must select each (summer Olympic) 
year from the dropdown in turn to update the table with the medal information for that event, 
for both the men and women.

Navigating a Webpage
[Selenium] is fundamentally an automation library: it provides tools for interacting with webpages 
and their elements hands-free. The first step of our data collection script is to create 
a driver object, an instance of a browser that we can manipulate with Selenium methods.