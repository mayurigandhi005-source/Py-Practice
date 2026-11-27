# Q8: import grade.py module
import grade

# Q7: datetime module
from datetime import date

# Q10: threading module
import threading
import time


# Q1: Student class with constructor (Roll No, Name)
# Q2: Create object and display details
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def display(self):
        print("Roll No:", self.roll_no, "| Name:", self.name)


# Q3: Getter and Setter for Marks
# Q4: Calculate Grade using methods
# Q6: Handle invalid marks using Exception Handling
class MarksManager:
    def __init__(self):
        self._marks = 0

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks 0 between 100 ")
        self._marks = marks

    def calculate_grade(self):
        return grade.get_grade(self._marks)


# Q5: Department container class to store multiple students
class Department:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


# Q7: Use datetime module to store admission date
admission_date = date.today()


# Q9: Inheritance and override grade calculation method
class BaseGrade:
    def get_grade(self, marks):
        return grade.get_grade(marks)


class MeritGrade(BaseGrade):
    def get_grade(self, marks):
        if marks >= 85:
            return "A+ (Merit)"
        return grade.get_grade(marks)


# Q10: Create thread for report generation using sleep() and join()
def print_report():
    print("Report in process...")
    time.sleep(2)
    print("Report ready!")


# --- Execution ---
# Q1 & Q2
s1 = Student(1, "mayuri")
s1.display()

# Q3, Q4 & Q6
mm = MarksManager()
try:
    mm.set_marks(80)
    print("Marks:", mm.get_marks())
    print( "Grade:", mm.calculate_grade())
    mm.set_marks(150)  # invalid marks test
except ValueError as e:
    print("Error:", e)

# Q5
dept = Department()
dept.add_student(s1)
print("Department students count:", len(dept.students))

# Q7
print("Admission Date:", admission_date)

# Q9
mg = MeritGrade()
print("Merit Grade:", mg.get_grade(90))

# Q10
t = threading.Thread(target=print_report)
t.start()
t.join()
print("Program end..")