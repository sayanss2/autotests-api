import json

json_data = """
{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": ["Python", "QA Automation", "API Testing"],
  "address": {
    "city": "Москва",
    "zip": "101000"
  }
}
"""

parsed_data = json.loads(json_data)
print(parsed_data['name'])

data = {
    "name": 'Мария',
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent = 4, ensure_ascii = False)
print(json_string)

with open('json_example.json', 'r', encoding = 'utf-8') as file:
    data_infile = json.load(file)
    print(data_infile)

with open('json_user.json', 'w', encoding = 'utf-8') as file:
    json.dump(data, file,  indent = 2, ensure_ascii = False)