from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass
import time

# xpaths
menu= "//*[@title='Menu']"
new_grp = "//*[text()='New group']"
contact_field = "//*[@placeholder='Type contact name']"
create_grp =  "//*[@data-icon='arrow-forward']"
msg_box = "//*[text()='Type a message']"

# contact names should be exact
contact_names = ['Chaitanya','Sai Kumar']
group_name = 'CT Automation Test'
msg_txt = "Just Some cool automations"

driver = webdriver.Chrome()
grp_name_actions= ActionChains(driver)
msg_actions = ActionChains(driver)
driver.get('https://web.whatsapp.com/')

## Scan QR in this time.
time.sleep(20)

(driver.find_element_by_xpath(menu)).click()
(driver.find_element_by_xpath(new_grp)).click()

# adding contacts to group
contact_fld_ele = driver.find_element_by_xpath(contact_field)
for cntct in contact_names:
    time.sleep(0.5)
    time.sleep(1)
    contact_fld_ele.send_keys(cntct)
    contact_fld_ele.send_keys(Keys.RETURN)

(driver.find_element_by_xpath(create_grp)).click()

time.sleep(1)
#naming group and proceeding

grp_name_actions.send_keys(group_name)
grp_name_actions.send_keys(Keys.RETURN)
grp_name_actions.perform()
time.sleep(3)

#sending message
msg_actions.send_keys(msg_txt)
msg_actions.send_keys(Keys.RETURN)
msg_actions.perform()
