import unittest
from error_handling_summary.config_provider import ConfigProvider
from error_handling_summary.error_handling import ErrorHandling

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # ARRANGE
        self.config = ConfigProvider.load_from_file(r'C:\Users\nraba\PycharmProjects\Tzahi Lessons\5Tech_AutomationBootcamp\error_handling_summary\config.json')

    def test_write_file(self):
        # ACT
        ErrorHandling.write_file(self.config["file_path"], self.config["content"])
        # ASSERT
        self.assertTrue(self.config["file_path"])

    def test_content_of_writing_file(self):
        # ACT
        ErrorHandling.write_file(self.config["file_path"], self.config["content"])
        with open(self.config["file_path"], "r") as file:
            check = file.read()
        # ASSERT
        self.assertEqual(check, self.config["content"])

    def test_read_file(self):
        # ARRANGE
        ErrorHandling.write_file(self.config["file_path_for_read"], self.config["file_path_for_read_content"])
        # ACT
        content = ErrorHandling.read_file(self.config["file_path_for_read"])
        # ASSERT
        self.assertEqual(content, self.config["file_path_for_read_content"])

if __name__ == '__main__':
    unittest.main()