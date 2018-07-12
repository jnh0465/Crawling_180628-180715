# crawling
___
##최종목표
-
`
원래목표 :     
`    
aws lambda 함수를 사용해 파이썬 코드를 zip으로 올리고    
CloudWatch Events 트리거를 연결해 cron식으로 하루에 한 번씩 dynamodb로 업로드하기
   
`
수정된목표 : 
`   
- [x] crawling_name.py를 실행해 얻은 데이터를 json파일로 저장   
- [x] boto3(aws sdk for python)를 import해 dynamodb에 테이블 생성, 로드, 삭제, 검색하는 코드 만들기
- [ ] aws ec2(윈도우)에서 하루에 한 번씩 페이지를 크롤링해 얻은 데이터를 aws dynamodb로 전송  

+boto3(aws sdk for python) 혹은 CloudWatch Events로 ec2 인스턴스를 끄고 킬 수 있으면 좋겠다
`    

___
#180626
-
~~~python
titles = soup.find_all('div', {'class':'title'})
~~~ 
*find_all* 함수를 사용해서 페이지의 태그값을 읽어왔다.  
~~~python
base_url = 'url'  
for n in range (33)   
    url = base_url.format(n+1)   
    webpage = urlopen(url)   
~~~
*url*에 변수를 두어 for문을 돌릴 때 페이지를 넘기면서 값을 출력했다.   
___
#180628_location
-
~~~python
driver = webdriver.Chrome('')        #selenium
driver.get('')
~~~   
~~~python
def save_csv(output):
    dataframe = pd.DataFrame(output)
    dataframe.to_csv(".csv", mode='a', header=False, index=False, encoding='euc-kr')
    
def save_json(group_data):
    with open('.json', 'a', encoding="EUC-KR") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")
~~~
#180626과 같은 내용을 크롤링해오는 거지만 *selenium*을 이용해 크롬으로 긁어왔고  
긁어온 내용을 *csv*와 *json*파일로 저장해 보았다.   
   
~~~python
base_url = 'url'  
for n in range (33)   
    url = base_url.format(n+1)   
    webpage = urlopen(url)   
~~~
*url*을 for문을 돌려서 url 주소로 읽어왔던 전 방식과는 달리   
   
~~~python
for i in range(3):                                                           
    for i in range(3,12):
        driver.find_element_by_xpath(''+str(i)+'').click() 
        main(driver.page_source)
    driver.find_element_by_xpath('').click()           #다음페이지 버튼 클릭
~~~
*xpath*를 이용해 버튼을 눌러 페이지를 이동했다.

~~~json
{										#180628_location json
	"name+address+tel": [
		[
			"ㅇㅇ역",
			"서울특별시 ㅇㅇ구 ㅇㅇ로 ㅇㅇ빌딩",
			"02-1234-1234"
		]
	]
}
~~~   
___
#180629_menu
-
~~~python
def crawing_page(i,params):
    driver.find_element_by_xpath('//*[@id="container"]/div[1]/div/div/ul/li['+str(i)+']/a').click()
    params=params
    crawling_list(driver.page_source,params)
~~~
~~~python
group_data[params]=output
save_json(group_data)
~~~
~~~python
crawing_page(1,"dd-menu")
crawing_page(2,"salad_menu")
crawing_page(3,"")
crawing_page(4,"")
crawing_page(5,"")
crawing_page(6,"")
~~~
함수인자로 버튼의 xpath값과 json파일에 사용될 param값을 입력받아서 json을 만들어 보았다.

~~~json
{										#180629_menu json
	"sandwich_menu": [
		[
			"스파이시 ddddd"
		],
		[
			"터키 dddd"
		]
	]
}{
	"salad_menu": [
		[
			""
		],
		[
			""
		]
	]
}
~~~
