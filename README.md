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

`
희망사항 :
`   
+boto3(aws sdk for python) 혹은 CloudWatch Events로 ec2 인스턴스를 끄고 킬 수 있으면 좋겠다

___
#180626
-
`
친하지 않았던 개발자도구와 친해졌고 평소 접하던 웹사이트가 하나하나 태그로 이루어져있고 공개되어 있어서`   
`쉽게 읽어올 수 있다는 것이 신기했다.`  
`또한, 파이썬으로 처음짜본 코드라 이게 맞나 아닌가? 헷갈리면서도 신기했다.`  

~~~python
titles = soup.find_all('div', {'class':'title'})
~~~ 
`*find_all* 함수를 사용해서 페이지의 태그값을 읽어왔다. `    
~~~python
base_url = 'url'  
for n in range (33)   
    url = base_url.format(n+1)   
    webpage = urlopen(url)   
~~~
`*url*에 변수를 두어 for문을 돌릴 때 페이지를 넘기면서 값을 출력했다. `     
___
#180628_location
-
`beautifulsoup으로 읽어올 수 없었던 사이트가 seleniume을 통해 창이 뜨면서(!) 동적으로 긁어올 수 있는게 신기했고,`   
`selector값이 아닌 xpath값으로 클릭하고 다음페이지로 이동할 수 있다는 것이 신기했다.`   
`또, 처음 접하는 json파일이 너무 생소했다.`   
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
`#180626과 같은 내용을 크롤링해오는 거지만 *selenium*을 이용해 크롬으로 긁어왔고`     
`긁어온 내용을 *csv*와 *json*파일로 저장해 보았다.`      
   
~~~python
base_url = 'url'  
for n in range (33)   
    url = base_url.format(n+1)   
    webpage = urlopen(url)   
~~~
`*url*을 for문을 돌려서 url 주소로 읽어왔던 전 방식과는 달리`     
   
~~~python
for i in range(3):                                                           
    for i in range(3,12):
        driver.find_element_by_xpath(''+str(i)+'').click() 
        main(driver.page_source)
    driver.find_element_by_xpath('').click()           #다음페이지 버튼 클릭
~~~
`*xpath*를 이용해 버튼을 눌러 페이지를 이동했다.`   

~~~json
{										#180628_location json
	"name+address+tel": [
		[
			"ㅇㅇ역",
			"서울특별시 ㅇㅇ구 ㅇㅇ로 ㅇㅇ빌딩",
			"02-1234-1234"
		]
	]
}{									
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
`페이지 이동과 json의 param을 값을 함수로 만들어 좀 더 보기 좋게 코드를 만들었다`   
`구글에서 json파일 저장형식 'a'(추가)와 'w'(갱신)의 차이를 알게 되었다.`   
`나중에 시기별로 자동적으로 갱신시키고 싶어 'w'를 너무 쓰고 싶었으나,`   
`'w'를 사용하면 페이지가 계속 넘어가면서 맨 마지막 페이지 데이터만 저장되어 일단 'a'로 저장했다.`   

~~~python
def save_json(group_data):
    with open('.json', 'a', encoding="EUC-KR") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")
~~~
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
`함수인자로 버튼의 xpath값과 json파일에 사용될 param값을 입력받아서 json을 만들어 보았다.`    

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
___
#180701_ingredient #실패
-

`7월1일까지 약 7~8여개의 페이지를 크롤링하려고 시도했었는데`   
`각 페이지 사정상 버튼의 xpath의 값이 달라 입력이 안되는 경우도 있었고,`     
`페이지가 asp이어서 위치나 메뉴의 페이지가 바뀌는데 정작 크롤링한 데이터는 1페이지에 멈춰있는 경우도 많았다.`      
`또 크롤링을 했다고 하더라도 json에 익숙하지 않다보니 형식을 어떻게 해야할지 감을 잡지 못했다.`   

~~~json
{										#180701_ingredient json
	"sandwich_ingredients": [
		[
			"스파이시 ",
			[
				"ㅇㅇㅇㅇ 5장"
			],
			[
				"ㅇㅇㅇ 5장"
			],
			[
				"ㅁㅁ 2장"
			],
			[
				"ㅇㅇㅇ 1스쿱"
			]
		]
	]
}{
	"sandwich_ingredients": [
		[
			"베지",
			[
				"각종 야채"
			]
		]
	]
}
~~~
___
#180703 #실패 #생각바꾸기
-
`크롤링이 재밌어 하염없이 빠져있던 중에, 팀 멘토님과의 만남이 있었고 가장 중요한 걸 까먹고 있다는 것을 깨달았다.`    
`바로 '가격'이었다. `    
`중간목표가 데이터를 db에 옮기고 결제까지 연결하는 것이라 핵심이 메뉴이름과 가격인데,`    
`나는 위치나 성분같은 부수적인것을 크롤링하는데 빠져있었다.`   
`다만, 대부분의 프랜차이즈 사이트들이 가격을 웹페이지에 올리지 않아 무슨 프랜차이즈를 골라야 할지 고민이 많았다.`
~~~
맥ㅇㅇ드 - 가격안나옴
맘스ㅇㅇ - 가격안나옴
버거ㅇ - 가격안나옴
서ㅇㅇ이 - 가격안나옴
할ㅇ스 - 가격안나옴
스타ㅇㅇ - 가격안나옴
탐앤ㅇㅇ - 가격안나옴
이ㅇ야 - 가격안나옴
커피ㅇ - 가격안나옴
카ㅇㅇ네 - 가격안나옴
엔젤ㅇㅇㅇ - 가격안나옴
요거ㅇㅇ소  - 가격안나옴
봉구ㅇㅇㅇ거 - 나오는데 반은 jpg임
파ㅇㅇ찌 - 나오는데 팝업형태라 못읽음
~~~   
___
#180704_menu&price
-
`하나의 for문으로 모든 데이터를 읽어오지 못하는 경우가 생겼다.`     
`여러개의 for문으로 각각 읽어오자니 출력형식이 메뉴만 주루룩 가격만 주루룩 나오게 되었다.`   
`처음에는 divide 함수로 div를 1로 해서 하나씩 자르고 붙여주는 것을 생각했는데,`   
`태그로 완벽하게 읽히지 않아 re.sub이나 글자수로 잘라주어야 하는 것까지 나누어지는 경우가 생겨서`   
`태그가 제대로 읽히는 for함수에 count값을 붙여주어서 count을 div해서 나눠주고`   
`배열로 메뉴하나 가격하나 붙여주어 json으로 출력하는 것을 만들었다`

~~~python
def divide(div,data,output):
    start=0
    end=len(data)                             
    for idx in range(start, end + div, div):
        out=data[start:start + div]
        if out !=[]:
            output.append(out)
        start=start+div
~~~   
~~~python
 divide(count,data,output)
 for i in range(0,count):
    data_all.extend([output[0][i], output[1][i]])
 divide(2,data_all,data_all_output)
 group_data[params]=data_all_output
 save_json(group_data)
~~~   
~~~json
{										#180704_menu&price json
	"coffee&drink": [
		[
			"에이드",
			"6,000"
		],
		[
			"레몬 에이드",
			"6,500"
		],
		[
			"수박주스",
			"5,500"
		],
		[
			"라떼",
			"6,000"
		]
	]
}
~~~
___
#180708_create/deletetable
-
`aws cli configure 설정과 리전만 잘 입력해 두면`       
`dynamodb.create_table함수와 table.delete()함수로 이루어진 몇 줄 안되는 코드로`    
`dynamodb에 테이블이 생성되고 삭제되는게 너무 신기했다.`    
~~~python
import boto3
dynamodb = boto3.resource('dynamodb',region_name='ap-northeast-1')
~~~
___
#180709_loadtable/crawling       180709~180711
-
`올 것이 오고야 말았다. `    
`'json'`   
    
Link: [Amazon DynamoDB][awslink]
[awslink]: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.02.html "loadtable&json"
    
~~~json
[										#dynamodb에서 요구하는 json
   {
      "year" : ... ,
      "title" : ... ,
      "info" : { ... }
   },
   {
      "year" : ...,
      "title" : ...,
      "info" : { ... }
   },

    ...
]
~~~   
`위의 json형식으로 load할 수 있다고 aws 개발자 안내서에 나와있다. 하지만 내가 만든 json형식은 아래의 json이다.`      
~~~json
{										#180704_menu&price json
	"coffee&drink": [
		[
			"에이드",
			"6,000"
		],
		[
			"레몬 에이드",
			"6,500"
		],
		[
			"수박주스",
			"5,500"
		],
		[
			"라떼",
			"6,000"
		]
	]
}
~~~
`param값이야 지정해 준다고 쳐도 '{'와 '['의 차이는 대체 어떻게 바꾸어주어야 할지 감도 잡히지 않았다.`   
`re.sub으로 {을 [라고 바꿔주는 꼼수도 써볼까 했지만 역시 통하지 않았다.`    
___
~~~python
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
~~~
   
`결국 내가 이용한 코드는 위의 코드`  
`json값은 아래와 같이 나온다.`   
~~~json
[
	{
		"name": " 에이드",
		"price": "6000"
	},
	{
		"name": "레몬 에이드",
		"price": "6500"
	},
	{
		"name": "수박주스",
		"price": "5500"
	},
	{
		"name": " 라떼",
		"price": "6000"
	}
]
~~~
    
___   
`count값으로 나눠주고 count만큼 이름과 가격을 묶어준다는 것은 지난번 파이썬 파일과 같다.`   
`문제는 저 수많은 a[0],a[1]...a[71] 들인데,`   
`for문을 돌려 a[i]를 입력해주는 좋은 방법이 있을것같아 여러방법으로 시도했지만,`    
~~~python
for i in range(0,count):
        data_all={
            'name':output[0][i],
            'price':output[1][i],
        }
        a=data_all
 save_json(a,'twosome_menu.json')
~~~
`결과는`   
~~~json
{
	"name": "에스프레소 싱글",
	"price": "3300"
}
~~~
`이런 식으로 맨 마지막 것만 출력되거나,`   
~~~json
{
	"name",
	"price",
	"name",
	"price",
	"name",
	"price",
	"name",
	"price"
}
~~~
`이런 식으로 name과 price만 나오는 사태가 벌어졌다.` 
`일단 급한건 db저장이니 다른 팀원을 위해 잠시 접어두기로 한다.`    
___
+왜 됨?? 
`180713 00:20 read.me 작성도중 애매하게 json이 되는 것을 발견했다. 좀 더 고쳐 봐야 겠다.`    
~~~python
    divide(count,data,output)
    for i in range(0,count):
        data_all[i]={
            'name':output[0][i],
            'price':output[1][i],
        }
        a[i]=data_all[i]
    save_json(a,'twosome_menu.json')
~~~
~~~json
{
	"0": {
		"name": " 에이드",
		"price": "6000"
	},
	"1": {
		"name": "레몬 에이드",
		"price": "6500"
	},
	"2": {
		"name": "수박주스",
		"price": "5500"
	},
	"3": {
		"name": " 라떼",
		"price": "6000"
	}
}
~~~
