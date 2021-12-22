from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url= "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page= requests.get(url)
soup= BeautifulSoup(page.text, 'html.parser')

info_list=[]
star_table= soup.find_all('table')
table_rows= star_table[7].find_all('tr')
for tr in table_rows:
    td= tr.find_all('td')
    row= [i.text.rstrip() for i in td]
    info_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]

for i in range(1, len(info_list)):
    star_names.append(info_list[i][1])
    distance.append(info_list[i][5])
    mass.append(info_list[i][7])
    radius.append(info_list[i][8])

df= pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns=['Star_name','Distance','Mass','Radius'])
print(df)

df.to_csv('dwarf_stars.csv')