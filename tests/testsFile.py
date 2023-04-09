import datetime
from myapp import Course, Assignment, print_courses

def test_add_course():
    courses = []
    courses.append(Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2022, 12, 10)))
    assert len(courses) == 1
    assert courses[0].name == "Math"
    assert courses[0].start_date == datetime.datetime(2022, 9, 1)
    assert courses[0].end_date == datetime.datetime(2022, 12, 10)
    assert len(courses[0].assignments) == 0

def test_add_assignment():
    courses = []
    courses.append(Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2022, 12, 10)))
    courses[0].add_assignment(Assignment("Homework 1", datetime.datetime(2022, 9, 15)))
    assert len(courses[0].assignments) == 1
    assert courses[0].assignments[0].name == "Homework 1"
    assert courses[0].assignments[0].due_date == datetime.datetime(2022, 9, 15)
    assert not courses[0].assignments[0].completed

def test_mark_assignment_completed():
    courses = []
    courses.append(Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2022, 12, 10)))
    courses[0].add_assignment(Assignment("Homework 1", datetime.datetime(2022, 9, 15)))
    courses[0].assignments[0].mark_completed()
    assert courses[0].assignments[0].completed

def test_print_courses():
    courses = []
    courses.append(Course("Math", datetime.datetime(2022, 9, 1), datetime.datetime(2022, 12, 10)))
    courses[0].add_assignment(Assignment("Homework 1", datetime.datetime(2022, 9, 15)))
    expected_output = "1. Math (09/01/2022 - 12/10/2022)\n   1. Homework 1 (due 09/15/2022, Incomplete)\n"
    assert print_courses(courses) == expected_output

def test_invalid_choice():
    courses = []
    assert main(courses, "6") == "Invalid choice. Please try again.\n"

