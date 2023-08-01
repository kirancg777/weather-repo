import requests

# Function to fetch weather data from the API
def fetch_weather_data():
    api_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(api_url)
    return response.json()

# function to get temperature-data
def get_temperature_data(data, date):
    for entry in data['list']:
# if the date of the entry matches the input date
        if entry['dt_txt'].startswith(date):
# extract the temperature data
            temperature_data = entry['main']['temp']
            return temperature_data
# return none if no temperature data is found on date
    return None

# function to get wind speed-data
def get_wind_speed_data(data, date):
    for entry in data['list']:
 # if the date of the entry matches the input date
        if entry['dt_txt'].startswith(date):
# extract the wind speed 
            wind_speed_data = entry['wind']['speed']
            return wind_speed_data
# return one if no wind speed data is found on date
    return None

# function to get pressure-data 
def get_pressure_data(data, date):
    for entry in data['list']:
 # if the date of the entry matches the input date
        if entry['dt_txt'].startswith(date):
 # extract the pressure 
            pressure_data = entry['main']['pressure']
            return pressure_data
 # return None if no pressure data is found for the given date
    return None

def main():
    data = fetch_weather_data()

    while True:
        # input options
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            # exit case
            print("Exiting the program.")
            break
        elif choice == 1:
            # get temp
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature_data(data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} Kelvin")
            else:
                print(f"No temperature data found for {date}.")
        elif choice == 2:
            # get wind speed
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_data(data, date)
            if wind_speed is not None:
                print(f"Wind speed on {date}: {wind_speed} m/s")
            else:
                print(f"No wind speed data found for {date}.")
        elif choice == 3:
            # get pressure
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_data(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print(f"No pressure data found for {date}.")
        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()