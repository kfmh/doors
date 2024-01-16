import json
import unittest
import os
from importlib import resources  # Use importlib.resources for Python 3.7+

from src.doors.file_manager import FileManager

fpm = FileManager()

class JsonFormatTests:

    # First test if lods jsons
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
        file_paths = fpm.filepath_list(
            directory = '/courses/',
            exclude_files = ['README.md'])

        for f in file_paths:
            with open(f, 'r') as file:
                file_content = file.read()
            self.assertTrue(JsonFormatTests().is_json(file_content))
        
    

if __name__ == '__main__':
    unittest.main()
