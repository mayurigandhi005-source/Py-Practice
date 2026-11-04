def student_marks(**kwargs):
    name =kwargs['name']
    marks =kwargs['marks']
    if marks >= 40:
        print(name,"passed")
    else:
        print(name,"fail")
student_marks(name='mayuri',marks=80)  
student_marks(name='amam',marks=35)  
