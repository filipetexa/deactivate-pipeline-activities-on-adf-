import json
import os

class ConfigLoader:
    def __init__(self, config_path='./config.json'):
        self.config_path = config_path
        self.config = self.load_json(self.config_path)

    @staticmethod
    def load_json(file_path):
        """Carrega um arquivo JSON e retorna um dicionário."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"O arquivo especificado não foi encontrado: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_paths(self):
        """Retorna a lista de caminhos de diretórios e seus tipos a partir do arquivo de configuração."""
        return self.config