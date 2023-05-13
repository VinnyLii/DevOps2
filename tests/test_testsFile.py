import datetime
import unittest

from main import Course, Assignment, print_courses


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
        expected_output = '1. DevOps2'
        self.assertEqual(print_courses(courses), expected_output)

if __name__ == '__main__':
    unittest.main()
