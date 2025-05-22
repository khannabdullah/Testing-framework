from basepage.Basepage import Basepage_base
from utils.ValidationEngine import ValidationEngine
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
import time

class bulk_configuration(Basepage_base):
    
    def bulk_config(self, profile_name, listening_port, no_of_clients, starting_network_id, tunnel_mtu):
        wait = WebDriverWait(self.driver, 10)
        ve = ValidationEngine()

        time.sleep(2)

        # FORM VALIDATION (before interacting with UI)
        ve.is_not_empty("Profile Name", profile_name)
        ve.is_within_range("No of Clients", no_of_clients, 1, 500)
        ve.is_within_range("Listening Port", listening_port, 1, 65535)
        ve.is_valid_ip("Tunnel Network Subnet", starting_network_id)
        ve.is_within_range("Tunnel Mtu", tunnel_mtu, 1, 150000)
        

        # Click on the "Bulk Configuration" tabno_of_clients
        bulk_config_tab = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[8]/section/div/ul/li[6]/a')))
        bulk_config_tab.click()

        create_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[8]/section/div/div/div[1]/div[2]/button')))
        create_button.click()

        profile_name_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
        ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")
        # time.sleep(2)

        no_of_clients_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/input')))
        ve.validate_and_fill(no_of_clients_input, no_of_clients, "No of Clients")
        # time.sleep(2)

        status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/span[3]')))
        status.click()
        # time.sleep(2)

        protocol = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[4]/div[2]/select')))
        protocol = Select(protocol)
        protocol.select_by_index(1) 
        # time.sleep(2)

        performance = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[5]/div[2]/div/div/div/span[3]')))
        performance.click()
        # time.sleep(2)

        encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
        encryption_algo = Select(encryption_algo)
        encryption_algo.select_by_index(1)
        # time.sleep(2)

        listening_port_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: port"]')))
        ve.validate_and_fill(listening_port_input, listening_port, "Listening Port")
        # time.sleep(2)

        starting_network_id = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[2]/input')))
        starting_network_id.clear()
        ve.validate_and_fill(starting_network_id, "Starting Network ID", "Starting Network ID")
        # time.sleep(2)

        tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
        tunnel_mtu_input.clear()
        ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")

        time.sleep(2)
        # Click on the "Create" button
        form_create = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[3]/div/button[1]')))
        form_create.click()
        time.sleep(2)