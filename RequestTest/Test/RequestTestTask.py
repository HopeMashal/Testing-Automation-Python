import allure
from ddt import *
from unittest import TestCase
import requests

from RequestTest.Core.CSVFile import *
from RequestTest.Core.JSONFile import JSONFile

@ddt
class RequestTestTask(TestCase):
    @data(*CSVFile.GetDataFromCSVFile("./RequestTest/Files/inputGet.csv"))
    @unpack
    def testGetMethod(self,Routes,Status):
        r = requests.get('https://jsonplaceholder.typicode.com'+Routes)
        self.assertEqual(int(Status),r.status_code,"Status NOT Equals")

    @data(*JSONFile.ReadJSON("./RequestTest/Files/inputDelete.json"))
    @unpack
    def testDeleteMethod(self,body,url,expectedStatusCode,expectedResponseBody):
        r = requests.delete('https://jsonplaceholder.typicode.com'+url , data=json.dumps(body))
        self.assertEqual(int(expectedStatusCode),r.status_code,"Status NOT Equals")
        if(r.status_code < 500):
            self.assertEqual(expectedResponseBody,r.json())
            print(r.json())
            print(expectedResponseBody)

    @data(*JSONFile.ReadJSON("./RequestTest/Files/inputPut.json"))
    @unpack
    def testPutMethod(self,body,url,expectedStatusCode,expectedResponseBody):
        r = requests.put('https://jsonplaceholder.typicode.com'+url , data=json.dumps(body), headers={"Content-Type": "application/json"})
        self.assertEqual(int(expectedStatusCode),r.status_code,"Status NOT Equals")
        if(r.status_code < 500):
            self.assertEqual(expectedResponseBody,r.json())
            print(r.json())
            print(expectedResponseBody)

    @data(*JSONFile.ReadJSON("./RequestTest/Files/inputPost.json"))
    @unpack
    def testPostMethod(self,body,url,expectedStatusCode,expectedResponseBody):
        r = requests.post('https://jsonplaceholder.typicode.com'+url , data=json.dumps(body), headers={"Content-Type": "application/json"})
        self.assertEqual(int(expectedStatusCode),r.status_code,"Status NOT Equals")
        if(r.status_code < 500):
            self.assertEqual(expectedResponseBody,r.json())
            print(r.json())
            print(expectedResponseBody)

    def setUp(self):
        print("Before Test")

    def tearDown(self) :
        print("After Test")

    @classmethod
    def setUpClass(cls) :
        allure.attach.file("./RequestTest/Files/inputGet.csv","testGetMethod.csv",attachment_type=allure.attachment_type.CSV)
        allure.attach.file("./RequestTest/Files/inputDelete.json","testDeleteMethod.json",attachment_type=allure.attachment_type.JSON)
        allure.attach.file("./RequestTest/Files/inputPut.json","testPutMethod.json",attachment_type=allure.attachment_type.JSON)
        allure.attach.file("./RequestTest/Files/inputPost.json","testPostMethod.json",attachment_type=allure.attachment_type.JSON)
        print("Before class")

    @classmethod
    def tearDownClass(cls):
        print("After class")