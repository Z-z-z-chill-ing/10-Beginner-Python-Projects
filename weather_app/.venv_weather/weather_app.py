import requests, os
from dotenv import load_dotenv
from prettytable import PrettyTable
load_dotenv()

keyAPI = os.getenv("API_KEY")

def display_data(data, forecastDay):
    if (forecastDay):
        for day in range(0, int(forecastDay)):
            """Location Data"""
            country = data.get("location").get("country")
            region = data.get("location").get("name")
            latitude = data.get("location").get("lat")
            longitude = data.get("location").get("lon")
            localtime = data.get("location").get("localtime")
            """Current Weather Conditions"""
            currentWeatherDescription = data.get("current").get("condition").get("text")
            currentCelsius = data.get("current").get("temp_c")
            currentFahrenheit = data.get("current").get("temp_f")
            humidity = data.get("current").get("humidity")
            windSpeedMph = data.get("current").get("wind_mph")
            windSpeedKph = data.get("current").get("wind_kph")
            windDirection = data.get("current").get("wind_dir")
            precipitationMm = data.get("current").get("precip_mm")
            precipitationIn = data.get("current").get("precip_in")
            uvIndex = data.get("current").get("uv")
            visibilityKm = data.get("current").get("vis_km")
            visibilityMl = data.get("current").get("vis_miles")
            """Forecast"""
            forecast = data.get("forecast").get("forecastday")[day]
            forecast_date = forecast.get("date")
            forecast_date_epoch = forecast.get("date_epoch")
            # Daytime weather conditions
            max_temp_c = forecast.get("day").get("maxtemp_c")
            max_temp_f = forecast.get("day").get("maxtemp_f")
            min_temp_c = forecast.get("day").get("mintemp_c")
            min_temp_f = forecast.get("day").get("mintemp_f")
            avg_temp_c = forecast.get("day").get("avgtemp_c")
            avg_temp_f = forecast.get("day").get("avgtemp_f")
            max_wind_mph = forecast.get("day").get("maxwind_mph")
            max_wind_kph = forecast.get("day").get("maxwind_kph")
            total_precip_mm = forecast.get("day").get("totalprecip_mm")
            total_precip_in = forecast.get("day").get("totalprecip_in")
            avg_visibility_km = forecast.get("day").get("avgvis_km")
            avg_visibility_miles = forecast.get("day").get("avgvis_miles")
            avg_humidity = forecast.get("day").get("avghumidity")
            uv_index = forecast.get("day").get("uv")
            # Day condition
            day_condition_text = forecast.get("day").get("condition").get("text")
            day_condition_icon = forecast.get("day").get("condition").get("icon")
            day_condition_code = forecast.get("day").get("condition").get("code")
            # Astro data
            sunrise_time = forecast.get("astro").get("sunrise")
            sunset_time = forecast.get("astro").get("sunset")
            moonrise_time = forecast.get("astro").get("moonrise")
            moonset_time = forecast.get("astro").get("moonset")
            moon_phase = forecast.get("astro").get("moon_phase")
            moon_illumination = forecast.get("astro").get("moon_illumination")
            is_moon_up = forecast.get("astro").get("is_moon_up")
            is_sun_up = forecast.get("astro").get("is_sun_up")
            # Create a PrettyTable instance
            table = PrettyTable()
            # Add columns to the table
            table.field_names = [f"Category Day {day + 1}", "Value"]
            # Add rows for Location Data
            table.add_row(["Country", country])
            table.add_row(["Region", region])
            table.add_row(["Latitude", latitude])
            table.add_row(["Longitude", longitude])
            table.add_row(["Local Time", localtime])
            # Add a separator between sections
            table.add_row(["", ""])
            # Add rows for Current Weather Conditions
            table.add_row(["Current Weather Description", currentWeatherDescription])
            table.add_row(["Current Temperature (Celsius)", currentCelsius])
            table.add_row(["Current Temperature (Fahrenheit)", currentFahrenheit])
            table.add_row(["Humidity", humidity])
            table.add_row(["Wind Speed (mph)", windSpeedMph])
            table.add_row(["Wind Speed (kph)", windSpeedKph])
            table.add_row(["Wind Direction", windDirection])
            table.add_row(["Precipitation (mm)", precipitationMm])
            table.add_row(["Precipitation (in)", precipitationIn])
            table.add_row(["UV Index", uvIndex])
            table.add_row(["Visibility (km)", visibilityKm])
            table.add_row(["Visibility (miles)", visibilityMl])
            # Add a separator between sections
            table.add_row(["", ""])
            # Add rows for Forecast Data
            table.add_row(["Forecast Date", forecast_date])
            table.add_row(["Max Temperature (Celsius)", max_temp_c])
            table.add_row(["Max Temperature (Fahrenheit)", max_temp_f])
            table.add_row(["Min Temperature (Celsius)", min_temp_c])
            table.add_row(["Min Temperature (Fahrenheit)", min_temp_f])
            table.add_row(["Average Temperature (Celsius)", avg_temp_c])
            table.add_row(["Average Temperature (Fahrenheit)", avg_temp_f])
            table.add_row(["Max Wind Speed (mph)", max_wind_mph])
            table.add_row(["Max Wind Speed (kph)", max_wind_kph])
            table.add_row(["Total Precipitation (mm)", total_precip_mm])
            table.add_row(["Total Precipitation (in)", total_precip_in])
            table.add_row(["Average Visibility (km)", avg_visibility_km])
            table.add_row(["Average Visibility (miles)", avg_visibility_miles])
            table.add_row(["Average Humidity", avg_humidity])
            table.add_row(["UV Index", uv_index])
            # Add a separator between sections
            table.add_row(["", ""])
            # Add rows for Day Condition
            table.add_row(["Day Condition", day_condition_text])
            # Add a separator between sections
            table.add_row(["", ""])
            # Add rows for Astro Data
            table.add_row(["Sunrise Time", sunrise_time])
            table.add_row(["Sunset Time", sunset_time])
            table.add_row(["Moonrise Time", moonrise_time])
            table.add_row(["Moonset Time", moonset_time])
            table.add_row(["Moon Phase", moon_phase])
            table.add_row(["Moon Illumination", moon_illumination])
            table.add_row(["Is Moon Up?", is_moon_up])
            table.add_row(["Is Sun Up?", is_sun_up])
            # Print the table
            print(table)
    else:
            """Location Data"""
            country = data.get("location").get("country")
            region = data.get("location").get("name")
            latitude = data.get("location").get("lat")
            longitude = data.get("location").get("lon")
            localtime = data.get("location").get("localtime")
            """Current Weather Conditions"""
            currentWeatherDescription = data.get("current").get("condition").get("text")
            currentCelsius = data.get("current").get("temp_c")
            currentFahrenheit = data.get("current").get("temp_f")
            humidity = data.get("current").get("humidity")
            windSpeedMph = data.get("current").get("wind_mph")
            windSpeedKph = data.get("current").get("wind_kph")
            windDirection = data.get("current").get("wind_dir")
            precipitationMm = data.get("current").get("precip_mm")
            precipitationIn = data.get("current").get("precip_in")
            uvIndex = data.get("current").get("uv")
            visibilityKm = data.get("current").get("vis_km")
            visibilityMl = data.get("current").get("vis_miles")
            # Create a PrettyTable instance
            table = PrettyTable()
            # Add columns to the table
            table.field_names = [f"Category Day 1", "Value"]
            # Add rows for Location Data
            table.add_row(["Country", country])
            table.add_row(["Region", region])
            table.add_row(["Latitude", latitude])
            table.add_row(["Longitude", longitude])
            table.add_row(["Local Time", localtime])
            # Add a separator between sections
            table.add_row(["", ""])
            # Add rows for Current Weather Conditions
            table.add_row(["Current Weather Description", currentWeatherDescription])
            table.add_row(["Current Temperature (Celsius)", currentCelsius])
            table.add_row(["Current Temperature (Fahrenheit)", currentFahrenheit])
            table.add_row(["Humidity", humidity])
            table.add_row(["Wind Speed (mph)", windSpeedMph])
            table.add_row(["Wind Speed (kph)", windSpeedKph])
            table.add_row(["Wind Direction", windDirection])
            table.add_row(["Precipitation (mm)", precipitationMm])
            table.add_row(["Precipitation (in)", precipitationIn])
            table.add_row(["UV Index", uvIndex])
            table.add_row(["Visibility (km)", visibilityKm])
            table.add_row(["Visibility (miles)", visibilityMl])
            # Print the table
            print(table)

def get_default_location():
    try:
        response = requests.get('http://ip-api.com/json')
        if (not response.status_code == 200):
            raise requests.ConnectionError(f"Status Code({response.status_code}) couldn't get a location.")
        data = response.json()
        country = data.get("country")
        region = data.get("regionName")
        return country, region
    except (Exception, requests.ConnectionError) as e:
        print(f"Error Occurred: {e}")
        return None

def get_request(country, region, forecast):
    try:
        if (country and region and forecast):
            API = f"http://api.weatherapi.com/v1/forecast.json?key={keyAPI}&q={country},{region}&days={forecast}&aqi=no&alerts=no"
        elif (country and region and not forecast):
            API = f"http://api.weatherapi.com/v1/current.json?key={keyAPI}&q={country},{region}&aqi=yes"
        elif (country and forecast and not region):
            API = f"http://api.weatherapi.com/v1/forecast.json?key={keyAPI}&q={country}&days={forecast}&aqi=no&alerts=no"
        elif (country and not region and not forecast):
            API = f"http://api.weatherapi.com/v1/current.json?key={keyAPI}&q={country}&aqi=yes"
        else:
            print("Country should not be empty.")
            return None
        response = requests.get(API)
        if (not response.status_code == 200):
            raise requests.ConnectionError(f"Status Code({response.status_code}) couldn't get a location.")
        data = response.json()
        return data
    except (Exception, requests.ConnectionError) as e:
        print(f"Error Occurred: {e}")
        return None

def main():
    choice = input("Enter the country manually/or use default country[m/d]: ")
    if (choice.lower() == "m" and choice):
        country = input("Enter a country to get a weather: ")
        region = input("Enter a region to get a weather(optional): ")
        forecast = input("How many days of forecast do you need[1-14days](optional): ")
        data = get_request(country, region, forecast)
        display_data(data, forecast)
    elif (choice.lower() == "d" and choice):
        forecast = input("How many days of forecast do you need[1-14days](optional): ")
        country, region = get_default_location()
        data = get_request(country, region, forecast)
        display_data(data, forecast)
    else:
        print("\nYou should enter m or d to choose whether you wish to enter info manually or use your default location.\n")
        main()

if __name__ == "__main__":
    main()