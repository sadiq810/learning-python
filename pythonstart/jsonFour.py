# writing json file
import json

player1 = {
  "name": "Wali",
  "age": 78,
  "languages": ["English", "Pushto"],
  "city": "Peshawar"
}

# Open file in write mode
with open("playerOne.json", "w") as json_file:
    json.dump(player1, json_file)