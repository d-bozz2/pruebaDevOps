import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://localhost:8013")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

driver.get("http://localhost:8013")

driver.find_element(By.XPATH, "//input[@value='Create new ticket']").click()

elementoAsunto = driver.find_element(By.XPATH, "//input[@name='Subject']")
elementoAsunto.clear()
elementoAsunto.send_keys("Test")


driver.find_element(By.XPATH, "(//input[@value='Crear'])[1]").click()

time.sleep(30)

# tirar error de cross scripting

driver.close()