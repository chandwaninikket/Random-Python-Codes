import requests
try:
	moviename=input("enter movie name to find ")
	a1="http://www.omdbapi.com/?"
	a2="&s="+moviename
	a3="&apikey=" +"2aeb4bd3"
	webaddress=a1+a2+a3
	res=requests.get(webaddress)
	data=res.json()
	print(data)
	info=data['Search']
	count=0
	for i in info:
		print("*" * 30)
		mn=i['Title']
		yr=i['Year']
		po=i['Poster']
		print("Movie name is ", mn)
		print("Release Year is ",yr)
		image_address=po
		res=requests.get(image_address)
		poster=mn +".jpg"
		f=open(poster,"wb")
		f.write(res.content)
		f.close()
except Exception as e:
	print("Error is",e)