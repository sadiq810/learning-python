# Read json file and convert
import json

# f = open("player.json", "r")
# txt = f.read()
# jsn = json.loads(txt)

with open("player.json") as f:
    jsn = json.load(f)

print(jsn, type(jsn), jsn['name'])