from datetime import datetime
import json
import sys
import os

def loadJsonData(fileName):
    jsonFile = open(fileName, "r")
    data = json.load(jsonFile)
    jsonFile.close()
    return data

def datePrinter():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def filePathMerger(relativePath):
    try:
        filePath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + relativePath.replace('\\', '/')
        print "[DEBUG] " + datePrinter() + " Your system platform is: " + sys.platform
        assert os.path.isfile(filePath)
        print "[DEBUG] " + datePrinter() + " File \'" + relativePath + "\' found!"
        return filePath
    except IOError:
        print "[ERROR] " + datePrinter() + " File: \'" +os.path.dirname(os.path.dirname(os.path.realpath(__file__)))\
              + relativePath + "\' not found! Please verify again."
    else:
        filePath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + relativePath.replace('/', '\\')
        print "[DEBUG] " + datePrinter() + " Your system platform is: " + sys.platform
        assert os.path.isfile(filePath)
        print "[DEBUG] " + datePrinter() + " File \'" + relativePath + "\' found!"
        return filePath

