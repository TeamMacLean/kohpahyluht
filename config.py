import ConfigParser
import os


def get_config():
    config = ConfigParser.ConfigParser()
    path_to_config = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini')
    config.read(path_to_config)
    return config
