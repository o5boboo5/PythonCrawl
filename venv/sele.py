from selenium import webdriver

driver_path='/Users/o5boboo5/PycharmProjects/chromedriver'

driver=webdriver.Chrome(executable_path=driver_path)

driver.get('http://www.baidu.com')

print(driver.page_source)