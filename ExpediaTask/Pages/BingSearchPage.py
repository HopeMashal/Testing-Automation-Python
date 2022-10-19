from selenium.webdriver.common.by import By


class BingSearchPage:
  @staticmethod
  def openBingPage(driver):
    driver.get("https://www.bing.com/")

  @staticmethod
  def getSearchBox(driver):
    return driver.find_element(By.NAME, "q")

  def search(self, driver, searchText):
    search_box = BingSearchPage.getSearchBox(driver)
    search_box.send_keys(searchText)
    search_box.submit()