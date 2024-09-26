import re
import sys
import requests
from bs4 import BeautifulSoup
import csv
import lxml
from itertools import zip_longest

titles=[]
companies=[]
locations=[]
times=[]
skills=[]

response = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

if response.status_code != 200:
    sys.exit(f"Failed to retrieve page with status code: {response.status_code}")

src = response.content

soup = BeautifulSoup(src, 'lxml')

jobs = soup.find_all('div', {'class': 'css-1gatmva e1v1l3u10'})
#print(jobs)


for i, job in enumerate(jobs):
    title = job.find('h2', {'class': 'css-m604qf'})
    comapny = job.find('a', {'class': 'css-17s97q8'})
    location = job.find('span', {'class': 'css-5wys0k'})
    time_posted = job.find('div', {'class': 'css-d7j1kk'})
    job_skills = job.find_all('a', {'class': 'css-5x9pm1'})

    titles.append(title.text.strip())
    companies.append(comapny.text.strip(' - '))
    locations.append(location.text.strip())

    skill = ', '.join([skill.text.strip('· ') for skill in job_skills])
    skills.append(skill)

    # Getting the times posted
    time = time_posted.text.strip()
    match = re.search(r"\d \w+ \w+", time, flags=re.IGNORECASE)
    times.append(match.group(0))

file_list = [titles, companies, locations, times, skills]
exported = zip_longest(*file_list)


with open("wuzzuf_python_jobs.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(exported)

    print("File succesfully written")
