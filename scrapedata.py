import urllib2
z=0
url1='http://www.thehindu.com/archive/print/'

for i in range(2012,2017):
	yearurl = url1+str(i)+"/"
	for j in range(01, 13):
		monthurl =yearurl+str(j)+"/"
		for k in range(01,11):
			dayurl=monthurl+str(k)+"/"
			print (dayurl+"#FrontPage")
			z+=1
			print(z)
			url=urllib2.urlopen(dayurl+'#FrontPage')
			page=url.read()
			from bs4 import BeautifulSoup
			f=open('projectoutput1.txt','a')
			for ul in BeautifulSoup(page).find_all('ul',{'class':'archive-list'}):
				for a in ul.find_all('a'):
					out=a.text.encode('utf-8')
					f.write(out +'\n')
			f.close()



		





