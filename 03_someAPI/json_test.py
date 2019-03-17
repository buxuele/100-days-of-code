import json

# basic usage of json
"""
see:
    https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
    
1. To parse a single line(string), use
   json.loads()     # with s
   
2. To parse a file, use json.load():    # without s
    with open('filename.txt', 'r') as handle:
        parsed = json.load(handle)
"""

json_file = '["foo", {"bar":["baz", null, 1.0, 2]}]'    # <class 'str'>
python_obj = json.loads(json_file)  # <class 'list'>

print(json.dumps(python_obj, indent=4, sort_keys=True))













