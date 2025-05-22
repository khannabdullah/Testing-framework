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
        profile_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[2]/input')))
        Connections_01.ve.validate_and_fill(profile_name_field, profile_name, "Profile Name")


    
    def status(self):

        wait = WebDriverWait(self.driver, 10)
        status = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[1]/div[3]/select')))
        status.click()



    def routing_list(self, routes_list):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_routes_list("Routes List", routes_list)
        routing_list = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/input')))
        Connections_01.ve.validate_and_fill(routing_list, routes_list, "Routes List")
        route_add = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[6]/div[2]/div[2]/div/span[1]/a')))
        route_add.click()



    def listening_port(self, listening_port):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_within_range("Listening Port", listening_port, 1, 65535)
        listening_port_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: port"]')))
        Connections_01.ve.validate_and_fill(listening_port_input, listening_port, "Listening Port")



    def tunnel_local_ip(self, tunnel_local_ip):
        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_ip("Tunnel Local IP", tunnel_local_ip)
        tunnel_local_ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="0.0.0.0"]')))
        Connections_01.ve.validate_and_fill(tunnel_local_ip_input, tunnel_local_ip, "Tunnel Local IP")



    def tunnel_remote_ip(self, tunnel_remote_ip):

        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_ip("Tunnel Remote IP", tunnel_remote_ip)
        tunnel_remot_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: route_gateway"]')))
        tunnel_remot_input.click()
        tunnel_remot_input.send_keys(tunnel_remote_ip)



    def tunnel_mtu(self, tunnel_mtu):
        
        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_within_range("Tunnel MTU", tunnel_mtu, 1, 1500)
        tunnel_mtu_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@data-bind="textInput: tun_mtu"]')))
        Connections_01.ve.validate_and_fill(tunnel_mtu_input, tunnel_mtu, "Tunnel MTU")



    def encryption(self):
        
        wait = WebDriverWait(self.driver, 10)
        encryption_algo = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "cipher_list")]')))
        encryption_algo = Select(encryption_algo)
        encryption_algo.select_by_index(1) 



    def compression(self):

        wait = WebDriverWait(self.driver, 10)
        compression = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[11]/div[2]/div/div/div/label[2]')))
        compression.click()
        
    

    def tx_queue(self, tx_queue):

        Connections_01.ve.is_within_range("TX Queue Length", tx_queue, 1, 1000)
        wait = WebDriverWait(self.driver, 10)
        tx_que_length = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: txqueuelen"]')))
        tx_que_length.click()
        tx_que_length.clear()
        tx_que_length.send_keys(tx_queue)


    def keepalive_timeout(self, keepalive_timeout):

        Connections_01.ve.is_within_range("Keepalive Timeout", keepalive_timeout, 1, 3600)
        wait = WebDriverWait(self.driver, 10)
        keep_alive = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: keepalive"]')))
        keep_alive.click()
        keep_alive.clear()
        keep_alive.send_keys(keepalive_timeout)



    def socket_send_buffer_size(self, socket_send_buffer_size):
        
        Connections_01.ve.is_within_range("Socket Send Buffer Size", socket_send_buffer_size, 1, 1048576)
        wait = WebDriverWait(self.driver, 10)
        send_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: sndbuf"]')))
        send_buffer.click()
        send_buffer.clear()
        send_buffer.send_keys(socket_send_buffer_size)



    def socket_receive_buffer_size(self, socket_receive_buffer_size):
        
        Connections_01.ve.is_within_range("Socket Receive Buffer Size", socket_receive_buffer_size, 1, 1048576)
        wait = WebDriverWait(self.driver, 10)
        receive_buffer = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: rcvbuf"]')))
        receive_buffer.click()
        receive_buffer.clear()
        receive_buffer.send_keys(socket_receive_buffer_size)


    def tunnel_timeout(self, tunnel_timeout):

        Connections_01.ve.is_within_range("Tunnel Timeout", tunnel_timeout, 1, 3600)
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
        form_create = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[9]/div/button[1]')))
        form_create.click()


    def suppress_timestamps(self):
        
        wait = WebDriverWait(self.driver, 10)
        suppress_timestamps = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[32]/div[2]/div/div/div/label[2]')))
        suppress_timestamps.click()
 

    def presist_authentication(self):
        
        wait = WebDriverWait(self.driver, 10)
        presist_authentication = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[27]/div[2]/div/div/div/label[2]')))
        presist_authentication.click()

    def presist_tunnel_interface(self):
        
        wait = WebDriverWait(self.driver, 10)
        presist_tunnel_interface = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[25]/div/div[2]/div/div/div/label[2]')))
        presist_tunnel_interface.click()

    def performance(self):
        
        wait = WebDriverWait(self.driver, 10)
        performance = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[2]/div[2]/div/div/div/label[1]')))
        performance.click()

    def remote_server_ip(self, remote_server_ip):

        Connections_01.ve.is_valid_ip("Remote Server IP", remote_server_ip)
        
        wait = WebDriverWait(self.driver, 10)
        Connections_01.ve.is_valid_ip("Remote Server IP", remote_server_ip)
        remote_server_ip_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_ip"]')))
        Connections_01.ve.validate_and_fill(remote_server_ip_input, remote_server_ip, "Remote Server IP")

        


    def remote_server_port(self, remote_server_port):

        Connections_01.ve.is_valid_port("Remote Server Port", remote_server_port)
        wait = WebDriverWait(self.driver, 10)
        remote_server_port_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server_port"]')))
        Connections_01.ve.validate_and_fill(remote_server_port_input, remote_server_port, "Remote Server Port")


    def route_delay(self, route_delay):

        Connections_01.ve.is_within_range("Route Delay", route_delay, 1, 3600)
        wait = WebDriverWait(self.driver, 10)
        route_delay_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: route_delay"]')))
        Connections_01.ve.validate_and_fill(route_delay_input, route_delay, "Route Delay")

    def config_mode(self):

        wait = WebDriverWait(self.driver, 10)
        configuration_mode = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/label[2]')))
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
        wait = WebDriverWait(self.driver, 10)
        syslog_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: syslog"]')))
        syslog_input.click()
        syslog_input.clear()
        syslog_input.send_keys(syslog)

    def tunnel_network_subnet(self, Tunnel_Network_Subnet):

        Connections_01.ve.is_valid_ip("Tunnel Network Subnet", Tunnel_Network_Subnet)
        wait = WebDriverWait(self.driver, 10)
        tunnel_network_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-bind="textInput: server"]')))
        Connections_01.ve.validate_and_fill(tunnel_network_input, Tunnel_Network_Subnet, "Tunnel Network Subnet")


    def topolgy(self):

        wait = WebDriverWait(self.driver, 10)
        topology_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, '//select[contains(@data-bind, "topology_list")]')))
        Select(topology_dropdown).select_by_index(1)


    def tls_server(self):

        wait = WebDriverWait(self.driver, 10)
        tls_server = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[30]/div[2]/div/div/div/label[2]')))
        tls_server.click()

    def upload_certificates(self):

        wait = WebDriverWait(self.driver, 10)
        upload_certificate = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[8]/section/div/div/div[2]/form/div/div[8]/div[18]/div[2]/button')))
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
       
        Connections_01.profile_name(profile_name)
        Connections_01.status()
        Connections_01.status()
        Connections_01.routing_list(routes_list)
        Connections_01.performance()
        Connections_01.listening_port(listening_port)
        Connections_01.tunnel_local_ip(tunnel_local_ip)
        Connections_01.tunnel_remote_ip(tunnel_remote_ip)
        Connections_01.tunnel_mtu(tunnel_mtu)
        Connections_01.encryption()
        Connections_01.compression()
        Connections_01.tx_queue(tx_queue)
        Connections_01.keepalive_timeout(keepalive_timeout)
        Connections_01.socket_send_buffer_size(socket_send_buffer_size)
        Connections_01.socket_receive_buffer_size(socket_receive_buffer_size)
        Connections_01.presist_tunnel_interface()
        Connections_01.presist_authentication()
        Connections_01.tunnel_timeout(tunnel_timeout)
        Connections_01.suppress_timestamps()
        Connections_01.status_version()
        Connections_01.form_create()

    def site_to_site_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, multiple_routes, listening_port, tunnel_local_ip, tunnel_remote_ip, tunnel_mtu, route_delay, tx_queue, keepalive_timeout, socket_send_buffer_size, socket_receive_buffer_size, tunnel_timeout):
        
        Connections_01.profile_name(profile_name)
        Connections_01.status()
        Connections_01.status()
        Connections_01.config_mode()
        Connections_01.routing_list(routes_list)
        Connections_01.performance()
        Connections_01.remote_server_ip(remote_server_ip)
        Connections_01.remote_server_port(remote_server_port)
        Connections_01.tunnel_local_ip(tunnel_local_ip)
        Connections_01.tunnel_remote_ip(tunnel_remote_ip)
        Connections_01.tunnel_mtu(tunnel_mtu)
        Connections_01.encryption()
        Connections_01.compression()
        Connections_01.innitial_traffic()
        Connections_01.route_delay(route_delay)
        Connections_01.tx_queue(tx_queue)
        Connections_01.keepalive_timeout(keepalive_timeout)
        Connections_01.socket_send_buffer_size(socket_send_buffer_size)
        Connections_01.socket_receive_buffer_size(socket_receive_buffer_size)
        Connections_01.presist_tunnel_interface()
        Connections_01.presist_authentication()
        Connections_01.tunnel_timeout(tunnel_timeout)
        Connections_01.suppress_timestamps()
        Connections_01.status_version()
        Connections_01.form_create()
        Connections_01.upload_certificates()

    def site_to_multisite_server(self, profile_name, routes_list, listening_port, Tunnel_Network_Subnet, tx_queue, keepalive_timeout, tunnel_timeout, syslog, tunnel_mtu):
        
        Connections_01.profile_name(profile_name)
        Connections_01.status()
        Connections_01.routing_list(routes_list)
        Connections_01.performance()
        Connections_01.listening_port(listening_port)
        Connections_01.tunnel_network_subnet(Tunnel_Network_Subnet)
        Connections_01.tunnel_mtu(tunnel_mtu)
        Connections_01.encryption()
        Connections_01.tx_queue(tx_queue)
        Connections_01.keepalive_timeout(keepalive_timeout)
        Connections_01.presist_tunnel_interface()
        Connections_01.presist_authentication()
        Connections_01.syslog(syslog)
        Connections_01.suppress_timestamps()
        Connections_01.status_version()
        Connections_01.form_create()

    def site_to_multisite_client(self, profile_name, routes_list, remote_server_ip, remote_server_port, tx_queue, tunnel_mtu, keepalive_timeout):

        Connections_01.profile_name(profile_name)
        Connections_01.status()
        Connections_01.config_mode()
        Connections_01.routing_list(routes_list)
        Connections_01.protocol()
        Connections_01.performance()
        Connections_01.remote_server_ip(remote_server_ip)
        Connections_01.remote_server_port(remote_server_port)
        Connections_01.tunnel_mtu(tunnel_mtu)
        Connections_01.encryption()
        Connections_01.innitial_traffic()
        Connections_01.tx_queue(tx_queue)
        Connections_01.keepalive_timeout(keepalive_timeout)
        Connections_01.presist_authentication()
        Connections_01.remote_certes()
        time.sleep(2)
        Connections_01.form_create()
        time.sleep(2)
        Connections_01.upload_certificates()