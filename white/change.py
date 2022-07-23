import json

with open('data.json', 'r') as file:
    content = file.read()
    for i in range(801, 1001):
        clean = content.replace('][', str(i))  
        json_data = json.loads(clean)
        with open(f'data{i}.json', 'w') as f:
            json.dump(json_data, f)
