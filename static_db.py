from utils import fprint
import json


class StaticDB:

    def __init__(self, fileName):
        self.fileName = fileName
        fprint('Static DB initialised', 'i')

    def getAttribute(self, attr):
        with open(self.fileName) as file:
            data = json.load(file)
            return data.get(attr, {})