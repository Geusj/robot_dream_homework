import threading
import requests
import multiprocessing
import time

cities = [
    {"city": "Esbjerg", "latitude": 55.47, "longitude": 8.45},
    {"city": "Copenhagen", "latitude": 55.68, "longitude": 12.57},
    {"city": "New York", "latitude": 40.71, "longitude": -74.01},
    {"city": "Venice", "latitude": 45.44, "longitude": 12.33},
    {"city": "Tonder", "latitude": 54.93, "longitude": 8.84}
]


def get_weather(city):
    latitude = city["latitude"]
    longitude = city["longitude"]
    resp = requests.get(
        url="https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m"
        }
    )
    if resp.status_code == 200:
        data = resp.json()
        if "hourly" in data and "temperature_2m" in data["hourly"] and len(data["hourly"]["temperature_2m"]) > 0:
            temperature = data['hourly']['temperature_2m'][0]
            return temperature


def thread_only():
    start_time = time.time()
    threads = []
    for city in cities:
        thread = threading.Thread(target=get_weather, args=(city,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    end_time = time.time()
    return end_time - start_time


def multi_process():
    start_time = time.time()
    processes = []

    for city in cities:
        process = multiprocessing.Process(target=get_weather, args=(city,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":
    # time for single-threaded method
    temperatures = []
    start_time = time.time()
    for city in cities:
        temperature = get_weather(city)
        if temperature is not None:
            temperatures.append(temperature)
            print(f"Temperature in {city['city']}: {temperature}°C")
    if len(temperatures) > 0:
        avg_temperature = sum(temperatures) / len(temperatures)
        print(f"Average temperature: {avg_temperature}°C")
        hottest_city = None
        hottest_temperature = float('-inf')
        for city in cities:
            temperature = get_weather(city)
            if temperature is not None and temperature > hottest_temperature:
                hottest_city = city
                hottest_temperature = temperature
        if hottest_city is not None:
            print(f"{hottest_city['city']} is the hottest city with {hottest_temperature}°C")
    end_time = time.time()
    print(f"Single-threaded execution time: {end_time - start_time:.4f} seconds")

    # time for multi-threaded method
    thread_time = thread_only()
    print(f"Multi-threaded execution time: {thread_time:.4f} seconds")

    # time for multi-process method
    process_time = multi_process()
    print(f"Multi-process execution time: {process_time:.4f} seconds")
