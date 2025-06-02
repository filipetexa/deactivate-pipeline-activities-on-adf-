from config import ConfigLoader
import os
import json

# Read configuration
config = ConfigLoader('./config.json')
config = config.get_paths()

path = config[0]['pipelines_path']
type = config[0]['activity_type']
pattern = config[0]['activity_name_pattern']

# Loop with pipeline files
for root, _, files in os.walk(path):
    for pipeline in files:
        pipeline_path = os.path.join(root, pipeline)
        with open(pipeline_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Loop on pipeline activities
        for activity in data.get('properties', {}).get('activities', []):
            if type == activity.get('type') and pattern in activity.get('name', ''):
                activity['state'] = 'Inactive'

        # Salvar o JSON modificado
        with open(pipeline_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
