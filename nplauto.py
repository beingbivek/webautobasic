from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

url = "https://npl.bivekthapa.com.np/index.php/login"
username = "username"
password = "pass"

driver = webdriver.Edge()
driver.get(url)

# Wait for the username field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username-51"))
)
username_field.send_keys(username)

# Wait for the password field to be present
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "user_password-51"))
)
password_field.send_keys(password)

driver.find_element(by="css selector", value="input[type=submit].um-button").click()

print("run successfully")

sleep(1)

driver.get("https://npl.bivekthapa.com.np/index.php/table/")
print(driver.find_element(by="css selector", value=".easybet_rank_user:nth-child(2)").text)