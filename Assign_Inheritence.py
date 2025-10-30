# ---------------------------------------
# 1) Create a Student class with following 

# 	a) instance variables 
# 	   Name,Rollno(private),Subject (Protected)
# 	b) Instance Methods
# 	   get_subject 
# 	   set_subject -- sets a subject for the particular instance
	   
# 	   get_rollno
# 	   set_rollno -- sets a rollno for the particular instance

# 	   display_student_details -- > prints the name,rollno,subject 
# 	   get_primary_skill --> prints the primary skill
# 	   set_primary_skill --> sets the primary skill
	   
# 	Create a subclass named DBDA_student with following 
# 	a) instance variables 
# 	   Name,Rollno(private),Subject(protected), primary_skill,secondary_Skills(an array of other skills other than primary skill)
# 	b) Instance Methods
# 	   get_subject
# 	   set_subject -- sets a subject for the particular instance

# 	   get_rollno
# 	   set_rollno -- sets a rollno for the particular instance

# 	   display_student_details -- > prints the name,rollno,subject,primary_skill,secondary_skills
	   
# 	   Override the set_primary_skill method to always have SQL as primary skill
	   

# 	Main Method:
# 		Create two DBDA student objects for ex: Student1,Student2
# 		display subject names for each of the above created objects
		
# 		display rollno for each of the above created objects
# 		set a new subject name for each of the above created objects 	
# 		display subject names again after updating for each of the above created objects
		
# 		compare Student1,Student2 for > in some if else block
# 			if the condition evaluate to true print "If clause successful"
# 			if the condition evaluate to false print "Else clause successful"

# 		set the primary skill for Student1	
# 		print the primary skill for Student1
# 		print the primary skill for Student2


class Student:
    
    def __init__(self,Name,Rollno,Subject):
        self.Name=Name
        self.__Rollno=Rollno
        self._Subject=Subject
        self.Primary_Skill= None
    
    def get_subject (self):
        return self._Subject
    
    
    
    def set_subject (self,newSubject):
         self._Subject=newSubject
         
         
    def get_rollno (self):
        return self.__Rollno
    
    
    def set_rollno (self,newRollno):
        self.__Rollno =newRollno
        
    def display_student_details(self):
        return F" name:{self.Name} rollno {self.__Rollno}  subject {self._Subject}"
    
    
    def get_primarySkill (self):
        return self.__Rollno
    
    def set_primaySkill (self,newPrimarySkill):
       self.newPrimarySkill=newPrimarySkill
       
       
class DBDA_Student(Student):
    def __init__(self,Name,Rollno,Subject,secondarySkills=None):
        super().__init__(Name,Rollno,Subject)
        self.secondarySkills= secondarySkills if secondarySkills else []
        
    #override method 
    def display_student_details(self):
        return F" name{self.Name} rollno {self.__Rollno} subject{self._Subject}"
    
    #  Override the set_primary_skill method to always have SQL as primary skill
    
    
    def set_primary_skill (self):
        self.Primary_Skill="Sql"
        
    
    def get_rollno (self):
        return self.__Rollno   
        
    #comparision 
    def __gt__(self,other):
        return self.get_rollno() > other.get_rollno()
    
def main():
    stud1 = DBDA_Student("Tilak",239105,"Python",["HTML","CSS"])
    stud2 = DBDA_Student("Vivk",239106,"History",["javascipt","react"])
    
    print("rollNo :___")
    print(stud1.get_rollno())
    print(stud2.get_rollno())
    
    
    print("old subject :___")
    print(stud1.get_subject())
    print(stud2.get_subject())
    
    print("updated subject :___")
    print(stud1.set_subject("programimg concept"))
    print(stud2.set_subject("operating system "))
    
    #comparisoion 
    
    if stud1 > stud2:
        print("if clause succesfull ")
    else:
        print("else clause succesfull ")
        
    print("primary skills")
    print(stud1.get_primarySkill())
    print(stud2.get_primarySkill())
    
if __name__== '__main__':
    main()
    