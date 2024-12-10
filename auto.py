import time
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pywifi

# WiFi connection settings
# wifi_name = "Bivek's iPhone"
# wifi_password = "okgood12"

# Webpage login settings
url = "https://npl.bivekthapa.com.np/index.php/login/?redirect_to=https%3A%2F%2Fnpl.bivekthapa.com.np%2F"
username = "id"
password = "pass"

# Connect to WiFi
# wifi = pywifi.PyWiFi()
# interface = wifi.interfaces()[0]
# interface.connect(wifi_name, wifi_password)


# Open webpage and login
driver = webdriver.Edge()
driver.get(url)

driver.find_element(by="id", value="username-51").send_keys(username)
driver.find_element(by="id", value="user_password-51").send_keys(password)

# time.sleep(15)
# driver.find_element_by_name('username-51').send_keys(username)
# driver.find_element_by_name('user_password-51').send_keys(password)
# driver.find_element_by_css_selector("input[type=submit].um-button").click()

print("run successfully")

# username_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "username"))
# )
# username_input.send_keys(username)

# password_input = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "password"))
# )
# password_input.send_keys(password)

# login_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.NAME, "login"))
# )
# login_button.click()
