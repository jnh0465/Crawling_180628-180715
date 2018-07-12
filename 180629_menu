from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
from selenium import webdriver
from collections import OrderedDict

driver=webdriver.Chrome('')      
driver.get('')

def save_csv(output):
    dataframe=pd.DataFrame(output)
    dataframe.to_csv(".csv", mode='a', header=False, index=False, encoding='euc-kr')
    
def save_json(group_data):
    with open('.json', 'a', encoding="EUC-KR") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")
        
def divide(div,data,output):
    start=0
    end=len(data)                             
    for idx in range(start, end + div, div):
        out=data[start:start + div]
        if out !=[]:
            output.append(out)
        start=start+div
        
def crawing_page(i,params):
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/ul/li['+str(i)+']/a').click()
    params=params
    crawling_list(driver.page_source,params)
    
def crawling_list(html,params):
    html=driver.page_source
    soup=BeautifulSoup(html, 'html5lib')

    group_data=OrderedDict()
    data=[]
    output=[]

    for name in soup.select('ul li strong') :
        menu_name = name.get_text()
        menu_name = re.sub('\n+'," ", menu_name)
        menu_name = re.sub('개인정보취급방침'," ", menu_name).strip()
        if(1<len(menu_name)):             
            nameList=list(menu_name.split('\n'))                           
            data.extend(nameList)
            
    divide(1,data,output)

    group_data[params]=output
    print(json.dumps(group_data, ensure_ascii=False, indent="\t") )
    #save_csv(output)
    save_json(group_data)

crawing_page(1,"---")
crawing_page(2,"salad_menu")
crawing_page(3,"---")
crawing_page(4,"---")
crawing_page(5,"---")
crawing_page(6,"---")
