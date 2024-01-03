# Guide for Adding Courses

1. From the terminal, create a directory:
    ```bash
    mkdir <directory_name>
    cd <directory_name>
    git clone https://github.com/kfmh/doors.git
    cd doors/src/doors/mcq_courses
    ```

2. Make a new copy of `mcq_template.json` and name it `<course_name>.json`.
3. Add each multiple-choice question as a new sub-dictionary in `<course_name>.json`. For example:

    ```json
    {
        "cool_quotes": {
            "0": {
                "question": "What is the meaning of life?",
                "explanation": "The meaning of life as a reference to 'The Hitchhiker's Guide to the Galaxy'",
                "wrong_1": "Burgers",
                "wrong_2": "Pizza",
                "correct": "42"
            },
            "1": {
                "question": "What is the mind killer?",
                "explanation": "The a reference to 'Dune'",
                "wrong_1": "Doubt",
                "wrong_2": "Alcohol",
                "correct": "Fear"
            }
        }   
    }
    ```

4. Navigate back to the root directory and install:
    ```bash
    pip install .
    ```

# Contribute a Course to the Doors Project

To contribute your course, add the new course in a branch and create a pull request (PR).
