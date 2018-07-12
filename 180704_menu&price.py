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
    
def crawling_list(html,params):
    html=driver.page_source
    soup=BeautifulSoup(html, 'html.parser')
    
    group_data=OrderedDict()
    data=[]
    output=[]
    data_all=[]
    data_all_output=[]
    count=0
    
    for name in soup.find_all('p','tit') :
        menu_name=name.get_text()
        menu_name=menu_name.strip()
        if(1<len(menu_name)): 
            nameList=list(menu_name.split('\n'))     
            data.extend(nameList)
            
    for price in soup.find_all('p','p-price02') :
        menu_price=price.get_text()
        menu_price = re.sub(r'\\+','', menu_price).strip()

        priceList=list(menu_price.split('\n'))     
        data.extend(priceList)
    
        count+=1
            
    divide(count,data,output)
    for i in range(0,count):
        data_all.extend([output[0][i], output[1][i]])

    divide(2,data_all,data_all_output)
    
    group_data[params]=data_all_output
    print(json.dumps(group_data, ensure_ascii=False, indent="\t"))
    #save_csv(output)
    save_json(group_data)
    
def crawing_page(i,params):
    driver.get(''+str(i))
    params=params
    crawling_list(driver.page_source,params)
    
crawing_page(2,"coffee&drink")
crawing_page(3,"cake")
