from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from ExpediaTask.Core.Constants import *

class OpenBrowser:
  @staticmethod
  def OpenChromeBrowser():
    options = ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path=Constants.CHROME_DRIVER_PATH, chrome_options=options)
    driver.implicitly_wait(100)
    driver.maximize_window()
    return driver

  @staticmethod
  def OpenFireFoxBrowser():
    options = FireFoxOptions()
    options.add_argument('--headless')
    ffprofile = webdriver.FirefoxProfile()
    ffprofile.set_preference("intl.accept_languages", "en-US")
    driver = webdriver.Firefox(firefox_profile=ffprofile, executable_path=Constants.FireFox_DRIVER_PATH,options=options)
    driver.implicitly_wait(100)
    driver.maximize_window()
    return driver