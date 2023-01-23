## convert json to python dictionary: json.loads

import json

player1 = '{"name": "Ali", "age": 90, "city": "Peshawar"}'

dict = json.loads(player1)

print(dict, dict['name'], type(dict))

## converting Dictionary to json: json.dumps
jsn = json.dumps(dict)
print(jsn, type(jsn))