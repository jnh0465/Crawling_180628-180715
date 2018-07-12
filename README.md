# crawling
-
#180626
-
`
titles = soup.find_all('div', {'class':'title'})
`<br/>
*find_all* 함수를 사용해서 페이지의 태그값을 읽어왔다.<br/>

`
base_url = 'url'
for n in range (33) 
    url = base_url.format(n+1)
    webpage = urlopen(url)
`<br/>
url에 변수를 두어 for문을 돌릴 때 페이지를 넘기면서 값을 출력했다.<br/>

-
#180628_location
-
#180626과 같은 내용을 크롤링해오는 거지만 *selenium*을 이용해 크롬으로 긁어왔고 긁어온 내용을 *csv*와 *json*파일로 저장해 보았다.<br/>
또 url을 for문을 돌려서 읽어왔던 전 방식과는 달리

`
for i in range(3):                                                           
    for i in range(3,12):
        driver.find_element_by_xpath(''+str(i)+'').click() 
        main(driver.page_source)
    driver.find_element_by_xpath('').click()           #다음페이지 버튼 클릭
`
