import datetime
import unittest

class Course:
    def __init__(self, name, start_date, end_date, Course_code):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.Course_code = Course_code
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

class Assignment:
    def __init__(self, name, due_date, day_frame):
        self.name = name
        self.due_date = due_date
        self.day_frame = day_frame
        self.completed = False
      
    def mark_completed(self):
        self.completed = True
        
def print_courses(courses):
    output = ''
    for i, course in enumerate(courses):
        output += '{}. {} [{}]'.format(i+1, course.name, course.Course_code)
        if course.start_date and course.end_date:
            output += ' ({} - {})'.format(course.start_date.strftime('%m/%d/%Y'), course.end_date.strftime('%m/%d/%Y'))
        output += '\n'
    return output.strip()

class TestCourseAndAssignment(unittest.TestCase):
    
    def setUp(self):
        self.course = Course('DevOps2', datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=30), 'DEVOPS2-101')
        self.assignment = Assignment('test assignment', datetime.datetime.now() + datetime.timedelta(days=10), '3 days')
    
    def test_course_has_name(self):
        self.assertEqual(self.course.name, 'DevOps2')
        
    def test_course_has_code(self):
        self.assertEqual(self.course.Course_code, 'DEVOPS2-101')
        
    def test_assignment_has_name(self):
        self.assertEqual(self.assignment.name, 'test assignment')
        
    def test_assignment_mark_completed(self):
        self.assertFalse(self.assignment.completed)
        self.assignment.mark_completed()
        self.assertTrue(self.assignment.completed)
        
    def test_print_courses(self):
        courses = [self.course]
        expected_output = '1. DevOps2 [DEVOPS2-101] ({} - {})\n'.format(datetime.datetime.now().strftime('%m/%d/%Y'), (datetime.datetime.now() + datetime.timedelta(days=30)).strftime('%m/%d/%Y'))
        self.assertEqual(print_courses(courses), expected_output)
        print(print_courses(courses))

if __name__ == '__main__':
    unittest.main()
