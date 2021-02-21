import sys
import json

# custom imports
from utils import fprint


class Database:

    def __init__(self, fileName):
        self.fileName = fileName

    def getAttribute(self, attr):
        with open(self.fileName) as file:
            data = json.load(file)
            # fprint(data, 'd')
            return data.get(attr, {})


class DinamicDB(Database):

    def __init__(self, fileName):
        super().__init__(fileName)
        fprint('Dinamic DB initialised', 'i')

    def setAttribute(self, attr, value):
        new_data = None
        with open(self.fileName) as file:
            new_data = json.load(file)
        new_data[attr] = value
        with open(self.fileName, 'w') as file:
            json.dump(new_data, file, indent=4, separators=(',', ':'), sort_keys=True, ensure_ascii=False)

class StaticDB(Database):

    def __init__(self, fileName):
        super().__init__(fileName)
        fprint('Static DB initialised', 'i')