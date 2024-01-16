import json
import unittest


# First test if lods jsons
def is_json(document):
    try:
        json.loads(document)
        return True
    except json.JSONDecodeError:
        return False




class Test_jsonformat(unittest.TestCase):
    # First test if lods jsons
    def test_is_json(self):
        self.assertTrue(is_json(), True)

if __name__ == '__main__':
    unittest.main()