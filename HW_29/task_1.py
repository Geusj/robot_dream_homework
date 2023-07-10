import random
import http.client

websites = [
    "google.com",
    "facebook.com",
    "twitter.com",
    "amazon.com",
    "apple.com"
]

# Випадково обираємо сайт
random_website = random.choice(websites)

# Виконуємо запит на обраний сайт
conn = http.client.HTTPConnection(random_website)
conn.request("GET", "/")
response = conn.getresponse()

# Виводимо результати
print("Сайт:", random_website)
print("Статус-код:", response.status)
print("Довжина HTML-коду:", len(response.read().decode()))
