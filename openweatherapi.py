import requests, json
#import mysql.connector

api_key = '801cd15e7a38441c42871603e1902469'

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = "Halifax"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url) 

x = response.json() 

if x["cod"] != "404": 
    y = x["main"] 
   
    # store the value corresponding 
    # to the "temp" key of y 
    current_temperature = y["temp"] 
   
    # store the value corresponding 
    # to the "pressure" key of y 
    current_pressure = y["pressure"] 
   
    # store the value corresponding 
    # to the "humidity" key of y 
    current_humidiy = y["humidity"] 
     
    # current_humidiy = y["wind"]  
    # store the value of "weather" 
    # key in variable z 
    z = x["weather"] 
   
    # store the value corresponding  
    # to the "description" key at  
    # the 0th index of z 
    weather_description = z[0]["description"] 
   
    w = x["wind"]

    json_string = json.dumps(w)
    wx = json.loads(json_string)['speed'] * 1.609344
    # print following values 
    print(" Temperature (in Celsius unit) = " +
                   str(current_temperature - 273.15) + 
          "\n atmospheric pressure (in hPa unit) = " +
                     str(current_pressure) +
           "\n humidity (in percentage) = " +
                     str(current_humidiy) +
           "\n description = " +
                    str(weather_description) + 
           "\n Wind = " +
                         str(wx))

else: 
    print(" City Not Found ") 
