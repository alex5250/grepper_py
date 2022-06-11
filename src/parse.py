from selenium import webdriver
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from logger import  setup_logger
logger = setup_logger(__name__)
import time


class Parse_From_web():
    def __init__(self):
        chromedriver_autoinstaller.install() 
        logger.warning("Installing chromedriver to system and adding it to path.")
    pass

    def make_search(self,title,language,suffix,element_id):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(chrome_options=options)
        url_ready=(f"{suffix}{title} {language}")
        logger.info(f"User reqested to open url:{url_ready}")
        driver.get(url_ready)
        elem = driver.find_elements(By.CLASS_NAME, element_id)
        response={}
        answer_counter=0
        for answers in elem:
            response[answer_counter]=answers.text
            answer_counter=answer_counter+1
        return_value=('url',url_ready,'responses',response)
        return return_value

    pass

    def pretty_Print(self,output):
        print(f"Parsed from: {output[1]}")
        solutions=output[3]
        for a in range(0,len(solutions)):
            print(f"Solution {a}:")
            print(solutions.get(a))
    pass