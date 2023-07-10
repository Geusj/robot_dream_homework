import requests
def get_coordinates(city):
    url = f"https://api.open-meteo.com/v1/geocode?query={city}"
    response = requests.get(url)
    data = response.json()
    if "latitude" in data and "longitude" in data:
        return data["latitude"], data["longitude"]
    return None, None
def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    if "current_weather" in data:
        return data["current_weather"]
    return None
def main():
    city = input("Введіть назву міста: ")
    latitude, longitude = get_coordinates(city)
    if latitude is not None and longitude is not None:
        weather = get_weather(latitude, longitude)
        if weather is not None:
            print(f"Погода в місті {city}:")
            print("Температура:", weather["temperature"])
            print("Вологість:", weather["humidity"])
            print("Стан неба:", weather["skytext"])
        else:
            print("Не вдалося отримати погоду для заданого міста.")
    else:
        print("Не вдалося знайти координати для заданого міста.")



if __name__ == "__main__":
    main()
