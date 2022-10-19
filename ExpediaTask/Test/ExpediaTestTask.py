import allure
from ddt import *
from unittest import TestCase

from ExpediaTask.Core.CSVFile import *

@ddt
class ExpediaTestTask(TestCase):
    @data(*CSVFile.GetDataFromCSVFile("./ExpediaTask/Config/input.csv"))
    @unpack
    def testExpedia(self):
        print("")

    def setUp(self):
        print("Before Test")

    def tearDown(self) :
        print("After Test")

    @classmethod
    def setUpClass(cls) :
        allure.attach.file("./ExpediaTask/Config/input.csv","inputData.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./ExpediaTask/Config/output.csv","outputData.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./ExpediaTask/Config/prop.config","prop.config",attachment_type=allure.attachment_type.TEXT)
        print("Before class")

    @classmethod
    def tearDownClass(cls):
        print("After class")