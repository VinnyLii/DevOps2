import datetime

class Course:
    def __init__(self, name, start_date, end_date, Course_code):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.assignments = []

    def add_assignment(self, assignment, trimester):
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
        output += '{}. {}'.format(i+1, course.name)
        output += '\n'
    return output.strip()

def main():
    courses = []
    while True:
        print("\n1. Add course\n2. Add assignment\n3. Mark assignment as completed\n4. View courses and assignments\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the name of the course: ")
            start_date = input("Enter the start date of the course (MM/DD/YYYY): ")
            end_date = input("Enter the end date of the course (MM/DD/YYYY): ")
            courses.append(Course(name, datetime.datetime.strptime(start_date, '%m/%d/%Y'), datetime.datetime.strptime(end_date, '%m/%d/%Y')))
            print("Course added successfully!")
        elif choice == "2":
            course_index = int(input("Enter the number of the course to add the assignment to: ")) - 1
            name = input("Enter the name of the assignment: ")
            due_date = input("Enter the due date of the assignment (MM/DD/YYYY): ")
            courses[course_index].add_assignment(Assignment(name, datetime.datetime.strptime(due_date, '%m/%d/%Y')))
            print("Assignment added successfully!")
        elif choice == "3":
            course_index = int(input("Enter the number of the course that the assignment is in: ")) - 1
            assignment_index = int(input("Enter the number of the assignment to mark as completed: ")) - 1
            courses[course_index].assignments[assignment_index].mark_completed()
            print("Assignment marked as completed!")
        elif choice == "4":
            print_courses(courses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
