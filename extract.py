from shutil import make_archive
from bs4 import BeautifulSoup as bs
import requests
import lxml
url = 'https://a2oj.com/categories'

response = requests.get( url , stream =True)

if (response.status_code == 200):
    soup = bs( response.content , 'lxml')

table = soup.find("table", attrs={"class":"tablesorter"})
# print(table)
tbody = table.find("tbody")
trows = tbody.find_all("tr")


names =[]
links =[]
base_url = 'https://a2oj.com/'
for row in trows:
    lis = list(row.descendants)
    no = lis[9]
    if ( int(no) != 0 ):
        names.append(lis[6])
        a = lis[5]
        links.append(base_url + a['href'])
import os



dir_path = os.path.join( os.getcwd() , 'categories')

import time
count =1
for i, newlink in enumerate(links):
    response = requests.get(newlink, stream=True)
    soup = bs(response.content, 'lxml')
    table = soup.find("table", attrs={"class": "tablesorter"})
    # print(table)
    tbody = table.find("tbody")
    trows = tbody.find_all("tr")
    items =[]
    for row in trows:
        items.append(row.find_all("td"))
    info =[{ 'link':item[1].a['href'] , 'name':item[1].a.text,'judge':item[3].text } for item in items]
    print(len(info))
    try:
        with open(os.path.join(dir_path , names[i]+'.csv') , 'w') as f:
            f.write('link,name,judge')
            f.write('\n')
            for ii in info:
                f.write(('{},{},{}').format(ii['link'], ii['name'] , ii['judge']))
                f.write('\n')
            f.close()
    except:
        with open(os.path.join(dir_path, str(count) + 'pro.csv'), 'w') as f:
            f.write('link,name,judge')
            f.write('\n')
            for ii in info:
                f.write(('{},{},{}').format(
                    ii['link'], ii['name'], ii['judge']))
                f.write('\n')
            f.close()
        time.sleep(2)
        continue
    time.sleep(2)

from shutil import make_archive
source = os.path.join(os.getcwd(), 'myarchive')
target = os.path.join(os.getcwd(), 'categories')
print(make_archive(source, 'zip', target))












