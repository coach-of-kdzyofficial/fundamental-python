user = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    }
}
print(user)
print(user["id"])
print(user["name"])
print(user["username"])
print(user["email"])
print(user["address"]["street"])
print(user["address"]["geo"]["lat"])
print(user["address"]["geo"]["lng"])

print(user)
print(type(user))

print('\nUbah disc ke JSON')
import json
result = json.dumps(user)
print(type(result))
print(result)

#with open('result.json', 'w') as file :
#   json.dumb(user, file)

