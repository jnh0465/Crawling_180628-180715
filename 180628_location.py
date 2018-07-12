from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
from selenium import webdriver
from collections import OrderedDict

driver = webdriver.Chrome('driver')        #selenium
driver.get('...........page={}.........')

def save_csv(output):
    dataframe = pd.DataFrame(output)
    dataframe.to_csv("filename.csv", mode='a', header=False, index=False, encoding='euc-kr')
    
def save_json(group_data):
    with open('filename.json', 'a', encoding="EUC-KR") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")

def divide(div,data,output):
    start = 0
    end = len(data)                             
    for idx in range(start, end + div, div):
        out = data[start:start + div]
        if out != []:
            output.append(out)
        start = start + div

def crawling(tables,data):
    for table in tables :
        table_name=table.get_text()
        table_name = re.sub('\n+'," ", table_name)
        table_name = re.sub('\xa0+'," ", table_name).strip()
               
        if(table.find('a')) :   
            if(1<len(table_name)<11): 
                nameList=list(table_name.split('\n'))     
                data.extend(nameList)
            elif(len(table_name)>10):                   
                addressList=list(table_name.split('\n'))
                data.extend(addressList)
                       
        elif(table.find('div',{'class':'tel'})):    
            telList=list(table_name.split('\n'))
            data.extend(telList)
    
def main(html):
    html=driver.page_source
    soup = BeautifulSoup(html, 'html5lib')

    tables = soup.select('tr td') 
    group_data = OrderedDict()
    data = []
    output=[]
    
    crawling(tables,data) 
    divide(3,data,output)

    group_data["name+address+tel"]=output
    print(json.dumps(group_data, ensure_ascii=False, indent="\t") )
    #save_csv(output)
    save_json(group_data)
    
def crawling_tenpage():
    for i in range(3):                                                                           
        for i in range(3,12):
            driver.find_element_by_xpath('//*[@id="storeList"]/div/div/div[2]/div/a['+str(i)+']').click()    #xpath(1부터 10페이지)
            main(driver.page_source)
        driver.find_element_by_xpath('//*[@id="storeList"]/div/div/div[2]/div/a[12]').click()           #다음페이지 버튼 클릭
    for i in range(3,5):
        driver.find_element_by_xpath('//*[@id="storeList"]/div/div/div[2]/div/a['+str(i)+']').click()    #xpath(31부터 33페이지)
        main(driver.page_source)

crawling_tenpage()
