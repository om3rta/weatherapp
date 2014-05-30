#imports
import pycurl
import cStringIO
import json
import os

#get_input asks user for zip code/city
def get_input():
	city = ""
	city = raw_input(["enter a zip code, or enter 'exit' to exit"])
	city = city.lower()
	return city

#make_url constructs a URL based on the user input
def make_url(city):
	url_front = "http://api.wunderground.com/api/3ff15933e8683503/conditions/q/"
	url_city = city
	url_end = ".json"
	url_full = url_front + city + url_end
	return url_full

#get_weather uses the contructed URL from make_url to request information from the wunderground API
def get_weather(new_url):
	buf = cStringIO.StringIO()
	c = pycurl.Curl()
	c.setopt(c.URL, new_url)
	c.setopt(c.WRITEFUNCTION, buf.write)
	c.perform()
	weather_info = buf.getvalue()
	buf.close()
	return weather_info

#organize_weather parses the information gathered by get_weather and organizes it into a dictionary
def organize_weather(forecast):
	weather_parsed = json.loads(forecast)
	return weather_parsed

#weather_report gathers information from the dictionary created in organize_weather and prints it
def weather_report():
	report = ""
	print "\nCurrent weather report for " + forecast_json['current_observation']['display_location']['city'] + ", " + forecast_json['current_observation']['display_location']['state'] + ":\n\n"
	print "Condition: " + forecast_json['current_observation']['weather']
	print "Temperature: " + forecast_json['current_observation']['temperature_string']
	print "Feels like: " + forecast_json['current_observation']['feelslike_string']
	return report

#main program. Prompt user for input. Gather weather information from specified location.
#screen clears every time the program starts, or when a new report is done. Reports can be repeated until the user chooses to 'exit'.
city = None
os.system('cls' if os.name == 'nt' else 'clear')
while city != "exit":
	city = get_input()
	if city != "exit":
		os.system('cls' if os.name == 'nt' else 'clear')
		new_url = make_url(city)
		forecast = get_weather(new_url)
		forecast_json = organize_weather(forecast)
		if 'response' in forecast_json:
			if 'error' in forecast_json["response"]:
				print "You did not provide a valid zip address or city, please try again."
			else:
				report = weather_report()
				print report