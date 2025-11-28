# Create a class that captures students. 
#Each student has a first name, last name, class year, and major. Create two examples of students.

class Student:
    
    def __init__ (self,first_name, last_name, class_year, major):
        self.first_name =first_name
        self.last_name=last_name
        self.class_year= class_year
        self.major=major
    
    def get_fname(self):
        return self.first_name
    
    def get_lname(self):
        return self.last_name
    
    def get_classyear(self):
        return self.class_year
    
    def get_major(self):
        return self.major
    
def main ():
       s1 = Student("Tilak","shelke","iacsd-sept23","dac")
       s2 = Student("Tilak1","shelke1","acts-sept25","ccst")
       
       print(f"first_name:{s1.first_name},second_name:{s1.last_name},class_year:{s1.class_year},major:{s1.major}")
       print(f"first_name:{s2.first_name},second_name:{s2.last_name},class_year:{s2.class_year},major:{s2.major}")
        
        
if __name__ =='__main__':
 main()
        