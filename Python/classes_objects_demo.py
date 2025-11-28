# Initial explaination for class and object creation

class Student:
    # class variable
    school_name = "CDAC"    

    # initialiser
    def __init__(self,rcv_name,rcv_rollno,rcv_pocket_money,rcv_course):
        # instance variable
        self.student_name = rcv_name      # public instance variable 
        self.student_rollno = rcv_rollno   # public instance variable 
        self.student_pocket_money = rcv_pocket_money # public instance variable 
        self.student_enrolled_coursename = rcv_course # public instance variable 
        self.student_bank_balance = set([298738,902803,72637,5625,565]).pop()
        print(f"{self} was created successfully with values {rcv_name},{rcv_rollno},{rcv_pocket_money},{rcv_course}")

    #instance_method
    def display_details_of_students(self):
        print(f"{self} with values {self.student_name},{self.student_rollno},{self.student_pocket_money},{self.student_enrolled_coursename}")


    # instance method
    def get_enrolled_course(self):
        return self.student_enrolled_coursename

    # instance method
    def get_student_pocket_money(self):
        return self.student_pocket_money
    
    # instance method
    def enroll(self,rcv_course_name):
        self.student_enrolled_coursename = rcv_course_name

    # instance method
    def unenroll(self):
        self.student_enrolled_coursename = None
        
    # instance method
    def get_student_bank_balance(self):
        return self.student_bank_balance

    # class method
    @classmethod
    def change_schoolname(cls,rcv_schoolname):
        cls.school_name = rcv_schoolname
    
    # static method
    @staticmethod
    def display_facilities_available():
        print("Facilities are 1) Gym ---- 2)Library ---- 3)TT\n")
    
    def __del__(self):
    # body of destructor   
        print(f"I am in destructor for ")
        self.display_details_of_students()

# main method which is outside the class 
def main():
    print("I am in main and I am not part of the class ")

    # create a Student object referenced by gaurav
    gaurav= Student("Gaurav",1,100,'Python')
    pratik= Student("Pratik",2,200,'Scala')
    
    print("Before Unenroll call ", gaurav.get_enrolled_course())
    # invoke a instance method(setter) for gaurav referenced object to set an attribute of the class 
    gaurav.unenroll()
    print("After Unenroll call ", gaurav.get_enrolled_course())
    # invoke a instance method for gaurav referenced object 
    gaurav.enroll("Scala")
    print("After Enroll call ", gaurav.get_enrolled_course())
    
    
      # print the class variable 
    print("School name at Class level is",Student.school_name)
    print("Gaurav School name is",gaurav.school_name)
    print("Pratik School name is",pratik.school_name)

    # invoke class method(setter) using gaurav instance variable reference
    gaurav.change_schoolname("Sunbeam1")

    # print the class variable 
    print("School name at Class level is",Student.school_name)
    print("Gaurav School name is",gaurav.school_name)
    print("Pratik School name is",pratik.school_name)
    
    # invoke the static method 
    Student.display_facilities_available()
    gaurav.display_facilities_available()
    pratik.display_facilities_available()
    #display_facilities_available() # doesnot work 
# invoke the main function 


# main()

if __name__ == '__main__':
    main()


