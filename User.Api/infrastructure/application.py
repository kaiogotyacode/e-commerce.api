import asyncio
import inspect
from configuration import configuration
    
configuration.load_settings()
env = configuration.get_environment()

import builtins
import importlib

def active(name: str=None, globals=None, locals=None, fromlist=(), level=0):    
    ret = importlib.__import__(name, globals, locals, fromlist, level)
    return ret

builtins.__import__ = active

def start_apis():
    pass
    # Learn how to add Fast API

if __name__ == '__main__':
    start_apis()