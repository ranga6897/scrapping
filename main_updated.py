#from scrapping_functions import builders,leroy,buco,cashbuild
from scrapp import builders,leroy,buco,cashbuild
from database_functions import  create_table,updateMultipleRecords


# import urllib.request
import pandas as pd
import sqlite3 as lite

con = lite.connect('price_details.db')

create_table(con)  # for creating the table from the given data

df = pd.read_sql_query("select * from data;", con) #reading the table as a dataframe
df.fillna(0,inplace = True) #replacing None values with 0, bcoz  None cannot be passed into function
df[['builders_sku','leroy_sku','buco_sku','cashbuild_sku']] = df[['builders_sku','leroy_sku','buco_sku','cashbuild_sku']].astype('int') #bcoz sku should be int


# get prices from related websites
df['builders_price'] = df['builders_sku'].apply(lambda x:builders(x) if x > 0 else '')
df['leroy_price'] = df['leroy_sku'].apply(lambda x:leroy(x) if x > 0 else '')
df['buco_price'] = df['buco_sku'].apply(lambda x:buco(x) if x > 0 else '')
df['cashbuild_price'] = df['cashbuild_sku'].apply(lambda x:cashbuild(x) if x > 0 else '')


# output
df.to_csv('sample_output.csv')

# records needed to update:
temp = df[['builders_price','leroy_price','buco_price','cashbuild_price','id']].values
records_to_update = []
for row in temp:
    records_to_update.append(tuple(row))


# updating data-base records
updateMultipleRecords(records_to_update,con)


