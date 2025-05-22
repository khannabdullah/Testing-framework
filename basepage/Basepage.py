# import os
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
# # from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By # type: ignore
from selenium import webdriver # type: ignore
# import json
# # import re
# # import time
    
# class Basepage_base:
   
#     def load_json(self, filename):
#         # Construct the full path to the JSON file
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         json_path = os.path.join(base_dir, filename)
        
#         # Open and load the JSON data from the file
#         with open(json_path) as json_file:
#             return json.load(json_file)
        
#     def __init__(self, driver):
#         # call JSON files
#         self.driver = driver
#         self.test_data_login = self.load_json('Login.json')
#         self.test_data_server = self.load_json('site_server.json')

import os
import json

class Basepage_base:
    def __init__(self, driver):
        self.driver = driver
        self.test_data_login = self.load_json('Authentications.json')
        self.test_data_server = self.load_json('Connections.json')  # unified JSON
        self.test_data_bulk = self.load_json('bulk_config.json')

    def load_json(self, filename):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, filename)
        with open(json_path) as json_file:
            return json.load(json_file)
        

    def delete_connection(self):
        wait = WebDriverWait(self.driver, 10)
        delete_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[2]/table/tbody/tr[1]/td[13]/button[1]')))
        delete_button.click()
        confirm_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')))
        confirm_button.click()
        
