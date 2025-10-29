#  Create a Student class with following 

# 	a) instance variables 
# 	   Name,Rollno,Subject
# 	b) Instance Methods
# 	   get_subject
# 	   set_subject -- sets a subject for the particular instance
# 	c) Class variables 
# 	   school_name 
# 	d) Class methods
# 		get_school_name
# 		set_school_name -- sets a school name for the class 
# 	e) static methods
# 		display_prerequiste_skills --> displays some skills for all students in general good to have ones

# 	Main Method:
# 		Create two student objects
# 		display subject names for each of the above created objects
# 		set a new subject name for each of the above created objects 	
# 		display subject names again after updating for each of the above created objects

# 		display the class variable 
# 		update the class variable using set_school_name method
# 		display the class variable 
# 		update the class variable using class_name. notation
# 		display the class variable 
# 		update the class variable using object_name. notation
# 		display the class variable 
# 		display the object variable with the same name as class variable for the object you selected on line27

# 		delete the school_name instance variable for the object you selected on line27
# 		display the object variable with the same name as class variable for the object you selected on line27

# 		delete the the object you selected on line27
# 		display the rollno for the object you selected on line27

# 		delete the school_name for the class
# 		display the class variable 
	

# 1) Create a class that captures students. 
# 	Each student has a first name, last name, class year, and major. Create two examples of students.

# 2) Create a class that captures planets. 
# 	Each planet has a name, a distance from the sun, and its gravity relative to Earth’s gravity. For distance and gravity, use the type double which captures real numbers. Make objects for Earth and your favorite non-earth planet.

# 3) Create classes that capture bank customers and bank accounts.
# 	A customer has a first and last name. An account has a customer and a balance. Make objects for two accounts held by the same customer.

# 4) Create a class that captures airline tickets. 
# 	Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. A seat assignment has both a row and a letter for the seat within the row (such as 12F). Make two examples of tickets.

# 5) Refer provided classesAndObjectsPractice.docx for problems on class and objects 



class Student:
    
    #class level 
    school_name ="Cdac-Acts"
    
    #constrcutor 
    def __init__(self,name,rollno,subject ):
        self.name= name
        self.rollno = rollno
        self.subject = subject
        
        #instance method :
    def get_subject(self):
        return self.subject
        
        #instance method 
    def set_subject(self,new_subject):
        self.subject = new_subject
            
            

  #class level method
    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @classmethod
    def set_school_name(cls,new_school_name):
        cls.school_name= new_school_name
    
    @staticmethod
    def display_prerequire_skills():
        print("Skills: Basic Math, Reading, Teamwork, Computer Use\n")    
    
    
def main():
    s1= Student("tILAK",23,"SCIENCE")
    s2= Student("tILAK1",24,"HISRTORY")
    
    print(F"{s1.name} SUBJECT {s1.get_subject()}")
    print(F"{s2.name} subject {s2.get_subject()}")
    
    # pass the dtaa to the functions 
    s1.set_subject("Maths")
    s2.set_subject("Geography")
    
 # update the value 
    print(F"{s2.name} SUBJECT {s1.get_subject()}")
    print(F"{s2.name} subject {s2.get_subject()}")
    
    # print the class level methOD NAME 
    
    print("CLASS level school name ",Student.get_school_name())
    
    # set the class level method name by setter method 
    Student.set_school_name("Iacsd_Pune")
    print("set the data ",Student.get_school_name())
    
    #you can directly update the class level variable 
    Student.school_name="sunbeam_Pune"
    print("set the data ",Student.get_school_name())

    # you can set the class level varaiable by object 
    s1.school_name=" Infoway_Pune "

    print("instance _variable ",s1.school_name)
    
    s2.school_name=" Sunbeam Marketyard"
    print("instance_varaiable ",s2.school_name)
    
    #print by class name
    print("Student.school_name",Student.school_name)
    
    # deleting the instance
    
    #del s1.school_name
    
    #check # deleting the instance or not 
    print("check",s1.school_name)
    
    # it give error bcoz its instance already delete 
    #del s1 
    
    # it gives error bcoz its already deleted 
   #0 del Student.school_name

   
if __name__ == '__main__':
    main()    
    