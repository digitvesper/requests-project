import requests
import pprint

# запрос json
# params = {
#     'userId' : 1
# }
# response = requests.get(" https://jsonplaceholder.typicode.com/posts", params=params)
# response_json = response.json()
# pprint.pprint(response_json)


# загрузка изображения
# img = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Tesla-optimus-bot-gen-2-scaled_%28cropped%29.jpg/411px-Tesla-optimus-bot-gen-2-scaled_%28cropped%29.jpg"
# response = requests.get(img)
#
# with open("test.jpg", "wb") as file:
#     file.write(response.content)

# состав ответа
# response = requests.get("https://api.github.com")
# print(response.status_code)
# response_json = response.json()
# print(response.headers)
# pprint.pprint(response_json)



# задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.

url = "https://jsonplaceholder.typicode.com/posts"
#Создаем словарь в котором будет храниться информация для отправки:

data = {
    "title": 'foo',
    "body": 'bar',
    "userId": 1
}

response = requests.post(url, data=data)
print(response.status_code)
print(f"ответ - {response.json()}")
