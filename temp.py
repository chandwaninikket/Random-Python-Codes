import requests

try:
	cityname=input("Enter your cityname ")
	a1="https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q=" + cityname
	a3="&appid=c6e315d09197cec231495138183954bd"
	web_address=a1+a2+a3
	res=requests.get(web_address)
	#print(res)
	data=res.json()
	#print(data)
	temp=data['main']['temp']
	print("Temperature of ",cityname, "is ",round(temp))

except Exception as e:
	print("Issue ",e)
