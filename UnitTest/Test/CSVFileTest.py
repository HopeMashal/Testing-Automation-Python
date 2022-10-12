import allure
from ddt import *
from unittest import TestCase

from Core.CSVFile import *

@ddt
class TestData(TestCase):
    @data((3, 2,3), (4, 3,3), (5, 3,5))
    @unpack
    def test_numbers(self, num1, num2, maxNum):
        self.assertEqual(maxNum, max(num1,num2))

    @data(*CSVFile.GetDataFromCSVFile("../Files/CSVFileTest.csv"))
    @unpack
    def test_data(self,num1,num2, num3):
        self.assertEqual(max(int(num1),int(num2)),int(num3))

    def setUp(self):
        allure.attach.file("../Files/CSVFileTest.csv","test_data.csv",attachment_type=allure.attachment_type.CSV)
        print("Setup")

    def tearDown(self) :
        print("Teardown")

    @classmethod
    def setUpClass(cls) :
        print("Setup class")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")