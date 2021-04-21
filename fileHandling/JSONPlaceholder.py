#-*- coding: utf-8 -*-
"""Воспользуемся источником фейковых данных JSON - JSONPlaceholder - для оттачивания навыков работы с JSON.
URL ресурса: https://jsonplaceholder.typicode.com/todos"""
import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(type(todos))
print(todos[:2])
print(type(todos[0]))
