# crawling
##최종목표
-
`
원래목표 :    
aws lambda 함수를 사용해 파이썬 코드를 돌리고 CloudWatch Events 트리거를 연결해 cron식으로 하루에 한 번씩 dynamodb로 업로드하기
`
`
수정된목표 : aws ec2(윈도우)에서 하루에 한 번씩 페이지를 크롤링해 얻은 데이터를 aws dynamodb로 전송   
`
`
+boto3(aws sdk for python)로 ec2 인스턴스를 끄고 킬 수 있으면 좋겠다
`
#180626
-
~~~
titles = soup.find_all('div', {'class':'title'})
~~~ 
*find_all* 함수를 사용해서 페이지의 태그값을 읽어왔다.  
~~~
base_url = 'url'  
for n in range (33)   
    url = base_url.format(n+1)   
    webpage = urlopen(url)   
~~~
url에 변수를 두어 for문을 돌릴 때 페이지를 넘기면서 값을 출력했다.   

#180628_location
-
#180626과 같은 내용을 크롤링해오는 거지만 *selenium*을 이용해 크롬으로 긁어왔고  
긁어온 내용을 *csv*와 *json*파일로 저장해 보았다.   

~~~
base_url = 'url'  
for n in range (33)   
    url = base_url.format(n+1)   
    webpage = urlopen(url)   
~~~
*url*을 for문을 돌려서 url 주소로 읽어왔던 전 방식과는 달리   

~~~
for i in range(3):                                                           
    for i in range(3,12):
        driver.find_element_by_xpath(''+str(i)+'').click() 
        main(driver.page_source)
    driver.find_element_by_xpath('').click()           #다음페이지 버튼 클릭
~~~
*xpath*를 이용해 버튼을 넘겨 페이지를 이동했다.
