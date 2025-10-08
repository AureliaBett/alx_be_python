class Student:
    def __init__(self, name, age, adm, year, grade):
        self.name = name
        self.age = age
        self.adm = adm
        self.year = year
        self.grade = grade
    def student_Info(self):
        student_Details = f"Name:  {self.name}\nAge: {self.age}\nADM No: {self.adm}\nYear: {self.year}"
        return student_Details
    def student_Grade(self):
        grade_Attained = f"The student scored {self.grade}"
        print(grade_Attained)
        return grade_Attained
    
    def fail_or_Pass(self, pass_Mark):
        if pass_Mark >= self.grade:
            print("Fail. You need to retake the test")
        elif pass_Mark < self.grade:
            print ("Pass. You can proceed to the next class")
        else:
            print("No grade was assigned")     


student_list = Student("Maureen Haile", "20", "EEI/9999", "2017", 90 )
print(student_list.student_Info())
student_list.student_Grade()
student_list.fail_or_Pass(70)


    