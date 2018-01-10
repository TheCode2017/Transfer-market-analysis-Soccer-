#Extracting data from wikipedia using Beautiful soup
import requests
from bs4 import BeautifulSoup
import pandas as pd
wiki_url="https://en.wikipedia.org/wiki/List_of_English_football_transfers_summer_2017"
req=requests.get(wiki_url)
soup=BeautifulSoup(req.content,'lxml')
table_classes={"class":["sortable","plainrowheaders"]}
wikitables = soup.find("table",class_="wikitable sortable")


#Extracting the information to a list
col1=[]
col2=[]
col3=[]
col4=[]
col5=[]
for row in wikitables.findAll("tr"):
    cells=row.findAll("td")
    if(len(cells)==5):
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
        
#Converting the list to a dataframe 
#import pandas to convert list to data frame
df=pd.DataFrame(A,columns=['Date'])
df['Name']=B
df['Moving from']=C
df['Moving to']=D
df['Fee']=E
df.to_csv("C:/opt/spark/spark-2.2.1-bin-hadoop2.7/transfer.csv")

print(df)




#Expirementing on the data
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib
import matplotlib.pyplot as plt
#To display the number of players each club has sold in the summer market
sold=transfer.iloc[:,2].values
val,freq=np.unique(sold,return_counts=True)
zipped=zip(val,freq)#Zipping the val and counts list elementwise into a single list.This returns a zipped object
print(list(zipped))#To print the zipped object we need to use list()


#To display the number of players each club has bought in the summer market
buy=transfer.iloc[:,3].values
val1,freq1=np.unique(buy,return_counts=True)
print(list(zip(val1,freq1)))






#Extracting data from wikipedia using MS Excel
from pyspark.sql import SparkSession
#The entry point to all functionality in Spark is the SparkSession class.Created using Saprksession.builder
spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
#sc = SparkContext.getOrCreate()
#Read the data and store it in a dataframe(oandas dataframe)
transfer=pd.read_csv("C:/opt/transferexcel.csv",sep=",")
#Counting the number of incoming and outgoing players for three clubs
incoming=transfer['Moving to'].str.contains('Manchester United|Barcelona|Manchester City').value_counts()[True]
outgoing=transfer['Moving from'].str.contains('Manchester United|Barcelona|Manchester City').value_counts()[True]
print(incoming)
print(outgoing)
transfer['Date']=pd.to_datetime(transfer['Date'])#Transforming the 'date' column to date format(%Y%m%d)
#print(transfer)
## Convert Spark DataFrame to Pandas
#pandas_df = young.toPandas()
# Create a Spark DataFrame from Pandas
#spark_df = context.createDataFrame(pandas_df)Creating a Spark Dataframe from pandas dataframe 
transfer_spark=spark.createDataFrame(transfer)
transfer_spark.createOrReplaceTempView("transfer")#Create a temporary view of the dataframe
#Selecting transfers within a date range in SQL
sql_transfer=spark.sql("SELECT * FROM transfer WHERE Date>='2017-02-02' AND Date <'2017-06-03'").show()
