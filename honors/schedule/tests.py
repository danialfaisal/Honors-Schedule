import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       #Pre-defined variables
       user = "instructor"
       pwd = "maverick1a"
       newuser = "test-instructor"
       newpwd = "4900testing"
       fname = "test"
       lname = "test"
       email = "test@test.com"




       #Opening browser & maximizing window
       driver = self.driver
       driver.fullscreen_window()


       #logging in to the admin page
       driver.get("https://honors-schedule.herokuapp.com/admin")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       assert "Logged In"


       #Creating a new test User
       elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[2]/table/tbody/tr[5]/td[1]/a")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(newuser)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys(newpwd)
       time.sleep(2)
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys(newpwd)
       time.sleep(2)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys(fname)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys(lname)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"id_is_staff\"]")
       elem.click()
       time.sleep(1)
       elem = driver.find_element_by_xpath("//*[@id=\"id_is_superuser\"]")
       elem.click()
       time.sleep(1)
       elem.send_keys(Keys.RETURN)
       time.sleep(3)
       assert "Test user created"

       #Deleting the last created User
       elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr[last()]/td[1]/input")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select/option[2]")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/button")
       elem.click()
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[4]")
       elem.click()
       time.sleep(3)
       assert "Deleted New test user"




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
