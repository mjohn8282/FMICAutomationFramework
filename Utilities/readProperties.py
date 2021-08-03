import configparser
import pytest


class Readconfi:

    def __init__(self, intialiseconfigfile):
        self.config = intialiseconfigfile

    def getbaseurl(self):
        url = self.config.get('login', 'baseurl')
        return url

    def getfirefoxdriverlocation(self):
        location = self.config.get('driverlocation', 'firefox')
        return location

    def getedgedriverlocation(self):
        location = self.config.get('driverlocation', 'edge')
        return location

    def gettestfilelocation(self):
        location = self.config.get('Testdata', 'testdatafilelocation')
        return location

    def getchromedriverlocation(self):
        # location = self.confi.get("driverlocation", "chrome")
        # return location
        return "D:\\John\\PythonProject\\POM\\Drivers\\chromedriver.exe"

    def getpassword(self):
        password = self.config.get('login', 'password')
        return password

    def getuseremail(self):
        useremail = self.config.get('login', 'useremail')
        return useremail
