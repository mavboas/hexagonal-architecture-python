import os
import yaml
from src.app.utils.dict_to_object import DictToObject


class LoadConfig:
    def __init__(self):
        self.env = os.environ.get('ENV')
        self.file_path = r'./config.yaml'
        self.file_data = self.load_config_file()
        self.parameters = self.load_environment_data()

    def load_config_file(self):
        with open(self.file_path, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data

    def load_environment_data(self):
        object_created = DictToObject(self.file_data)
        if self.env is None:
            raise KeyError(f"CONFIG FILE ERROR: No environment variable with a key name 'ENV' has been configured")
        elif hasattr(object_created, self.env):
            return getattr(object_created, self.env)
        else:
            raise KeyError(f"CONFIG FILE ERROR: '{self.env}' does not exist in the config file")