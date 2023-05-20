from model import Hashmap
import os

for dirpath, dirnames, files in os.walk('./files'):
    for file_name in files:
        path = os.path.abspath(f"./{file_name}")
        print(f"file_name: {file_name}, file path {path}")