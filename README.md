# retailwhiskeystore
In this project, we'll walk throught the creation of a data architect for a whiskey retail store that enables the shop managers to make better desicions.
I'll start with ETL process to get whiskey data into the company's central database. 
The data is extracted via https://www.thewhiskyexchange.com via python using webscrapping.
Data will be stored in the central database. Then, I will design a data warehouse that extract data from central database and 
provide a single source of relevant data for various departaments.
At the end, I'll create various visualizations that will assist in quick desicions making.

Part 1.- Web Scrapping:
To get the data from the retail shop, I'll scrape the website https://www.thewhiskyexchange.com/ 
I will use python request and beatiful to scrape the data and create a scraper object using OOP  

The main class is called whiskey_web_scrapping and has the following methods:

I. scrape_html
I will use the method GET request via request and create the soup object 

![image](https://user-images.githubusercontent.com/101696287/183009346-16830e76-d314-4e05-8f51-0b209dacbd36.png)

II. Get page content & page price
I will use these two objects to extract specific objects within the soup object. These objects contain name, alcohol amount, percent and price of each whiskey



