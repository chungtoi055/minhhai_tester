
from selenium import webdriver
from selenium.webdriver.common.by import By
test_driver = webdriver.Chrome()

# Di chuyển đến địa chỉ "....."
test_driver.get('https://www.nhaccuatui.com/')
          #chờ ngầm định
# 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '//*[@id="btnShowBoxLogin"]/div/p').click()
#button = test_driver.find_element(By.XPATH, '//*[@id="btnShowBoxLogin"]/div/p')
#test_driver.execute_script("arguments[0].click();", button)
# 3: Bấm vào button "Đăng nhập/ Login"


test_driver.find_element(By.XPATH, '//*[@id="_frmLogin"]/div/a').click()