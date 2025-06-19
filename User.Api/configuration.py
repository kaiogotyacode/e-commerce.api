import sys
import asyncio
import os
import configparser
import warnings

warnings.filterwarnings("ignore")

class configuration:

    settings: configparser.ConfigParser = None

    @staticmethod
    def get_environment(env:str = "CURRENT_ENVIRONMENT"):
        return os.getenv(env, None)
        
    @staticmethod
    def set_environment(env:str, value: str):
        os.environ[env] = value

    @staticmethod
    def get_environment_value(env:str = "CURRENT_ENVIRONMENT"):
        return os.environ[env]

    @staticmethod
    def load_settings():
        file:str = None
        if configuration.get_environment() is not None:
            file = 'settings.' + configuration.get_environment_value() + '.ini'
        else:
            file = 'settings.ini'

        configuration.settings = configparser.ConfigParser()
        configuration.settings._interpolation = configparser.ExtendedInterpolation()
        configuration.settings.read(os.path.join(os.getcwd(), file), encoding='utf-8-sig')
        configuration.settings.sections()

    @staticmethod
    def get_settings(section: str, key: str) -> str:
        if configuration.settings is None:
            configuration.load_settings()
            
        if configuration.settings.has_section(section) and configuration.settings.has_option(section, key):
            return configuration.settings.get(section, key)
        else:
            return None