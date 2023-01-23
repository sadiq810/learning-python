## converting python object to json
import json

print( json.dumps({"name": "Ali", "age": 34}) ) # Dictionary to json
print( json.dumps(["Ali", "Wali", "Jan"]) ) # List to json
print( json.dumps(("Ali", "Wali", "Jan")) ) # tuple to json
print( json.dumps("Hi, there") ) # string to json
print( json.dumps(234) ) # integer to json
print( json.dumps(234.345) ) # float to json
print( json.dumps(True) ) # Boolean to json => true
print( json.dumps(False) ) # false
print( json.dumps(None) ) # null