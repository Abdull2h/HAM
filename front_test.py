from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import time

driver = webdriver.Chrome()



driver.get('http://the-gnn.herokuapp.com/')
driver.find_element_by_link_text('About us').click()
print(driver.title)
print(driver.current_url)

driver.get('http://the-gnn.herokuapp.com/')
driver.find_element_by_link_text('Members').click()
print(driver.title)
print(driver.current_url)

driver.get('http://the-gnn.herokuapp.com/')
driver.find_element_by_link_text('Sign up!').click()
print(driver.title)
print(driver.current_url)

driver.get('http://the-gnn.herokuapp.com/')
action = driver.find_element_by_xpath("//a[@href='action']")
driver.execute_script("arguments[0].click();", action)
print(driver.title)
print(driver.current_url)

driver.get('http://the-gnn.herokuapp.com/')
adventure = driver.find_element_by_xpath("//a[@href='adventure']")
driver.execute_script("arguments[0].click();", adventure)
print(driver.title)
print(driver.current_url)

driver.get('http://the-gnn.herokuapp.com/')
Sport = driver.find_element_by_xpath("//a[@href='sports']")
driver.execute_script("arguments[0].click();", Sport)
print(driver.title)
print(driver.current_url)

#test contact us page and sending an eamil
driver.get('http://the-gnn.herokuapp.com/')
driver.find_element_by_link_text('Contact us').click()
driver.find_element_by_id('name').send_keys('Mohammed')
driver.find_element_by_id('email').send_keys('moh.daim996@gmail.com')
driver.find_element_by_id('phone').send_keys('123456789')
country=Select(driver.find_element_by_id('exampleFormControlSelect1'))
country.select_by_visible_text("Saudi Arabia")
messege = driver.find_element_by_id('exampleFormControlTextarea1')
messege.send_keys('my messege')
messege.submit()
print(driver.title)
print(driver.current_url)
driver.close()
driver.quit()




'''
links = driver.find_elements(By.TAG_NAME,'a')
for lnk in links:
    time.sleep(2)
    try:
        page=driver.find_element_by_link_text(lnk.text)
        page.click()
    except StaleElementReferenceException:
        pass
    else:
        print(driver.current_url)
    finally:
        driver.get('http://the-gnn.herokuapp.com/')
'''

