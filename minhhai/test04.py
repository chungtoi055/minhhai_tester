from Tools.demo.markov import test
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


test_driver = webdriver.Chrome()

#Step 1: Di chuyển đến địa chỉ "....."
test_driver.get('https://www.nhaccuatui.com/')


#Step 2: Bấm vào button "Đăng nhập"
test_driver.find_element(By.XPATH, '//*[@id="btnShowBoxLogin"]/div/p').click()

test_driver.implicitly_wait(4)

# Step 3: Nhập username
test_driver.find_element(By.XPATH, '//*[@id="uname"]').send_keys('qwertyuiop1208')


# Step 4: Nhập password
test_driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('qwertyuiop1208')

# Step 5: Bấm vào button "Đăng nhập/Login "
test_driver.find_element(By.XPATH, '//*[@id="_frmLogin"]/div/a').click()

# Step 6: Để trống thanh tìm kiếm
test_driver.find_element(By.XPATH, '//*[@id="txtSearch"]').send_keys('')

# Step 7: Bấm vào button  "tìm kiếm"
test_driver.find_element(By.XPATH, '//*[@id="btnSearch"]').click()


#tắt testcase
# test_driver.close()
# test_driver.quit()