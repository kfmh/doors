import unittest
# from ..src.doors.mcq_courses import mcq_process
import json
import os
import pkg_resources

class PrepareTest:
    def __init__(self, 
                 directory="../src/doors/mcq_courses/",
                 exclude_file=['README.md','mcq_template.json']):
        self.directory = pkg_resources.resource_filename(__name__,directory)
        self.exclude_file = exclude_file
        self.files = [f for f in os.listdir(self.directory) 
                      if os.path.isfile(os.path.join(self.directory, f)) 
                      and f not in exclude_file]
        
    def mcq_course_name(self, f, json_content):
        js = next(iter(json_content))

        if js != f[:-5]:
            error_message = (
                '<-+-+-+-+->\n'
                'Courses name key does not match file name \n'
                f'file name:{f}\n'
                f'course name:{js}\n'
                '<-+-+-+-+->'
            )
            return False, f, error_message
        else:
            return True, f, 'Check cleard'


    def mcq_indexing(self, f, json_content):
        index_list = list(json_content[f[:-5]].keys())
        error_message = (
            '<-+-+-+-+->\n'
            'Course question indexing is formatted wrong, \n'
            f'current index: {index_list}\n'
            'correct indexing: ["0", "1", "2", ...]\n'
            '<-+-+-+-+->'
        )


        for i, jsindex in enumerate(index_list):
            try: 
                if i != int(jsindex):
                    print(error_message)
                    return False, f, error_message
                else:
                    return True, f, 'Check cleard'
            except ValueError:
                print(error_message)


    def mcq_questions_keys(self, f, json_content):
        course_content = json_content[f[:-5]]
        key_strings = list(course_content.keys())
        correct_mcq_keys = ['question', 'explanation', 'wrong_1', 'wrong_2', 'correct']
        for i in key_strings:
            if list(course_content[i].keys()) != correct_mcq_keys:
                error_message = (
                    '<-+-+-+-+->\n'
                    f'Course mcq keys are inncorect on index {i} \n'
                    f'current keys: {list(course_content[i].keys())} \n'
                    f'correct keys: {correct_mcq_keys}\n'
                    '<-+-+-+-+->'
                )
                print(error_message)
                return False, f, error_message

        return True, f, 'Check cleared'

            
    def mcq_questions(self, f, json_content):
        course_content = json_content[f[:-5]]
        key_strings = list(course_content.keys())
        mcq_keys = ['question', 'explanation', 
                    'wrong_1', 'wrong_2', 'correct']

        for i in key_strings:
            q = course_content[i]
            for k in mcq_keys:
                if type(q[k]) != str:
                    error_message = (
                       '<-+-+-+-+->\n'
                       f'Incorrect datatype, all MCQ values must be strings {i} \n'
                       f'Error at: (key:{k}, value:{q[k]}, typ:{type(q[k])})\n'
                       '<-+-+-+-+->'
                    )   
                    return False, f, error_message
                else:
                    pass

        return True, f, 'Check cleard'

        
    def test_jsonformat(self):
        checks = 0
        for f in self.files:
            print(f)
            with open(f'{self.directory}{f}') as file:
                json_content = json.load(file)
            # Chech if course name key matches file name
            correct, file, msg = self.mcq_course_name(f, json_content)

            # ================================================
            # Todo: make into loop instead of neste if
            if correct:
                # Chech if course name key matches file name
                correct, file, msg = self.mcq_indexing(f, json_content)
                if correct:
                    correct, file, msg = self.mcq_questions_keys(f, json_content)
                    if correct:
                        last_check, file, msg = self.mcq_questions(f, json_content)
                        if last_check:
                            checks += 1
            # Todo: make into loop
            # ================================================
        if checks == len(self.files):
            return True
        else: False



p = PrepareTest()
class Test_jsonformat(unittest.TestCase):

    def test_check_format(self):
        self.assertEqual(p.test_jsonformat(), True)

if __name__ == '__main__':
    unittest.main()
