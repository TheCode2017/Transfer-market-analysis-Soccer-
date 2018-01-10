# Transfer-market-analysis-Soccer-
The aim of the project is to analyze the 2017 soccer transfer market and derive useful results on the number of transfers made by clubs all over the world .


#Things learned:

1.How to scrap data from a website using BeautifulSoup.

2.How to load the scraped data into a pandas dataframe.

3.How to scrap data from a website using MS EXCEL.

4.Differences between pandas dataframe and Spark Dataframe.

In this project I extract data from the wikipedia website (https://en.wikipedia.org/wiki/List_of_English_football_transfers_summer_2017) using two methods:

a) Beautiful Soup: In this method I identify the table that I want to extract(in this case the first table in the website) and using its classname "wikitable sortable" I store the information in .lxml format.Then I transfer this information into a list which I then use to ultimately transfer the contents to pandas dataframe.However some columns('Date' and 'Fee') were not properly displayed as you can see in the output files.

b) In order to properly scrap the data from the website I followed a simpler approach,scraping using MS-EXCEL.
I performed the following steps:

Open MS Excel->Data->From Web->Enter the URL of the webpage that you want to scrap->Select Table 1.

The table will be neatly extracted into MS Excel and all the columns are properly displayed as shown in the output image.Save this as a .csv file. Using pandas.read_csv I loaded this data into a dataframe and started playing with the data.
I wrote some code to explore the data and find out the following:

1.The number of players sold by a club.

2.The number of players bought by a club.


Then I converted the pandas dataframe to a Spark dataframe which enabled me to run complex SQL queries on the data.For example I was able to return a list of transfers made within a specific date range by a club or set of clubs as shown in the output.

Then I was able to explore the data further and extract out information such as the number of players sold and bought by each club involved in the transfer market.

I have learnt a lot about SPARK,BeautifulSoup,MS-Excel by doing this pet project.Keep learning everyday!
