import re
from selenium.webdriver.common.keys import Keys
from basepage.Basepage import Basepage_base
# from utils.ValidationEngine import ValidationEngine
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.support.ui import Select # type: ignore
import time


class ValidationEngine():
    def __init__(self):
        self.errors = []

    def is_valid_username(self, field_name, username):
        if not username or len(username.strip()) < 3:
            self.errors.append(f"{field_name} must be at least 3 characters long.")

    def is_valid_password(self, field_name, password):
        if not password or len(password) < 6:
            self.errors.append(f"{field_name} must be at least 6 characters long.")

    def is_not_empty(self, field_name, value):
        if not value or str(value).strip() == "":
            self.errors.append(f"{field_name} should not be empty.")

    def validate_and_fill(self, element, value, field_name=""):
        try:
            element.click()
            element.clear()
            element.send_keys(value)
            print(f"{field_name} set to: {value}")
        except Exception as e:
            print(f"Failed to set {field_name}. Error: {e}")

    def is_valid_ip(self, field_name, ip_address):
        # Regular expression to validate IP address (IPv4)
        ip_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if not re.match(ip_regex, ip_address):
            self.errors.append(f"{field_name} must be a valid IP address.")
    
    def is_valid_port(self, field_name, port):
        try:
            port = int(port)
            if port < 1 or port > 65535:
                self.errors.append(f"{field_name} must be a valid port number between 1 and 65535.")
        except ValueError:
            self.errors.append(f"{field_name} must be a valid integer for a port.")


    def is_valid_ip(self, field_name, ip):
        pattern = r".*"
        if not re.match(pattern, ip):
            self.errors.append(f"{field_name} has invalid IP format.")

    def is_within_range(self, field_name, value, min_val, max_val):
        try:
            value = int(value)
            if not (min_val <= value <= max_val):
                self.errors.append(f"{field_name} should be between {min_val} and {max_val}.")
        except ValueError:
            self.errors.append(f"{field_name} should be an integer.")

    def is_valid_routes_list(self, field_name, value):
        pattern = r"^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$"
        if not re.match(pattern, value):
            self.errors.append(f"{field_name} is not in valid CIDR format.")

    def validate_bulk_routes(self, field_name, routes_list):
        for route in routes_list:
            self.is_valid_routes_list(f"{field_name} route '{route}'", route)

    def validate_or_throw(self):
        if self.errors:
            raise Exception("Validation failed:\n" + "\n".join(self.errors))

    def report(self):
        return self.errors

    def clear(self):
        self.errors = []

    # def is_not_empty(self, field_name, value):
    #     if not value.strip():
    #         self.errors.append(f"{field_name} cannot be empty.")

    # def is_within_limit(self, field_name, value, min_len=1, max_len=255):
    #     if not (min_len <= len(value) <= max_len):
    #         self.errors.append(f"{field_name} must be between {min_len} and {max_len} characters.")


    # def validate_multiple_inputs(self, field_name, inputs, min_len=1, max_len=255):
    #     print(f"\n🧪 Validating multiple inputs for: {field_name}")
    #     for value in inputs:
    #         self.errors = []  # Clear previous errors
    #         print(f"➡️  Testing value: '{value}'")
            
    #         self.is_not_empty(field_name, value)
    #         self.is_within_limit(field_name, value, min_len, max_len)
            
    #         if self.errors:
    #             print(f"❌ Invalid: {self.errors}")
    #         else:
    #             print("✅ Valid input.")