# multiple  a, b-c

#MRO - ---> METHOD RESOULATION ORDER

'''class A:
    def display(self):
        print("a.display")
class B:
    def display1(self):
        print("B.display")
class C(A,B):
    pass

c = C()
c.display()'''


#hybrid = = single + multiple 
# C-A-B-A
# C-B-A
#C-B-A

'''class A:
    def display(self):
        print("a.display")
class B(A):
    def display1(self):
        print("B.display")
class C(B,A):
    pass

c = C()
c.display()
'''
#-----------------------------------

'''class A:
    def display(self):
        print("a.display")
class B(A):
    def display1(self):
        print("B.display")
class D(B):
    pass
class C(D,B,A):
    pass

c = C()
c.display()'''

# ----------------------------------------------------------
class Uni:
    def __init__(self):
        self.uni_name = "apollo clg"
        # print("university-name init= " ,self.uni_name)
    def display(self,new):
        self.uni_name = new
        print("university-name = " ,self.uni_name)
class Branch(Uni):
    def __init__(self):
        super().__init__()
        self.Branch_name = "Bechelor of engineering"
        # print("branch name init= ",self.Branch_name)
    def dispaly(self,new):
        self.Branch_name = new
        print("branch name = ",self.Branch_name)
class Course(Branch):
    def __init__(self):
        super().__init__()
        self.course_name = "infromation technology"
        # print("course - name init= ",self.course_name)
    def dispaly(self,new):
        self.course_name = new
        print("course - name = ",self.course_name)
class Student(Course,Branch):
    def __init__(self):
        super().__init__()
        self.std_name = "Ankit patel"
        self.std_rollno = 26
        self.std_marks = 77
    def dispaly(self,new,new1):
        self.std_name = new
        self.std_marks = new1
        print("student_name = ",self.std_name)
        print("student_rollno = ",self.std_rollno)
        print("student_marks = ",self.std_marks)
        print("university-name = " ,self.uni_name)
        print("Branch _name = ",self.Branch_name)
        print("course_name = ",self.course_name)



# student = Student()
# student.dispaly()

print("------------------------update infromation----------------------")
print("\1 for University --->")
print("\2 for Branch --->")
print("\3 for Course --->")
print("\4 for Student --->")
choice = int(input("enter the numebr = "))
if(choice == 1):
    uni =Uni()
    uni.display(input("enter the university name ---> "))
elif(choice == 2):
    bra = Branch()
    bra.dispaly(input("enter the branch name ---> "))
elif(choice == 3):
    cour = Course()
    cour.dispaly(input("enter the course name --->"))
elif(choice == 4):
    std = Student()
    std.dispaly(input("enter the student--name --->"),input("enter the student-- marks -->"))

else:
    print("please select number----->")





