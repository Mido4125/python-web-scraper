import requests
from bs4 import BeautifulSoup
import csv
import lxml
from itertools import zip_longest

titles=[]
companies_names=[]
location_names=[]
times=[]
levels=[]

response = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

src = response.content

soup = BeautifulSoup(src, 'lxml')

job_titles = soup.find_all('h2', {'class': 'css-m604qf'})
companies = soup.find_all('a', {'class': 'css-17s97q8'})
locations = soup.find_all('span', {'class': 'css-5wys0k'})
time_posted = soup.find_all('div', {'class': 'css-d7j1kk'})
job_level = soup.find_all('div', {'class': 'css-y4udm8', 'class': 'css-4c4ojb'})
#print(time_posted)

for i in range(len(job_titles)):
    titles.append(job_titles[i].text.strip())
    companies_names.append(companies[i].text.strip())
    location_names.append(locations[i].text.strip())
    times.append(time_posted[i].text.strip())
    #levels.append(job_level.text.strip())
    print(times[i])

