import json
import logging


class ConfigProvider:
    # No constructor because this class only submits actions.

    @staticmethod
    def load_from_file(filename):
        try:  # With opening files always we use -try-.
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"File {filename} not found. Starting with an empty library.")
