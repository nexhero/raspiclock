import yaml
import os
import sys

class raspiclock:
    def __init__(self):
        self.path = os.path.dirname(__file__) + "/"
        rf = self.path + "raspiclock.yaml"
        try:
            stream = file(rf, "r")
            self.data = yaml.load(stream)
        except Exception as e:
            print e
            system.exit("Raspiclock Error File")

    #return module list
    def ModulesList(self):
        return self.data['modules']

    #Return keys values from config key
    def getConfig(self, key):
        try:
            value = self.data['config'][key]
        except Exception as e:
            print e
            sys.exit( "Error to acces " + key + " value")
        return value
