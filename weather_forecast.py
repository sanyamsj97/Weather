import requests
import json

def fetch_weather_forecast(city):
    api_key = "df981908f780c2b1a9d4f5f881d7e303"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    try:
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"  # Units can be "metric" or "imperial"
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        weather_data = json.loads(response.text)

        # Extract relevant weather information from the API response
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        weather_desc = weather_data["weather"][0]["description"]

        # Display the weather forecast
        print(f"Weather Forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
        print(f"Weather Description: {weather_desc}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting to the API: {conn_err}")
    except KeyError:
        print("Invalid response from the API. Please try again.")
    except Exception as err:
        print(f"An error occurred: {err}")

# Prompt the user for a city name and fetch the weather forecast
city_name = input("Enter the name of a city: ")
fetch_weather_forecast(city_name)
