import grade  # Q8: import custom grade.py module
from datetime import date  # Q7: import date class to get today's date
import threading  # Q10: import threading module to create a thread
import time   # Q10: import time module to use sleep()

# Q1: Student class with constructor (Roll No, Name)
class Student:
    def __init__(self,roll_no,name): # constructor: sets roll_no and name when object is created
        self.roll_no = roll_no  # store roll_no in the object
        self.name = name   # store name in the object

# Q2: display student details        
    def display(self): # method to print student details
        print("roll no",self.roll_no)  # print roll_no
        print("name",self.name)  # print name

s1 = Student(1,"mayuri") # create object s1 of Student class
s1.display()   

# Q3, Q4 & Q6: Marks getter/setter, grade calculation, and exception handling
class setMarks:
    def __init__(self): # constructor: initialize marks to 0
        self.marks=0  # default marks value(encapsulated data)
    def get_marks(self): # Q3: getter method to return current marks
        return self.marks # return stored marks

    def set_marks(self,marks):
        if marks < 0 or marks > 100:
            raise ValueError ("marks  between 0 and 100")  
        self.marks = marks

    def calculate_grade(self):
        return grade.get_grade(self.marks)

s2= setMarks()
try:
    s2.set_marks(80)
    print("marks",s2.get_marks())
    print("grade",s2.calculate_grade())
    s2.set_marks(15)
except ValueError as e:
    print("error",e)              

class Department:
    def __init__(self):
        self.students = []

    def add_stu(self,student):
        self.students.append(student) 

dept = Department()
dept.add_stu(s1)
print("student count",len(dept.students))   

admission_date = date.today()
print("Admission Date",admission_date)

class bgrade:
    def get_grade(self,marks):
        return grade.get_grade(marks)

class mgrade(bgrade):
    def get_grade(self,marks):
        if marks >= 85 :
            return "A+"
        return grade.get_grade(marks)
mg=mgrade()
print("grade",mg.get_grade(90))   

def report():
    print("report in process")
    time.sleep(2)
    print("report ready")

t = threading.Thread(target=report)
t.start()
t.join()
print("program end")    

