from unittest import TestCase
from pandas import read_csv
from app.io.input import file_read, pd_read


class TestInputFile(TestCase):

    def test_empty(self):
        self.assertEquals(file_read("../../data/empty.txt"), "", "Should be empty")

    def test_absent(self):
        self.assertEquals(file_read("../../data/absent.txt"), "Error", "There has to be error")

    def test_usual(self):
        with open("../../data/test.txt") as file:
            data = file.read()
        self.assertEquals(file_read("../../data/test.txt"), data, "Should work correctly")


class TestInputPandas(TestCase):

    def test_empty(self):
        self.assertEquals(pd_read("../../data/empty.csv"), "Empty file", "Should be empty")

    def test_absent(self):
        self.assertEquals(pd_read("../../data/absent.csv"), "Error", "There has to be error")

    def test_usual(self):
        data = read_csv("../../data/simple.csv")
        self.assertEquals(str(pd_read("../../data/simple.csv")), str(data), "Should work correctly")
