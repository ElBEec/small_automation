import time
import  unittest
from unittest import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from utils import Driver_setup



from src.common.actions import TestLogin






class Tests(TestLogin):

 def test_contact_us(self):
      contact_button = self.my_driver.find_element(Driver_setup.By.XPATH,'//*[@id="menu-item-25"]/a/span[2]')
      contact_button.click()
      time.sleep(2)
      input_first_name = self.my_driver.find_element(Driver_setup.By.XPATH,'//*[@id="post-24"]/div/div/form/div[1]/input')
      input_first_name.send_keys('aviv')
      input_last_name = self.my_driver.find_element(Driver_setup.By.XPATH,'//*[@id="post-24"]/div/div/form/div[2]/input')
      input_last_name.send_keys('mucha')
      input_email = self.my_driver.find_element(Driver_setup.By.XPATH,'//*[@id="post-24"]/div/div/form/div[3]/input')
      input_email.send_keys('avivmucha0@gmail.com')
      input_content = self.my_driver.find_element(Driver_setup.By.XPATH,'//*[@id="post-24"]/div/div/form/div[4]/textarea')
      input_content.send_keys('it was very nice')
      input_submit = self.my_driver.find_element(Driver_setup.By.XPATH,'//*[@id="post-24"]/div/div/form/div[7]/button/div')
      input_submit.click()
      time.sleep(2)
      assert self.my_driver.find_element(Driver_setup.By.CLASS_NAME,'uagb-forms-success-message-173d6c98')

