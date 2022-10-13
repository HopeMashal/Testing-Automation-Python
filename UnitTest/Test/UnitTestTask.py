# cd UnitTest/Test >> pytest .\UnitTestTask.py --alluredir=..\allure-results

from unittest import TestCase


class UnitTestTask(TestCase):
  @classmethod
  def setUpClass(cls):
    print("Before Class")

  @classmethod
  def tearDownClass(cls):
    print("After Class")

  def setUp(self):
    print("Before Test")

  def tearDown(self):
    print("After Test")

  def testA(self):
    self.assertEqual(2,3)

  def testB(self):
    self.assertIn("o","Hope")

  def testC(self):
    self.assertTrue(False)

  def testD(self):
    self.assertFalse(True)

  def testE(self):
    self.assertGreater(4,6,"Wrong!!")