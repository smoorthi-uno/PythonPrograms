#!/usr/bin/env python3

# Swetha Moorthi
# ISQA 3900 - November 05, 2020
# A Python program to find current weather details of any city using openweathermap API

# import modules
from datetime import datetime
import requests
import pytemperature


def main():
    now = datetime.now().strftime("%A, %B %d, %Y")
    print("ISQA 3900 Open Weather API")
    print(now)
    print()

    choice = "y"
    while choice == "y":
        # user prompt for city name
        city = input("Enter city:       ")

        # user prompt for country name
        print("Use ISO letter country code like: https://countrycode.org/")
        country = input("Enter country code: ")

        # variable to store api url
        api_start = 'https://api.openweathermap.org/data/2.5/weather?q='

        # variable to store API key
        api_key = '&appid=8a23774f1b6574da61b9de4d1673b958'

        # complete url address
        url = api_start + city + ',' + country + api_key

        # get method of requests module returns the response object
        # json method of response object converts json format data into python format data
        json_data = requests.get(url).json()

        try:
            if json_data['cod'] != "404":
                # if city is found
                weather_description = json_data['weather'][0]['description']
                current_temperature = round(pytemperature.k2f(json_data['main']['temp']), 2)
                current_pressure = json_data['main']['pressure']
                current_humidity = json_data['main']['humidity']
                low_temperature = pytemperature.k2f(json_data['main']['temp_min'])
                high_temperature = pytemperature.k2f(json_data['main']['temp_max'])

                print("Current Conditions: ", weather_description)
                print("Current Temperature in Fahrenheit: ", current_temperature)  # using round method
                print("Current Pressure in hpa: ", current_pressure)
                print("Current Humidity: {}%".format(current_humidity))
                print("Expected Low Temperature in Fahrenheit: {:.2f}".format(low_temperature))  # using string format()
                print(
                    "Expected High Temperature in Fahrenheit: {:.2f}".format(high_temperature))  # using string format()

            else:
                # city not found
                print("\tUnable to access " + city + " in " + country)
                print("\tVerify city name and country code")
        except:
            print("\tUnable to access " + city + " in " + country)
            print("\tVerify city name and country code")

        choice = input("Continue (y/n)?: ")
        print()
    print("Bye!")


# if started as the main module, call the main() function
if __name__ == "__main__":
    main()