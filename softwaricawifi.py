from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "http://gateway.example.com/no_cookie_loginpages/dns_post.shtml"
username = "softwarica"
password = "cov3ntry123"

driver = webdriver.Edge()
driver.get(url)

sleep(1)
driver.find_element(by="name", value="agree").click()
driver.find_element(by="class name", value="fwrapper").click()

sleep(1)

# Wait for the username field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
username_field.send_keys(username)

# Wait for the password field to be present
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password_field.send_keys(password)

driver.find_element(by="class name", value="fwrapper").click()

print("run successfully")

# sleep(1)

# driver.get("https://npl.bivekthapa.com.np/index.php/table/")
# print(driver.find_element(by="css selector", value=".easybet_rank_user:nth-child(2)").text)