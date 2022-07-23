import json

with open('1.json', 'r') as file:
    content = file.read()
    for i in range(1,201):
        clean = content.replace('][', str(i))  
        json_data = json.loads(clean)
        with open(f'data{i}.json', 'w') as f:
            json.dump(json_data, f)


