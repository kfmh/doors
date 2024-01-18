import json
import unittest
from src.doors.file_manager import FileManager

fpm = FileManager()

class JsonFormatTests:

    # First test if lods jsons
    @staticmethod
    def is_json(document):
        try:
            json.loads(document)
            return True
        except json.JSONDecodeError as e:
            print(e)
            return False


class Testjsonformat(unittest.TestCase):
    # First test if lods jsons
    def test_is_json(self):
        """Test all that all files are json and can be loades 
        files in courses directory"""
        json_format_tests = JsonFormatTests()

        file_paths = fpm.filepath_list(
            directory = '/courses/',
            exclude_files = ['README.md'])

        for f in file_paths:
            with open(f, 'r') as file:
                file_content = file.read()
            # print(file_content)
            self.assertTrue(json_format_tests.is_json(file_content))
        
    

if __name__ == '__main__':
    unittest.main()
