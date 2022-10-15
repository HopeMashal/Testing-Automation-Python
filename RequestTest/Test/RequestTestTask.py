import allure
from ddt import *
from unittest import TestCase
import requests

from RequestTest.Core.CSVFile import *

@ddt
class RequestTestTask(TestCase):
    @data(*CSVFile.GetDataFromCSVFile("./RequestTest/Files/input.csv"))
    @unpack
    def test_data(self,Routes,Status):
        r = requests.get('https://jsonplaceholder.typicode.com'+Routes)
        print(r.status_code)
        self.assertEqual(int(Status),r.status_code,"Status NOT Equals")

    def setUp(self):
        print("Setup")

    def tearDown(self) :
        print("Teardown")

    @classmethod
    def setUpClass(cls) :
        allure.attach.file("./RequestTest/Files/input.csv","test_data.csv",attachment_type=allure.attachment_type.CSV)
        print("Setup class")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")