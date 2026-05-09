import yaml
import os

class ConfigReader:

    def __init__(self, env="qa"):
        self.env = env.lower()
        self.config_data = self._load_config()

    def _load_config(self):
        file_path = os.path.join(os.path.dirname(__file__), "config.yaml")

        with open(file_path, "r") as file:
            data = yaml.safe_load(file)

        if self.env not in data:
            raise Exception(f"Environment '{self.env}' not found in config")

        return data[self.env]

    def get(self, key):
        return self.config_data.get(key)