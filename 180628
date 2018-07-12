from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = '........page={}...... '
 
for n in range (33) :
    url = base_url.format(n+1)
    webpage = urlopen(url)
    soup = BeautifulSoup(webpage, 'html5lib')
    
    titles = soup.find_all('div', {'class':'title'})
    nums = soup.find_all('div', {'class':'num'})
    names=soup.find_all('div',{'id':'storeName'})

    for name in names :
        a=name.get_text()
        print(a)
