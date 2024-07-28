import json


class ConfigProvider:

    @staticmethod
    def load_from_file(filename):
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")