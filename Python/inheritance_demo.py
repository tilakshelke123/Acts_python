from  classes_objects_demo import Student

""" Single Inheritance with nothing in the new child class """
class CCST_student(Student):
    def __init__(self, rcv_name, rcv_rollno, rcv_pocket_money, rcv_course):
         super().__init__(rcv_name, rcv_rollno, rcv_pocket_money, rcv_course)
         self.special_powers = ['Flying']
    
    # instance method ( Overriding)
    def unenroll(self):
        self.student_enrolled_coursename = 'TESTING'
        
    # instance method )( additional functionality)
    def display_special_powers(self)    :
        print(self.special_powers)
        
    # # instance method )( additional functionality with overload)
    # def display_special_powers(self, Free_power )    :
    #     print(self.special_powers,Free_power)  

Hrithik = CCST_student("Hrithik",3,300,"CCST")
print(Hrithik.get_student_pocket_money())

print(Hrithik.get_enrolled_course())
Hrithik.unenroll()
print(Hrithik.get_enrolled_course())
Hrithik.display_special_powers()