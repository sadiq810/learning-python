### Python pretty print JSON dumps

import json

player1 = '{"name": "Wali","age": 78,"languages": ["English", "Pushto"],"city": "Peshawar"}'

dict = json.loads(player1)
pretty = json.dumps(dict, indent = 4, sort_keys = True)
print(pretty, type(pretty))