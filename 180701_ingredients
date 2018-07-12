from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import pandas as pd
from selenium import webdriver
from collections import OrderedDict

driver = webdriver.Chrome('')    
driver.get('')

def save_csv(output):
    df = pd.DataFrame(output)
    df.to_csv(".csv", mode='a', header=False, index=False, encoding='euc-kr')
    
def save_json(group_data):
    with open('.json', 'a', encoding="EUC-KR") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")
        
def crawling(names,ingredients,data):
    for name in names :
        menu_name = name.get_text().strip()
        menu_name = re.sub('\n+'," ", menu_name)
        menu_name = re.sub('\t+'," ", menu_name).strip()
                     
        nameList=menu_name.split('\n')                                        #메뉴이름 nameList
        data.extend(nameList)

    for ingredient in ingredients :
        menu_ingredient = ingredient.get_text().strip()
        menu_ingredient = re.sub('\n+'," ", menu_ingredient).strip()

        if(len(menu_ingredient)<11):    
            ingredientList=list(menu_ingredient.split('\n'))                  #성분 ingredientList
            data.extend([ingredientList])
    
def crawling_list(html,params):
    html=driver.page_source
    soup = BeautifulSoup(html, 'html5lib')
    
    names = soup.select('div div.hd h2')
    ingredients = soup.select('div.recipe ul li')
    group_data = OrderedDict()
    data = []
    output = []
    
    crawling(names,ingredients,data)
    output.append(data)
    
    group_data[params]=output
    print(json.dumps(group_data, ensure_ascii=False, indent="\t") )
    #save_csv(output)
    save_json(group_data)

def crawling_sendwich():
    params="sandwich_ingredients"
    for i in range(1,21):
        driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/ul/li['+str(i)+']/a').click()
        crawling_list(driver.page_source,params)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[6]/div/a').click()
        
    i=21                                                    #왠진 모르지만 21번째만 연결 xpath가 다름  **a[2]
    driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/ul/li['+str(i)+']/a[2]').click()
    crawling_list(driver.page_source,params)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[6]/div/a').click()
   
    for i in range(22,29):
        driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/ul/li['+str(i)+']/a').click()
        crawling_list(driver.page_source,params)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[6]/div/a').click()

def crawling_salad():
    params="salad_ingredients"
    for i in range(1,24):
        driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/ul/li['+str(i)+']/a').click()
        crawling_list(driver.page_source,params)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[6]/div/a').click()

        
crawling_sendwich()
driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/ul/li[2]/a').click()
crawling_salad()
