from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from collections import OrderedDict
import time

driver=webdriver.Chrome('')      
driver.get('')
now = time.localtime()

def time():
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(s+" 완료")
    
def save_json(data,a):
    with open(a, 'w', encoding="EUC-KR") as make_file:
        json.dump(data, make_file, ensure_ascii=False, indent="\t")

def divide(div,data,output):
    start=0
    end=len(data)                             
    for idx in range(start, end + div, div):
        out=data[start:start + div]
        if out !=[]:
            output.append(out)
        start=start+div

def crawling_list():
    html=driver.page_source
    soup=BeautifulSoup(html, 'html.parser')
    
    group_data=OrderedDict()
    data=[]
    output=[]
    data_all=OrderedDict()
    a=OrderedDict()
    b=[]
    c=OrderedDict()
    count=0

    for name in soup.find_all('p','tit') :
        menu_name=name.get_text()
        menu_name=menu_name.strip()
        if(1<len(menu_name)): 
            nameList=list(menu_name.split('\n'))     
            data.extend(nameList)
            
    for price in soup.find_all('p','p-price02') :
        menu_price=price.get_text()
        menu_price = re.sub(',','', menu_price)
        menu_price = re.sub(r'\\+','', menu_price).strip()
        priceList=list(menu_price.split('\n'))     
        data.extend(priceList)
        count+=1

    divide(count,data,output)
    for i in range(0,count):
        data_all[i]={
            'name':output[0][i],
            'price':output[1][i],
        }
        a[i]=data_all[i]
    
    print("count = {}".format(count))
    b= a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26],a[27],a[28],a[29],a[30],a[31],a[32],a[33],a[34],a[35],a[36],a[37],a[38],a[39],a[40],a[41],a[42],a[43],a[44],a[45],a[46],a[47],a[48],a[49],a[50],a[51],a[52],a[53],a[54],a[55],a[56],a[57],a[58],a[59],a[60],a[61],a[62],a[63],a[64],a[65],a[66],a[67],a[68],a[69],a[70],a[71]
    save_json(b,'_menu.json')
    
crawling_list()
time()
driver.close()
