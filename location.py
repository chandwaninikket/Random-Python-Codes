import requests
import folium
try:
	web_address = "https://ipinfo.io/"
	res=requests.get(web_address)
	print(res)

	data=res.json()
	print(data)

	city_name=data['city']
	print("City name= ", city_name)

	latlong=data['loc']
	lat=latlong.split(",")
	print("Latitude", lat[0])
	print("Longitude",lat[1])

	map=folium.Map(location=[latlong[0],latlong[1]])
	map.save('map1.html')
except Exception as e:
	print("issue ",e)