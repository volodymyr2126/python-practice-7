from unittest import TestCase
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
