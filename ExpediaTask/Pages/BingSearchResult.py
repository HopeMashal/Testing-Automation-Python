from selenium.webdriver.common.by import By


class BingSearchResult:
  @staticmethod
  def getResults(driver):
    return driver.find_elements(By.XPATH,"//*[@id=\"b_results\"]//*/h2/a")

  @staticmethod
  def getResultHref(driver,index):
    results_list = BingSearchResult.getResults(driver)
    return results_list[index].get_attribute("href")