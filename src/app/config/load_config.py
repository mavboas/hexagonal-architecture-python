import os
import yaml
from src.app.utils.dict_to_object import DictToObject
from src.app.config.log_config import logger


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class LoadConfig(metaclass=Singleton):
    def __init__(self, file_path=None):
        self.env = os.environ.get('ENV')
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = r'config.yaml'
        logger(f"CONFIG FILE PATH: {self.file_path}", level=20)
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
