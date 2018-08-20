from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from collections import OrderedDict
import time

driver=webdriver.Chrome('C:\Program Files (x86)\Python37-32/chromedriver.exe')        #selenium
driver.get('')
now = time.localtime()

def time():
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print(s+" load")
    
def save_json(data,a):
    with open(a, 'w', encoding="UTF-8") as make_file:
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
    countnum=1
    
    for name in soup.find_all('p','tit') :
        two_name=name.get_text()
        two_name=re.sub(' ','', two_name)
        two_name=two_name.strip()
        if(1<len(two_name)): 
            nameList=list(two_name.split('\n'))     
            data.extend(nameList)
            
    for price in soup.find_all('p','p-price02') :
        two_price=price.get_text()
        two_price = re.sub(',','', two_price)
        two_price = re.sub(r'\\+','', two_price).strip()
        priceList=list(two_price.split('\n'))     
        data.extend(priceList)
        count+=1

    img_names = soup.find_all('img')
    for img in img_names:
        two_img=str(img['src'])
        two_img = re.sub('/img/common/quick_membershipcard.gif','', two_img)

        if(34<len(two_img)<37):
            two_img=two_img.strip()
            urlList=list(two_img.split('\n'))     
            data.extend(urlList)
            
    divide(count,data,output)
    for i in range(0,count):
        data_all[i]={
            'num':countnum,
            'kname':output[0][i],
            'ename':'a',
            'price':output[1][i],
            'url':'https://www.:7009'+output[2][i]
        }
        countnum+=1
        a[i]=data_all[i]
    
    print("count = {}".format(count))
    b= a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14],a[15],a[16],a[17],a[18],a[19],a[20],a[21],a[22],a[23],a[24],a[25],a[26],a[27],a[28],a[29],a[30],a[31],a[32],a[33],a[34],a[35],a[36],a[37],a[38],a[39],a[40],a[41],a[42],a[43],a[44],a[45],a[46],a[47],a[48],a[49],a[50],a[51],a[52],a[53],a[54],a[55],a[56],a[57],a[58],a[59],a[60],a[61],a[62],a[63],a[64],a[65],a[66],a[67],a[68],a[69],a[70],a[71],a[72],a[73]
    save_json(b,'two_menu.json')
    
crawling_list()
time()
driver.quit()
