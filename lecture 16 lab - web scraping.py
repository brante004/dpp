#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path = r'C:\Users\songf\OneDrive - The University of Chicago\Curriculum\Spring 2022\PPHA 30537 Data and Programming I Python\Workbook\dpp\w8_scraping.csv'

response = requests.get(url)
response.text[0:300]

soup = BeautifulSoup(response.text, 'lxml')
target = soup.find('table')
target.find_all('tr')
target.find_all('headers')

unparsed_rows_lab = []
target_row = target.find_all('tr')
for row in target_row:
    row_th = row.find_all('th')
    row_td = row.find_all('td')
    row_data = row_th + row_td
    unparsed_rows_lab.append([data.text for data in row_data])

unparsed_rows_lab[0]
unparsed_rows_lab[1]

parsed_rows_lab = []
for rows in unparsed_rows_lab:
    rows = ','.join(rows)
    rows = rows.replace('\n', '')
    parsed_rows_lab.append(rows)

parsed_rows_lab[0]

document = '\n'.join(parsed_rows_lab)

with open(path, 'w') as ofile:
    ofile.write(document)

document