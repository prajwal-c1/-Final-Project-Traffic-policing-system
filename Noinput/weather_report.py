# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 
import datetime




def weather(city):
	now = datetime.datetime.now()
	days = ["Monday","Tuesday","Wednesday","Thusday","Friday","Saturday","Sunday"]
	day = datetime.datetime.today().weekday()
	print (" Current date and time : ",now.strftime("%Y-%m-%d %H:%M:%S"))
	print(" Day :",days[day])
	api_key = "9e32b2857f2216509b5a975066378392"


	base_url = "http://api.openweathermap.org/data/2.5/weather?" 
	city_name = city
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

	response = requests.get(complete_url) 

	x = response.json() 
	


	if x["cod"] != "404": 

	 
		y = x["main"] 
		 
		current_temperature = y["temp"]  
		current_pressure = y["pressure"] 
		current_humidiy = y["humidity"] 
		z = x["weather"] 
		weather_description = z[0]["description"] 
		print(" Visibility :",x["visibility"],"Meter")
		
		# print following values 
		print(" Temperature (in kelvin unit) = " +
						str(current_temperature) +
			"\n atmospheric pressure (in hPa unit) = " +
						str(current_pressure) +
			"\n humidity (in percentage) = " +
						str(current_humidiy) +
			"\n description = " +
						str(weather_description)) 
		print(" Estimated time : 195 sec ")

	else: 
		print(" City Not Found ") 
