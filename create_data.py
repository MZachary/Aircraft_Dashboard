import sqlite3
import time
import pandas as pd
from datetime import datetime

#turning off some annoying warnings that are output
pd.options.mode.chained_assignment = None


hz = 5

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

count = 0
total_count = 0
adjusted_time = 0
sample_data = pd.read_csv('sampleTelemData2.csv')

local_time = 0


first_time = time.time()
while True:
    starttime = time.time()
    
    tempdf = sample_data.iloc[[count]]
    local_time = local_time + (1/hz)
    tempdf['local_time'] = [local_time]
    tempdf['time_recorded'] = datetime.now()
    total_count = total_count + 1
    count = count + 1
    if count > len(sample_data)-1:
        count = 0

    tempdf.to_sql('serial_data', connection, if_exists='append', index = False)
    
    # SQL query to retrieve all data from
    # the person table To verify that the
    # data of the csv file has been successfully
    # inserted into the table
    # select_all = "SELECT * FROM serial_data"
    # rows = cur.execute(select_all).fetchall()
    
    # Output to the console screen
    # for r in rows:
        # print(r)
    
    # Committing the changes
    connection.commit()
    
    
    
    #adding some time delay stuff to average 1 second
    this_time = time.time() - starttime
    
    
    
    time.sleep((1/hz)-this_time - adjusted_time)
    
    total_time = time.time() - first_time
    average_time = total_time/total_count
    print(str(average_time))
    
    adjusted_time = average_time - (1/hz)
    
    
    
    # closing the database connection
    # connection.close()
