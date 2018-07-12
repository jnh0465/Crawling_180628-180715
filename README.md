# crawling
-
#180626
-
`
titles = soup.find_all('div', {'class':'title'})
`<br/>
*find_all* 함수를 사용해서 페이지의 태그값을 읽어왔다.<br/>

`
base_url = 'url'\n
for n in range (33) :
    url = base_url.format(n+1)
    webpage = urlopen(url)
`<br/>
url에 변수를 두어 for문을 돌릴 때 페이지를 넘기면서 값을 출력했다.<br/>
