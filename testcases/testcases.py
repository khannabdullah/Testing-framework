# import unittest
# import time

# from selenium import webdriver # type: ignore
# from basepage.Basepage import Basepage_base
# from login_page.login import LoginPage
# from bonded_vpn.vpn_profiles.connections import Connections_01

# class TestLogin(unittest.TestCase):
    
#     def setUp(self):    
#         self.driver = webdriver.Chrome() 
#         self.driver.maximize_window() 
            
#             # Initialize the page objects here
#         self.login_page = LoginPage(self.driver)
#         self.bond = Connections_01(self.driver)

#     def test_login(self):
    
#     #   Access the json data separately
#         base_page = Basepage_base(self.driver)
#         login_data = base_page.test_data_login['login']
#         site_data = base_page.test_data_server['site']

#         self.login_page.open(
#             login_data[0]['url']
            
#         )

#         self.login_page.login(
#             login_data[0]['username'],
#             login_data[0]['password']
#         )
#         time.sleep(2)

#         # Call the site_to_site_server method with the data from the JSON file
#         self.bond.site_to_site_server(
#             site_data[0]['profile_name']
#         )


# if __name__ == "__main__":
#     unittest.main()  

import unittest
import time
from selenium import webdriver
from basepage.Basepage import Basepage_base
from login_page.login import LoginPage
from bonded_vpn.vpn_profiles.connections import Connections_01
from bonded_vpn.vpn_profiles.logs import logs_tab
from bonded_vpn.vpn_profiles.bulk_configurations import bulk_configuration

class TestLogin(unittest.TestCase):
    
    def setUp(self):    
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_page = Basepage_base(self.driver)
        self.login_page = LoginPage(self.driver)
        self.bond = Connections_01(self.driver)
        self.logs = logs_tab(self.driver)
        self.bulk = bulk_configuration(self.driver)

    def test_login(self):   
        login_data = self.base_page.test_data_login['login']
        site_server_data = self.base_page.test_data_server['site_server']
        site_client_data = self.base_page.test_data_server['site_to_site_client']
        multisite_server = self.base_page.test_data_server['site_to_multisite_server']
        multisite_client = self.base_page.test_data_server['site_to_multisite_client']
        bulk_config = self.base_page.test_data_bulk['bulk_configurations']

        self.login_page.open(login_data['url'])
        self.login_page.login(login_data['username'], login_data['password'])

        self.bond.open_connection()

        self.bond.site_to_site_server(site_server_data)
                
        time.sleep(2)
        self.base_page.delete_connection()

        time.sleep(2)

        self.bond.site_to_site_client(site_client_data)

        time.sleep(2)

        self.base_page.delete_connection()

        time.sleep(2)

        self.bond.site_to_multisite_server(multisite_server)
        
        time.sleep(2)

        self.bond.site_to_multisite_client(multisite_client)

        # time.sleep(2)
        # self.logs.logs()
        # time.sleep(2)

        # self.bulk.bulk_config(

        #     bulk_config['profile_name'],
        #     bulk_config['listening_port'],
        #     bulk_config['no_of_clients'],
        #     bulk_config['starting_network_id'],
        #     bulk_config['tunnel_mtu']
        # )
        

    def tearDown(self):
        try:
            self.driver.quit()
        except PermissionError:
            print(" Warning: Could not terminate the driver due to permission issues.")

if __name__ == "__main__":
    unittest.main()
