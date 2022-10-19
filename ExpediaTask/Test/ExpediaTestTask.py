import allure
from ddt import *
from unittest import TestCase

from ExpediaTask.Core.CSVFile import *
from ExpediaTask.Core.ConfigFile import *

@ddt
class ExpediaTestTask(TestCase):
    Headers = []
    OutputData = []
    BaseURL = ""
    ResultURL = ""
    ResultInfo = ""

    @data(*CSVFile.GetDataFromCSVFile("./ExpediaTask/Config/input.csv"))
    @unpack
    def testExpedia(self,hotelID,name,city,address):
        print("")

    def setUp(self):
        print("Before Test")

    def tearDown(self) :
        print("After Test")

    @classmethod
    def setUpClass(cls) :
        cls.BaseURL = ConfigFile.GetPropValue("./ExpediaTask/Config/prop.config", "server", "url")
        cls.ResultURL = ConfigFile.GetPropValue("./ExpediaTask/Config/prop.config", "searchResult", "url")
        cls.ResultInfo = ConfigFile.GetPropValue("./ExpediaTask/Config/prop.config", "searchResult", "info")
        cls.Headers = ["hotel_id","name","city","address"]
        allure.attach.file("./ExpediaTask/Config/input.csv","inputData.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./ExpediaTask/Config/output.csv","outputData.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./ExpediaTask/Config/prop.config","prop.config",attachment_type=allure.attachment_type.TEXT)
        print("Before class")

    @classmethod
    def tearDownClass(cls):
        print("After class")