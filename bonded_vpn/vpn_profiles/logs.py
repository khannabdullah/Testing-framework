from basepage.Basepage import Basepage_base
from utils.ValidationEngine import ValidationEngine

from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
import time

class logs_tab(Basepage_base):
    def logs(self):
        wait = WebDriverWait(self.driver, 10)

        logs_tab_click = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[8]/section/div/ul/li[2]/a')))
        logs_tab_click.click()

        select_profile = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/div/div/select')))
        select_profile = Select(select_profile)
        select_profile.select_by_index(1)
        time.sleep(2)
        select_profile = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/div/div/select')))
        select_profile = Select(select_profile)
        select_profile.select_by_index(1)
