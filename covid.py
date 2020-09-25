import requests
import bs4
try:
	cname=input("Enter country name")
	web_add="https://www.worldometers.info/coronavirus/country/"+cname
	res=requests.get(web_add)
	print(res)
	data=bs4.BeautifulSoup(res.text,"html.parser")
	info=data.find_all("div",{"class":"maincounter-number"})
	#print(info)
	total_cases=info[0].find('span').text
	death_cases=info[1].find('span').text
	recovered_cases=info[2].find('span').text
	print("Total Cases \n",total_cases)
	print("Death Cases \n",death_cases)
	print("Recovery Cases \n",recovered_cases)
except Exception as e:
	print("issue",e)
