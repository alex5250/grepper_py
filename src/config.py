import configparser
import sys

from logger import  setup_logger
logger = setup_logger(__name__)

class Config():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read("/etc/grepper.py/config.ini")
        if len(self.config.sections()) >= 1:
            logger.debug(f"Config file check: passed. Config contains:{self.config.sections()}")
        else:
            logger.debug(f"Config file check: failed. Config contains:{self.config.sections()}")
            print("Do you had installed an config file?")
            sys.exit(0)

    def get_value_from_config(self,selection,value):
        value=self.config.get(selection,value)
        if value=="":
            print("something wrong with config.ini file. check it")
            sys.exit(0)
        else:
            return value
    def set_value_from_config(self,selection,value,set_value):
        self.config.set(selection,value,set_value)
        with open('/etc/grepper.py/config.ini', 'w') as configfile:
            self.config.write(configfile)           
    pass

