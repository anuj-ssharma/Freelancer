import requests
from bs4 import BeautifulSoup
import csv
import time

response = requests.get("https://www.freelancer.co.nz/job")
soup = BeautifulSoup(response.text,"html.parser")
section1 = soup.find(id="category-1")

filter_categories = ['PHP','HTML','Web Development','Java','Ecommerce development'
                     'Other - Software Development','HTML5','Software Development','.NET'
                     ,'Angular.js','Web Development','Programming','ASP.NET',
                     'QA & Testing','Coding','Joomla','Computer Security','ASP',
                     'Backend Development','Full Stack development']

lists = section1.find("ul")
categories = lists.find_all("a",class_="PageJob-category-link")

list_categories = []
timestamp = time.strftime("%Y-%m-%d")

for cat in categories:
    str = cat.get_text().strip()
   # print(str)
    if len(str) > 4:
        category_name = str.split("(")[0].strip()
        jobs = str.split("(")[1].split(")")[0]
        print(str + " : " + category_name)
        if any(category_name in category for category in filter_categories):
            list_categories.append([timestamp,category_name,jobs])


csvFile = open("categories.csv",'a')
csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
for cat in list_categories:
    csvWriter.writerow(cat)
csvFile.close()
