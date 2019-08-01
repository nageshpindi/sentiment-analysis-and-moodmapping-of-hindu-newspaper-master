import urllib2
from random import randrange
z=0
yearurl=""
monthurl=""
dayurl=""
dayarray=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
url1='http://www.thehindu.com/archive/print/'

for i in range(2012,2017):
	yearurl = url1+str(i)+"/"
	for j in range(01, 13):
		monthurl =yearurl+str(j)+"/"
		for k in range(1,11):
			dayurl=monthurl+str(randrange(0,len(dayarray)))+"/"
			url=urllib2.urlopen(dayurl+'#FrontPage')
			page=url.read()
			from bs4 import BeautifulSoup
			f=open('testmain.txt','a')
			for ul in BeautifulSoup(page).find_all('ul',{'class':'archive-list'}):
				for a in ul.find_all('a'):
					out=a.text.encode('utf-8')
					f.write(out +'\n')
			f.close()



		





