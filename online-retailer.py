from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')

  driver = webdriver.Chrome(options=options)

  # Create an account on this website below 👇 or change the website
  driver.get('https://titan22.com/account/login?return_url=%2Faccount')
  return driver


def main():
  driver = get_driver()

  # Find and fill the username and wait 2 sec (Put your email here 👇)
  driver.find_element(by='id', value='CustomerEmail').send_keys('Your EMAIL here!')
  time.sleep(2)

  # Find and fill the password and wait 2 sec and Press the Enter link (Password 👇)
  driver.find_element(by='id', value='CustomerPassword').send_keys('Your PASSWORD here' + Keys.RETURN)
  time.sleep(2)

  # Click the CONTACT US link
  text = driver.find_element(by='xpath', value='/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()

  # Print the Current Link
  print(driver.current_url)


if __name__ == '__main__':
  print(main())
