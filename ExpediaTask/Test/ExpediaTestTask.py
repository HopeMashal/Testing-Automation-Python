import allure
from ddt import *
from unittest import TestCase

from ExpediaTask.Core.CSVFile import *
from ExpediaTask.Core.ConfigFile import *
from ExpediaTask.Core.OpenBrowser import *
from ExpediaTask.Pages.BingSearchPage import *
from ExpediaTask.Pages.BingSearchResult import *

@ddt
class ExpediaTestTask(TestCase):
    Headers = []
    OutputData = []
    ResultURL = ""
    ResultInfo = ""
    MaxNumOfLinks = 0

    @data(*CSVFile.GetDataFromCSVFile("./ExpediaTask/Config/input.csv"))
    @unpack
    def testExpedia(self,hotelID,name,city,address):
        bingSearchPage = BingSearchPage()
        bingSearchPage.openBingPage(self.driver)
        bingSearchPage.search(self.driver,name + " " + city + " expedia")
        bingSearchResult = BingSearchResult()
        URLList = []
        counter = 0
        for index in range(len(bingSearchResult.getResults(self.driver))):
            resultHref = bingSearchResult.getResultHref(self.driver,index)
            if resultHref.startswith(self.ResultURL) and resultHref.endswith(self.ResultInfo):
                URLList.append(resultHref)
                counter += 1
        if counter > self.MaxNumOfLinks:
            self.MaxNumOfLinks = counter
        resultList = [hotelID,name,city,address]
        if counter == 0:
            resultList.append("Hotel NOT Found")
        else:
            resultList.extend(URLList)
        self.OutputData.append(resultList)

    def setUp(self):
        print("Before Test")

    def tearDown(self) :
        print("After Test")

    @classmethod
    def setUpClass(cls) :
        cls.driver = OpenBrowser.OpenChromeBrowser()
        cls.driver.maximize_window()
        cls.ResultURL = ConfigFile.GetPropValue("./ExpediaTask/Config/prop.config", "searchResult", "url")
        cls.ResultInfo = ConfigFile.GetPropValue("./ExpediaTask/Config/prop.config", "searchResult", "info")
        cls.Headers = ["hotel_id","name","city","address"]
        allure.attach.file("./ExpediaTask/Config/input.csv","inputData.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./ExpediaTask/Config/output.csv","outputData.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./ExpediaTask/Config/prop.config","prop.config",attachment_type=allure.attachment_type.TEXT)
        print("Before class")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        if cls.MaxNumOfLinks > 0:
            for i in range(cls.MaxNumOfLinks):
                cls.Headers.append("Link_" + (i + 1))
        CSVFile.WriteCSVFile("./ExpediaTask/Config/output.csv",cls.Headers,cls.OutputData)
        print("After class")