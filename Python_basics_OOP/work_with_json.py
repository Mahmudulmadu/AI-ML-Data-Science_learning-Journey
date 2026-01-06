import json

####  json string to Pyhton dictionary

# json_str = '{"name": "mahmudul", "isTeacher":true}'
# py_obj = json.loads(json_str)
# print(type(py_obj))


### Python obj to json str

# py_obj = {
#     "name" : "Mahmudul",
#     "isTeacher": None
# }
# json_str = json.dumps(py_obj)
# print(type(json_str))



### Json data from file to python object

# with open("data.json", "r") as f:
#     py_obj  = json.load(f)
#     print(py_obj)


#### Python dict data json data in file

py_obj = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

with open("Json_data.json","w+") as f:
    json.dump(py_obj, f, indent=4, sort_keys=True)
    