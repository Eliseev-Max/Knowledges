import json
json_string = """
{
    "ip" : "10.1.32.253",
    "port" : 80,
    "login" : "admin",
    "pass" : "admin",
    "timeout" : "Таймаут в сек"
}
"""
data = json.loads(json_string)
print(f"Результат работы метода loads - объект с типом , {type(data)}\n{data}")
print(data["ip"])
another_json = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
d1 = json.loads(another_json)
d1keys = d1.keys()
print(d1["researcher"])
