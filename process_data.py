import json


with open('Raw_data.json','r') as data_pulled_from_json_file:
    data = json.loads(data_pulled_from_json_file)