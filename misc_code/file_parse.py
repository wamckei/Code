# start virtual environment   -    python3 -m venv path/to/venv source path/to/venv/bin/activate

import csv
import pandas as pd

#Read in master csv 
df = pd.read_csv("ks_views.node_21719846719499.csv")
#Filter for host names that include US and ND to filter for DC only
df = df[df['Host Name'].str.contains('US', na=False) & df['Host Name'].str.contains('ND', na=False)]

#Column list for data frame
column_list = ["Host Name", "Block Serial No.", "CPU Count", "Core Count", "SSD Count", "HDD Count", "NVME Count"]
#write data to new CSV
df.to_csv('nutanix_out.csv', columns = column_list, mode='a', index=False, header=True)

#create new column for Distrobution center in nutanix_out,csv
df = pd.read_csv("nutanix_out.csv")
#create empty Distrobution center column
df['Distrobution Center'] = ''
#create empty Procurement Date column
df['Procurement date'] = ''
#create empty column Depreciation Schedule
df['Refresh Year'] = ''
#create empty column for cluster name
df['Cluster Name'] = ''
#write data back to CSV
df.to_csv('nutanix_out.csv', index=False)

#Data manipulation on the data frame
df = pd.read_csv("nutanix_out.csv")
#build distro center data 
df["Distrobution Center"] = df["Host Name"].str.slice (2,7)
#parse out date hardware was built based on SN
df['temp'] = df['Block Serial No.'].str.removeprefix('OM')
#populate procurement date with first 2 intergers from block serial#
df['Procurement date'] = df['temp'].str.slice(0,2)
#append 20 to procurement dates for year 20xx
df['Procurement date'] = '20' + df['Procurement date'].astype(str)
#populate cluster name column with data 
df['Cluster Name'] = df['Host Name'].str[:-5] + '-VIP'
#calculate refresh year 
df['Refresh Year'] = df['Procurement date'].astype(int)
#Calculate renweal year
df['Refresh Year'] = df['Refresh Year'].add(6)
#Drop temp column
df = df.drop('temp', axis=1)
#write data back to CSV
df.to_csv('nutanix_out.csv', index=False, header=True)