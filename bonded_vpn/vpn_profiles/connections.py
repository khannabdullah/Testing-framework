# from basepage.Basepage import Basepage_base
# from utils.ValidationEngine import ValidationEngine

# from selenium import webdriver # type: ignore
# from selenium.webdriver.common.by import By # type: ignore
# from selenium.webdriver.support.ui import WebDriverWait # type: ignore
# from selenium.webdriver.support import expected_conditions as EC # type: ignore
# from selenium.webdriver.support.ui import Select # type: ignore
# import time


# class Connections_01(Basepage_base):

#     def open_connection(self):
#         wait = WebDriverWait(self.driver, 10)

#         tcp_bondedvpn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/aside[2]/div/div[4]/div/div/nav/ul/li[9]/a')))
#         tcp_bondedvpn.click()

#         vpn_profiles = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/aside[2]/div/div[4]/div/div/nav/ul/li[9]/ul/li[1]/a')))
#         vpn_profiles.click()

#     def site_to_site_server(self, profile_name, routes_list, multiple_routes, listening_port, tunnel_local_ip, tunnel_remote_ip, tunnel_mtu, tx_queue, keepalive_timeout, socket_send_buffer_size, socket_receive_buffer_size, tunnel_timeout):  #l_port, list_port, local_ip, remote_ip, send_buffer, receive_buffer, tunnel_timeout
       
#         wait = WebDriverWait(self.driver, 10)
#         ve = ValidationEngine()
#         time.sleep(2)

#         # FORM VALIDATION (before interacting with UI)
         

#     # FORM VALIDATION (before interacting with UI)
#         ve.is_not_empty("Profile Name", profile_name)
        
#         ve.is_valid_routes_list("Routes List", routes_list)
#         ve.is_within_range("Listening Port", listening_port, 1, 65535)
#         ve.is_valid_ip("Tunnel Local IP", tunnel_local_ip)
#         ve.is_valid_ip("Tunnel Remote IP", tunnel_remote_ip)
#         ve.is_within_range("Tunnel MTU", tunnel_mtu, 576, 15000)  # RFC 791 MTU guidance
#         ve.is_within_range("TX Queue Length", tx_queue, 1, 10000)
#         ve.is_within_range("Keepalive Timeout", keepalive_timeout, 1, 3600)
#         ve.is_within_range("Send Buffer Size", socket_send_buffer_size, 1, 100000)
#         ve.is_within_range("Receive Buffer Size", socket_receive_buffer_size, 1, 100000)
#         ve.is_within_range("Tunnel Timeout", tunnel_timeout, 1, 3600)

#         ve.validate_or_throw()

#         # Click on the "TCP Bonded VPN and VPN Profiles" 

#         select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
#         select = Select(select_element)
#         select.select_by_index(1) 
#         time.sleep(2)

#         # Click on the "Create" button  
#         create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
#         create_button.click()
#         time.sleep(4)
        
#         # Fill in the form fields (Site to Site Server):  
#         # Fill in the "Profile Name" field
#         profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
#         ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")

#         routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))
#         ve.validate_and_fill(routing_list, routes_list, "Routes List")

#         route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
#         route_add.click()

#         # time.sleep(2)
#         # multiple_routes_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[2]/a')))
#         # multiple_routes_add.click()
#         # bulk_route_ips = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[3]/textarea')))
#         # bulk_route_ips.send_keys(multiple_routes)
#         # time.sleep(2)
#         # add_bulk_ips = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[3]/button')))
#         # add_bulk_ips.click()
#         # routes_ok_box = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/button[1]')))
#         # routes_ok_box.click()
#         # time.sleep(2)
#         # select_element_protocol = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[1]/div[2]/select')))
#         # select = Select(select_element_protocol)
#         # select.select_by_index(0)

#         self.driver.execute_script("window.scrollTo(0, 200);")        
#         listening_port_01 = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="1 - 65535"]')))
#         listening_port_01.click()
#         listening_port_01.send_keys(listening_port)

#         # time.sleep(2)
#         tunnel_Local_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="0.0.0.0"]')))
#         tunnel_Local_input.click()
#         tunnel_Local_input.send_keys(tunnel_local_ip)
#         # time.sleep(2)

#         tunnel_remot_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: route_gateway"]')))
#         tunnel_remot_input.click()
#         tunnel_remot_input.send_keys(tunnel_remote_ip)
#         # time.sleep(2)

#         tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
#         ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")

#         encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
#         encryption_algo = Select(encryption_algo)
#         encryption_algo.select_by_index(1) 
#         # time.sleep(2)

#         compression = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[11]/div[2]/div/div/div/label[2]')))
#         compression.click()
#         # time.sleep(2)

#         self.driver.execute_script("window.scrollTo(0, 200);") 
#         tx_que_length = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
#         tx_que_length.click()
#         tx_que_length.clear()
#         tx_que_length.send_keys(tx_queue)

#         keep_alive = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
#         keep_alive.click()
#         keep_alive.clear()
#         keep_alive.send_keys(keepalive_timeout)

#         send_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: sndbuf"]')))
#         send_buffer.click()
#         send_buffer.clear()
#         send_buffer.send_keys(socket_send_buffer_size)

#         receive_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: rcvbuf"]')))
#         receive_buffer.click()
#         receive_buffer.clear()
#         receive_buffer.send_keys(socket_receive_buffer_size)

#         tunnel_timeout_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: inactive"]')))
#         tunnel_timeout_input.click()
#         tunnel_timeout_input.clear()
#         tunnel_timeout_input.send_keys(tunnel_timeout)

#         status_version_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[33]/div[2]/select')))
#         status_version_input = Select(status_version_input)
#         status_version_input.select_by_index(0)

#         form_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
#         form_create.click()
        
#         time.sleep(2)

#     def site_to_site_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, multiple_routes, listening_port, tunnel_local_ip, tunnel_remote_ip, tunnel_mtu, route_delay, tx_queue, keepalive_timeout, socket_send_buffer_size, socket_receive_buffer_size, tunnel_timeout):
#         wait = WebDriverWait(self.driver, 10)
#         ve = ValidationEngine()

#         time.sleep(2)

#         # FORM VALIDATION (before interacting with UI)
#         ve.is_not_empty("Profile Name", profile_name)
#         ve.is_valid_routes_list("Routes List", routes_list)
#         ve.is_valid_ip("Remote Server IP", remote_server_ip)
#         ve.is_valid_port("Remote Server Port", remote_server_port)
#         ve.is_within_range("Listening Port", listening_port, 1, 65535)
#         ve.is_within_range("Tunnel MTU", tunnel_mtu, 1, 150000)
#         ve.is_within_range("Route Delay", route_delay, 0, 3600)
#         ve.is_within_range("TX Queue Length", tx_queue, 1, 1000)
#         ve.is_within_range("Keepalive Timeout", keepalive_timeout, 1, 3600)
#         ve.is_within_range("Socket Send Buffer Size", socket_send_buffer_size, 1, 1048576)
#         ve.is_within_range("Socket Receive Buffer Size", socket_receive_buffer_size, 1, 1048576)
#         ve.is_within_range("Tunnel Timeout", tunnel_timeout, 1, 3600)

#         # Stop if validation fails
#         ve.validate_or_throw()

#         # UI Interaction begins
#         select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
#         select = Select(select_element)
#         select.select_by_index(2)  # Adjusted from 3 to 2 based on original code
#         time.sleep(2)

#         # Click on the "Create" button  
#         create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
#         create_button.click()
#         time.sleep(2)

#         # Profile Name
#         profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
#         ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")

#         # Status
#         status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/label[2]')))
#         status.click()

#         # Configuration Mode
#         configuration_mode = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/label[2]')))
#         configuration_mode.click()

#         # Routing List
#         routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))       
#         ve.validate_and_fill(routing_list, routes_list, "Routes List")

#         # Route Add List
#         route_add_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
#         route_add_list.click()

#         # Remote Server IP
#         remote_server_ip_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_ip"]')))
#         ve.validate_and_fill(remote_server_ip_input, remote_server_ip, "Remote Server IP")

#         # Remote Server Port
#         remote_server_port_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_port"]')))
#         ve.validate_and_fill(remote_server_port_input, remote_server_port, "Remote Server Port")

#         # Add Route
#         route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[5]/div[2]/div[2]/div/div/a')))
#         route_add.click()

#         # Tunnel Local IP
#         tunnel_local_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="0.0.0.0"]')))
#         ve.validate_and_fill(tunnel_local_input, tunnel_local_ip, "Tunnel Local IP")

#         # Tunnel Remote IP
#         tunnel_remote_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: route_gateway"]')))
#         ve.validate_and_fill(tunnel_remote_input, tunnel_remote_ip, "Tunnel Remote IP")

#         # Tunnel MTU
#         tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
#         ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")

#         # Encryption Algorithm
#         encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
#         Select(encryption_algo).select_by_index(1)

#         # Compression
#         compression = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[11]/div[2]/div/div/div/label[2]')))
#         compression.click()

#         # Initial Traffic Interfaces
#         initial_traffic_interfaces = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "options: ifaces")]')))
#         Select(initial_traffic_interfaces).select_by_index(1)

#         # Route Delay
#         route_delay_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: route_delay"]')))
#         ve.validate_and_fill(route_delay_input, route_delay, "Route Delay")
#         time.sleep(2)

#         # TX Queue Length
#         tx_queue_length = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
#         ve.validate_and_fill(tx_queue_length, tx_queue, "TX Queue Length")

#         # Keepalive Timeout
#         keepalive = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
#         ve.validate_and_fill(keepalive, keepalive_timeout, "Keepalive Timeout")

#         # Send Buffer
#         send_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: sndbuf"]')))
#         ve.validate_and_fill(send_buffer, socket_send_buffer_size, "Send Buffer Size")

#         # Receive Buffer
#         receive_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: rcvbuf"]')))
#         ve.validate_and_fill(receive_buffer, socket_receive_buffer_size, "Receive Buffer Size")

#         # Tunnel Timeout
#         tunnel_timeout_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: inactive"]')))
#         ve.validate_and_fill(tunnel_timeout_input, tunnel_timeout, "Tunnel Timeout")

#         # Status Version Input
#         status_version_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[33]/div[2]/select')))
#         Select(status_version_input).select_by_index(0)

#         # Form Create
#         form_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
#         form_create.click()

#         time.sleep(4)

#         upload_certificate = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[18]/div[2]/button')))
#         upload_certificate.click()
        
#         time.sleep(2)
#         choose = wait.until(EC.presence_of_element_located((By.ID, 'file4')))
#         choose.send_keys("/home/fuse17/Data/Downloads/certificate.csr")
        
#         time.sleep(2)
#         upload = wait.until(EC.presence_of_element_located((By.NAME, 'submit')))
#         upload.click()

        

# # def site_to_site_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, multiple_routes, listening_port, tunnel_local_ip, tunnel_remote_ip, tunnel_mtu, route_delay, tx_queue, keepalive_timeout, socket_send_buffer_size, socket_receive_buffer_size, tunnel_timeout):
#     #     wait = WebDriverWait(self.driver, 10)
#     #     ve = ValidationEngine()
#     #     time.sleep(2)

#     #     # Click on the "TCP Bonded VPN and VPN Profiles" 
#     #     # tcp_bondedvpn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/aside[2]/div/div[4]/div/div/nav/ul/li[9]/a')))
#     #     # tcp_bondedvpn.click()

#     #     # vpn_profiles = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/aside[2]/div/div[4]/div/div/nav/ul/li[9]/ul/li[1]/a')))
#     #     # vpn_profiles.click()

#     #     select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
#     #     select = Select(select_element)
#     #     select.select_by_index(2) 
#     #     time.sleep(2)

#     #     # Click on the "Create" button  
#     #     create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
#     #     create_button.click()
#     #     time.sleep(2)

#     #     profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
#     #     profile_name_field.click()
#     #     profile_name_field.send_keys(profile_name)

#     #     status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/label[2]')))
#     #     status.click()

#     #     configuration_mode = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/label[2]')))
#     #     configuration_mode.click()

#     #     routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))       
#     #     routing_list.click()
#     #     routing_list.send_keys(routes_list)

#     #     route_add_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
#     #     route_add_list.click()

#     #     remote_server_ip_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_ip"]')))
#     #     remote_server_ip_input.click()
#     #     remote_server_ip_input.send_keys(remote_server_ip)

#     #     remote_server_port_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_port"]')))
#     #     remote_server_port_input.click()
#     #     remote_server_port_input.send_keys(remote_server_port)

#     #     # for clicking on "+" button
#     #     route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[5]/div[2]/div[2]/div/div/a')))
#     #     route_add.click()

#     #     tunnel_Local_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="0.0.0.0"]')))
#     #     tunnel_Local_input.click()
#     #     tunnel_Local_input.send_keys(tunnel_local_ip)

#     #     # time.sleep(2)
#     #     tunnel_remot_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: route_gateway"]')))
#     #     tunnel_remot_input.click()
#     #     tunnel_remot_input.send_keys(tunnel_remote_ip)

#     #     tunnel_remot_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: route_gateway"]')))
#     #     tunnel_remot_input.click()
#     #     tunnel_remot_input.send_keys(tunnel_remote_ip)

#     #     # time.sleep(2)
#     #     tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
#     #     tunnel_mtu_input.click()
#     #     tunnel_mtu_input.clear()
#     #     tunnel_mtu_input.send_keys(tunnel_mtu)

#     #     encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
#     #     encryption_algo = Select(encryption_algo)
#     #     encryption_algo.select_by_index(1) 

#     #     # time.sleep(2)
#     #     compression = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[11]/div[2]/div/div/div/label[2]')))
#     #     compression.click()

#     #     initial_traffic_interfaces = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "options: ifaces")]')))
#     #     initial_traffic_interfaces = Select(initial_traffic_interfaces)
#     #     initial_traffic_interfaces.select_by_index(1)

#     #     route_delay_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: route_delay"]')))
#     #     route_delay_input.click()
#     #     route_delay_input.send_keys(route_delay)
#     #     time.sleep(2)
         
#     #     tx_que_length = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
#     #     tx_que_length.click()
#     #     tx_que_length.clear()
#     #     tx_que_length.send_keys(tx_queue)

#     #     keep_alive = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
#     #     keep_alive.click()
#     #     keep_alive.clear()
#     #     keep_alive.send_keys(keepalive_timeout)

#     #     send_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: sndbuf"]')))
#     #     send_buffer.click()
#     #     send_buffer.clear()
#     #     send_buffer.send_keys(socket_send_buffer_size)
        
#     #     receive_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: rcvbuf"]')))
#     #     receive_buffer.click()
#     #     receive_buffer.clear()
#     #     receive_buffer.send_keys(socket_receive_buffer_size)

#     #     tunnel_timeout_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: inactive"]')))
#     #     tunnel_timeout_input.click()
#     #     tunnel_timeout_input.clear()
#     #     tunnel_timeout_input.send_keys(tunnel_timeout)

#     #     status_version_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[33]/div[2]/select')))
#     #     status_version_input = Select(status_version_input)
#     #     status_version_input.select_by_index(0)

#     #     form_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
#     #     form_create.click()
        

#     #     time.sleep(4)

#     # def site_to_multisite_server(self, profile_name, routes_list, listening_port, Tunnel_Network_Subnet, tx_queue, tunnel_mtu, keepalive_timeout, syslog):
            
#     #     wait = WebDriverWait(self.driver, 10)
#     #     ve = ValidationEngine()
#     #     time.sleep(2)

#     #     select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
#     #     select = Select(select_element)
#     #     select.select_by_index(3) 
#     #     time.sleep(2)

#     #     # Click on the "Create" button  
#     #     create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
#     #     create_button.click()
#     #     time.sleep(2)

#     #     profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
#     #     profile_name_field.click()
#     #     profile_name_field.send_keys(profile_name)

#     #     status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/label[2]')))
#     #     status.click()

#     #     routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))       
#     #     routing_list.click()
#     #     routing_list.send_keys(routes_list)

#     #     route_add_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
#     #     route_add_list.click()

#     #     listening_port_01 = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="1 - 65535"]')))
#     #     listening_port_01.click()
#     #     listening_port_01.clear()
#     #     listening_port_01.send_keys(listening_port)

#     #     tunnel_network = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server"]')))
#     #     tunnel_network.click()  
#     #     tunnel_network.clear()
#     #     tunnel_network.send_keys(Tunnel_Network_Subnet)

#     #     encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
#     #     encryption_algo = Select(encryption_algo)
#     #     encryption_algo.select_by_index(1) 

#     #     tx_que_length = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
#     #     tx_que_length.click()
#     #     tx_que_length.clear()
#     #     tx_que_length.send_keys(tx_queue)

#     #     tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
#     #     tunnel_mtu_input.click()
#     #     tunnel_mtu_input.clear()
#     #     tunnel_mtu_input.send_keys(tunnel_mtu)

#     #     keepalive_timeout_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
#     #     keepalive_timeout_input.click()
#     #     keepalive_timeout_input.clear()
#     #     keepalive_timeout_input.send_keys(keepalive_timeout) 

#     #     syslog_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: syslog"]')))
#     #     syslog_input.click()
#     #     syslog_input.clear()
#     #     syslog_input.send_keys(syslog)

#     #     topology = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "topology_list")]')))
#     #     topology = Select(topology)
#     #     topology.select_by_index(1)

#     #     status_version_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[33]/div[2]/select')))
#     #     status_version_input = Select(status_version_input)
#     #     status_version_input.select_by_index(0)

#     #     time.sleep(2)

#     def site_to_multisite_server(self, profile_name, routes_list, listening_port, Tunnel_Network_Subnet, tx_queue, keepalive_timeout, tunnel_timeout, syslog, tunnel_mtu):
       
#         wait = WebDriverWait(self.driver, 10)
#         ve = ValidationEngine()

#         # FORM VALIDATION (before interacting with UI)
#         ve.is_not_empty("Profile Name", profile_name)
#         ve.is_valid_routes_list("Routes List", routes_list)
#         ve.is_within_range("Listening Port", listening_port, 1, 65535)
#         ve.is_within_range("TX Queue Length", tx_queue, 1, 1000)
#         ve.is_within_range("Tunnel Timeout", tunnel_timeout, 1, 3600)
#         ve.is_within_range("Tunnel Mtu", tunnel_mtu, 1, 150000)
#         ve.is_within_range("Keepalive Timeout", keepalive_timeout, 1, 3600)
#         ve.is_valid_ip("Tunnel Network Subnet", Tunnel_Network_Subnet)

#         # Stop if validation fails
#         ve.validate_or_throw()

#         time.sleep(2)
#         # UI Interaction begins
#         select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
#         select = Select(select_element)
#         select.select_by_index(3) 
#         time.sleep(2)
        
        
#         create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
#         create_button.click()

#         time.sleep(2)
#         profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
#         ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")

#         status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/label[2]')))
#         status.click()

#         routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))
#         ve.validate_and_fill(routing_list, routes_list, "Routes List")

#         route_add_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
#         route_add_list.click()
        
#         listening_port_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: port"]')))
#         ve.validate_and_fill(listening_port_input, listening_port, "Listening Port")
       
#         tunnel_network_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server"]')))
#         ve.validate_and_fill(tunnel_network_input, Tunnel_Network_Subnet, "Tunnel Network Subnet")
        
#         tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
#         ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")

#         encryption_algo_element = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
#         Select(encryption_algo_element).select_by_index(1)
        
#         tx_queue_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
#         ve.validate_and_fill(tx_queue_input, tx_queue, "TX Queue Length")

#         keepalive_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
#         ve.validate_and_fill(keepalive_input, keepalive_timeout, "Keepalive Timeout")

#         syslog_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: syslog"]')))
#         syslog_input.click()
#         syslog_input.clear()
#         syslog_input.send_keys(syslog)

#         topology_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "topology_list")]')))
#         Select(topology_dropdown).select_by_index(1)

#         tls_server = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[30]/div[2]/div/div/div/label[2]')))
#         tls_server.click()

#         Suppress_Timestamps = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[32]/div[2]/div/div/div/label[2]')))
#         Suppress_Timestamps.click() 

#         # tunnel_timeout_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: inactive"]')))
#         # ve.validate_and_fill(tunnel_timeout_input, tunnel_timeout, "Tunnel Timeout")


#         form_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
#         form_create.click()

#     def site_to_multisite_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, tx_queue, tunnel_mtu, keepalive_timeout):

#         wait = WebDriverWait(self.driver, 10)
#         ve = ValidationEngine()

#         # FORM VALIDATION (before interacting with UI)
#         ve.is_not_empty("Profile Name", profile_name)
#         ve.is_valid_routes_list("Routes List", routes_list)
#         # ve.is_within_range("Listening Port", listening_port, 1, 65535)
#         # ve.is_within_range("TX Queue Length", tx_queue, 1, 1000)
#         # ve.is_within_range("Remote Server Ip", remote_server_ip)
#         ve.is_valid_ip("Remote Server IP", remote_server_ip)   
#         ve.is_within_range("Remote Server Port", remote_server_port, 1, 65535)
#         ve.is_within_range("Tunnel Mtu", tunnel_mtu, 1, 150000)
#         ve.is_within_range("Keepalive Timeout", keepalive_timeout, 1, 3600)
        

#         # Stop if validation fails
#         ve.validate_or_throw()

#         time.sleep(2)
#         # UI Interaction begins
#         select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
#         select = Select(select_element)
#         select.select_by_index(4) 
#         time.sleep(2)
        
        
#         create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
#         create_button.click()

#         time.sleep(2)
#         profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
#         ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")

#         status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/label[2]')))
#         status.click()

#         configuration_mode = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/label[2]')))
#         configuration_mode.click()

#         routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))
#         ve.validate_and_fill(routing_list, routes_list, "Routes List")

#         route_add_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
#         route_add_list.click()

#         remote_server_ip_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_ip"]')))
#         ve.validate_and_fill(remote_server_ip_input, remote_server_ip, "Remote Server IP")

#         # Remote Server Port
#         remote_server_port_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_port"]')))
#         ve.validate_and_fill(remote_server_port_input, remote_server_port, "Remote Server Port")

#         # Add Route
#         route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[5]/div[2]/div[2]/div/div/a')))
#         route_add.click()

#         tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
#         ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")

#         encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
#         encryption_algo = Select(encryption_algo)
#         encryption_algo.select_by_index(1) 

#         tx_queue_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
#         ve.validate_and_fill(tx_queue_input, tx_queue, "TX Queue Length")

#         keepalive_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
#         ve.validate_and_fill(keepalive_input, keepalive_timeout, "Keepalive Timeout")

#         initial_traffic_interfaces = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "options: ifaces")]')))
#         Select(initial_traffic_interfaces).select_by_index(1)

#         form_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
#         form_create.click()

#         time.sleep(4)

#         upload_certificate = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[18]/div[2]/button')))
#         upload_certificate.click()
        
#         time.sleep(2)
#         choose = wait.until(EC.presence_of_element_located((By.ID, 'file4')))
#         choose.send_keys("/home/fuse17/Data/Downloads/certificate.csr")
        
        
#         upload = wait.until(EC.presence_of_element_located((By.NAME, 'submit')))
#         upload.click()

#         time.sleep(2)
        
from basepage.Basepage import Basepage_base
from utils.ValidationEngine import ValidationEngine

from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
import time

class Connections_01(Basepage_base):

    ve = ValidationEngine()
    
    def open_connection(self):

        wait = WebDriverWait(self.driver, 10)
        tcp_bondedvpn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/aside[2]/div/div[4]/div/div/nav/ul/li[9]/a')))
        tcp_bondedvpn.click()
        vpn_profiles = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/aside[2]/div/div[4]/div/div/nav/ul/li[9]/ul/li[1]/a')))
        vpn_profiles.click()

    def profile_name(self, profile_name):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_not_empty("Profile Name", profile_name)
        
        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
        Connections_01.ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")


    
    def status(self):

        wait = WebDriverWait(self.driver, 10)
        status = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/label[2]')))
        status.click()



    def routing_list(self, routes_list):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_routes_list("Routes List", routes_list)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))
        Connections_01.ve.validate_and_fill(routing_list, routes_list, "Routes List")
        time.sleep(2)
        route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
        route_add.click()



    def listening_port(self, listening_port):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_within_range("Listening Port", listening_port, 1, 65535)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        listening_port_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[3]/div[2]/input')))
        Connections_01.ve.validate_and_fill(listening_port_input, listening_port, "Listening Port")



    def tunnel_local_ip(self, tunnel_local_ip):
        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_ip("Tunnel Local IP", tunnel_local_ip)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        tunnel_local_ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="0.0.0.0"]')))
        Connections_01.ve.validate_and_fill(tunnel_local_ip_input, tunnel_local_ip, "Tunnel Local IP")



    def tunnel_remote_ip(self, tunnel_remote_ip):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_ip("Tunnel Remote IP", tunnel_remote_ip)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        tunnel_remot_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: route_gateway"]')))
        tunnel_remot_input.click()
        tunnel_remot_input.send_keys(tunnel_remote_ip)



    def tunnel_mtu(self, tunnel_mtu):
        
        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_within_range("Tunnel MTU", tunnel_mtu, 1, 1500)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
        Connections_01.ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")



    def encryption(self):
        
        wait = WebDriverWait(self.driver, 10)
        encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
        encryption_algo = Select(encryption_algo)
        encryption_algo.select_by_index(1) 



    def compression(self):

        wait = WebDriverWait(self.driver, 10)
        compression = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[11]/div[2]/div/div/div/label[2]')))
        compression.click()
        
    

    def tx_queue(self, tx_queue):

        Connections_01.ve.is_within_range("TX Queue Length", tx_queue, 1, 1000)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        tx_que_length = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
        tx_que_length.click()
        tx_que_length.clear()
        tx_que_length.send_keys(tx_queue)


    def keepalive_timeout(self, keepalive_timeout):

        Connections_01.ve.is_within_range("Keepalive Timeout", keepalive_timeout, 1, 3600)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        keep_alive = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
        keep_alive.click()
        keep_alive.clear()
        keep_alive.send_keys(keepalive_timeout)



    def socket_send_buffer_size(self, socket_send_buffer_size):
        
        Connections_01.ve.is_within_range("Socket Send Buffer Size", socket_send_buffer_size, 1, 1048576)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        send_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: sndbuf"]')))
        send_buffer.click()
        send_buffer.clear()
        send_buffer.send_keys(socket_send_buffer_size)



    def socket_receive_buffer_size(self, socket_receive_buffer_size):
        
        Connections_01.ve.is_within_range("Socket Receive Buffer Size", socket_receive_buffer_size, 1, 1048576)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        receive_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: rcvbuf"]')))
        receive_buffer.click()
        receive_buffer.clear()
        receive_buffer.send_keys(socket_receive_buffer_size)


    def tunnel_timeout(self, tunnel_timeout):

        Connections_01.ve.is_within_range("Tunnel Timeout", tunnel_timeout, 1, 3600)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        tunnel_timeout_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: inactive"]')))
        tunnel_timeout_input.click()
        tunnel_timeout_input.clear()
        tunnel_timeout_input.send_keys(tunnel_timeout)



    def status_version(self):

        wait = WebDriverWait(self.driver, 10)
        status_version_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[33]/div[2]/select')))
        status_version_input = Select(status_version_input)
        status_version_input.select_by_index(0)

    def form_create(self):

        wait = WebDriverWait(self.driver, 10)
        form_create = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
        form_create.click()


    def suppress_timestamps(self):
        
        wait = WebDriverWait(self.driver, 10)
        suppress_timestamps = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[32]/div[2]/div/div/div/label[2]')))
        suppress_timestamps.click()
 

    def presist_authentication(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        presist_authentication = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[26]/div[2]/div/div/div/label[2]')))
        presist_authentication.click()

    def presist_tunnel_interface(self):
        
        wait = WebDriverWait(self.driver, 10)
        presist_tunnel_interface = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[25]/div/div[2]/div/div/div/label[2]')))
        presist_tunnel_interface.click()

    def performance(self):
        
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        performance = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[2]/div[2]/div/div/div/label[1]')))
        performance.click()

    def remote_server_ip(self, remote_server_ip):

        Connections_01.ve.is_valid_ip("Remote Server IP", remote_server_ip)
        
        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_ip("Remote Server IP", remote_server_ip)
        remote_server_ip_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_ip"]')))
        Connections_01.ve.validate_and_fill(remote_server_ip_input, remote_server_ip, "Remote Server IP")

        


    def remote_server_port(self, remote_server_port):

        Connections_01.ve.is_valid_port("Remote Server Port", remote_server_port)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        remote_server_port_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_port"]')))
        Connections_01.ve.validate_and_fill(remote_server_port_input, remote_server_port, "Remote Server Port")
        route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[5]/div[2]/div[2]/div/div/a')))
        route_add.click()


    def route_delay(self, route_delay):

        Connections_01.ve.is_within_range("Route Delay", route_delay, 1, 3600)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        route_delay_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: route_delay"]')))
        Connections_01.ve.validate_and_fill(route_delay_input, route_delay, "Route Delay")

    def config_mode(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        configuration_mode = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/label[2]')))
        configuration_mode.click()

    
    def innitial_traffic(self):

        wait = WebDriverWait(self.driver, 10)
        initial_traffic_interfaces = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "options: ifaces")]')))
        Select(initial_traffic_interfaces).select_by_index(1)

    def protocol(self):

        wait = WebDriverWait(self.driver, 10)
        protocol = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[3]/div[2]/select')))
        protocol = Select(protocol)
        protocol.select_by_index(0)

    def syslog(self, syslog):

        Connections_01.ve.is_within_range("Syslog", syslog, 1, 1000)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        syslog_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: syslog"]')))
        syslog_input.click()
        syslog_input.clear()
        syslog_input.send_keys(syslog)

    def tunnel_network_subnet(self, Tunnel_Network_Subnet):

        Connections_01.ve.is_valid_ip("Tunnel Network Subnet", Tunnel_Network_Subnet)

        # Stop if validation fails
        Connections_01.ve.validate_or_throw()
        wait = WebDriverWait(self.driver, 10)
        tunnel_network_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server"]')))
        Connections_01.ve.validate_and_fill(tunnel_network_input, Tunnel_Network_Subnet, "Tunnel Network Subnet")


    def topolgy(self):

        wait = WebDriverWait(self.driver, 10)
        topology_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "topology_list")]')))
        select = Select(topology_dropdown)
        select.select_by_index(1) 


    def tls_server(self):

        wait = WebDriverWait(self.driver, 10)
        tls_server = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[30]/div[2]/div/div/div/label[2]')))
        tls_server.click()

    def upload_certificates(self):

        wait = WebDriverWait(self.driver, 10)
        upload_certificate = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[18]/div[2]/button')))
        upload_certificate.click()
        
        time.sleep(2)
        choose = wait.until(EC.presence_of_element_located((By.ID, 'file4')))
        choose.send_keys("/home/fuse17/Data/Downloads/certificate.csr")
        
        
        upload = wait.until(EC.presence_of_element_located((By.NAME, 'submit')))
        upload.click()

        time.sleep(2)

    def remote_certes(self):

        wait = WebDriverWait(self.driver, 10)
        remote_certificates = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[34]/div/div[2]/select')))
        Select(remote_certificates).select_by_index(1)
        


    def site_to_site_server(self, profile_name, routes_list, multiple_routes, listening_port, tunnel_local_ip, tunnel_remote_ip, tunnel_mtu, tx_queue, keepalive_timeout, socket_send_buffer_size, socket_receive_buffer_size, tunnel_timeout):  #l_port, list_port, local_ip, remote_ip, send_buffer, receive_buffer, tunnel_timeout
       
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
        select = Select(select_element)
        select.select_by_index(1) 
        time.sleep(2)
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
        create_button.click()
        time.sleep(2)

        Connections_01.profile_name(self, profile_name)
        Connections_01.status(self)
        # Connections_01.status(self)
        Connections_01.routing_list(self, routes_list)
        # Connections_01.performance(self)
        Connections_01.listening_port(self, listening_port)
        Connections_01.tunnel_local_ip(self, tunnel_local_ip)
        Connections_01.tunnel_remote_ip(self, tunnel_remote_ip)
        Connections_01.tunnel_mtu(self, tunnel_mtu)
        Connections_01.encryption(self)
        Connections_01.compression(self)
        Connections_01.tx_queue(self, tx_queue)
        Connections_01.keepalive_timeout(self, keepalive_timeout)
        Connections_01.socket_send_buffer_size(self, socket_send_buffer_size)
        Connections_01.socket_receive_buffer_size(self, socket_receive_buffer_size)
        Connections_01.presist_tunnel_interface(self)
        # Connections_01.presist_authentication(self)
        Connections_01.tunnel_timeout(self, tunnel_timeout)
        Connections_01.suppress_timestamps(self)
        Connections_01.status_version(self)
        Connections_01.form_create(self)

    def site_to_site_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, multiple_routes, listening_port, tunnel_local_ip, tunnel_remote_ip, tunnel_mtu, route_delay, tx_queue, keepalive_timeout, socket_send_buffer_size, socket_receive_buffer_size, tunnel_timeout):
        
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
        select = Select(select_element)
        select.select_by_index(2) 
        time.sleep(2)
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
        create_button.click()
        time.sleep(2)

        Connections_01.profile_name(self, profile_name)
        Connections_01.status(self)
        Connections_01.status(self)
        Connections_01.config_mode(self)
        Connections_01.routing_list(self, routes_list)
        Connections_01.performance(self)
        Connections_01.remote_server_ip(self, remote_server_ip)
        Connections_01.remote_server_port(self, remote_server_port)
        Connections_01.tunnel_local_ip(self, tunnel_local_ip)
        Connections_01.tunnel_remote_ip(self, tunnel_remote_ip)
        Connections_01.tunnel_mtu(self, tunnel_mtu)
        Connections_01.encryption(self)
        Connections_01.compression(self)
        Connections_01.innitial_traffic(self)
        Connections_01.route_delay(self, route_delay)
        Connections_01.tx_queue(self, tx_queue)
        Connections_01.keepalive_timeout(self, keepalive_timeout)
        Connections_01.socket_send_buffer_size(self, socket_send_buffer_size)
        Connections_01.socket_receive_buffer_size(self,socket_receive_buffer_size)
        Connections_01.presist_tunnel_interface(self)
        # Connections_01.presist_authentication(self)
        Connections_01.tunnel_timeout(self, tunnel_timeout)
        Connections_01.suppress_timestamps(self)
        Connections_01.status_version(self)
        Connections_01.form_create(self)
        Connections_01.upload_certificates(self)

    def site_to_multisite_server(self, profile_name, routes_list, listening_port, Tunnel_Network_Subnet, tx_queue, keepalive_timeout, tunnel_timeout, syslog, tunnel_mtu):
        
        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
        select = Select(select_element)
        select.select_by_index(3) 
        time.sleep(2)
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
        create_button.click()
        time.sleep(2)

        Connections_01.profile_name(self, profile_name)
        Connections_01.status(self)
        Connections_01.routing_list(self,routes_list)
        # Connections_01.performance(self)
        Connections_01.listening_port(self,listening_port)
        Connections_01.tunnel_network_subnet(self, Tunnel_Network_Subnet)
        Connections_01.tunnel_mtu(self, tunnel_mtu)
        Connections_01.encryption(self)
        Connections_01.tx_queue(self, tx_queue)
        Connections_01.keepalive_timeout(self,keepalive_timeout)
        Connections_01.presist_tunnel_interface(self)
        # Connections_01.presist_authentication(self)
        Connections_01.syslog(self,syslog)
        Connections_01.suppress_timestamps(self)
        Connections_01.status_version(self)
        Connections_01.form_create(self)

    def site_to_multisite_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, tx_queue, tunnel_mtu, keepalive_timeout):

        wait = WebDriverWait(self.driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/select')))
        select = Select(select_element)
        select.select_by_index(4) 
        time.sleep(2)
        create_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/form/div/div[1]/div[2]/button')))
        create_button.click()
        time.sleep(2)

        Connections_01.profile_name(self, profile_name)
        Connections_01.status(self)
        Connections_01.config_mode(self)
        Connections_01.routing_list(self,routes_list)
        # Connections_01.protocol(self)
        Connections_01.performance(self)
        Connections_01.remote_server_ip(self, remote_server_ip)
        Connections_01.remote_server_port(self,remote_server_port)
        Connections_01.tunnel_mtu(self, tunnel_mtu)
        Connections_01.encryption(self)
        Connections_01.innitial_traffic(self)
        time.sleep(2)
        Connections_01.tx_queue(self, tx_queue)
        Connections_01.keepalive_timeout(self, keepalive_timeout)
        Connections_01.presist_authentication(self)
        Connections_01.remote_certes(self)
        time.sleep(2)
        Connections_01.form_create(self)
        time.sleep(2)
        Connections_01.upload_certificates(self)