import requests
from bs4 import BeautifulSoup
import pandas as pd
# empty lists for needed information to be filled later
Jobs=[]
companies=[]
locations=[]
links=[] # needed as every job title has a link to get into and scrap required data
salaries=[] # needed as every page has salaries
page_num=0
# 2- Use requests to fetch the URL you want to look into
while True:
    result=requests.get(f'https://wuzzuf.net/search/jobs/?a=hpb&q=senior%20process%20engineer&start={page_num}')
    # 3- third step to save page contents or markups
    scr= result.content
    # 4- creat soup object to parse the content
    soup=BeautifulSoup(scr,'lxml')
    page_limit=int(soup.find('strong').text)
    if page_num>(page_limit//15):
        print('page limit,terminate')
        break
    # 5- Find the thing you are looking for in the page through `inspect` to find tag andproper class
    Job_titles=soup.find_all('h2',{'class':'css-m604qf'})
    company_names=soup.find_all('a',{'class':'css-17s97q8'})
    location_names=soup.find_all('span',{'class':'css-5wys0k'})
    # 6- loop over to extract needed text from obtained lists in the previous step
    for i in range(len(Job_titles)):
        Jobs.append(Job_titles[i].text)
        companies.append(company_names[i].text)
        locations.append(location_names[i].text)
    # Job_titles[0].find('a').attrs['href']
    # 7 - have each link of job title
    for i in range(len(Job_titles)):
        links.append(Job_titles[i].find('a').attrs['href'])
    print('page switched')
    page_num = page_num + 1
# add added section to the link
added_Section='https://wuzzuf.net'
for i in range(len(links)):
    links[i]= added_Section + links[i]
# 8 - loop for every link in the page to get additional information


    '''
for link in links:
    result = requests.get(link)
    scr = result.content
    soup = BeautifulSoup(scr, 'lxml')
    salriess = soup.find('span', {'class': 'css-4xky9y'})
    salaries.append(salriess.text)
'''
# 15- save to a dataframe and export to CSV if needed
df=pd.DataFrame()
df['jobs']=Jobs
df['companies']=companies
df['locations']=locations
df['links'] = links
df.to_csv('scrapped_data.csv',index=False)





