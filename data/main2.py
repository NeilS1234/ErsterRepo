import json

user = {
    "name": "John Doe",
    "age": 30
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

{
    "name": "Max",
    "age": 20
}

import json

data = '{"name": "Max", "age": 20}'

user = json.loads(data)

print(user["name"])
