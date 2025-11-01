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

#--------------------------------------------------------------------------------------

# class Student:
    
#     def __init__(self,Name,Rollno,Subject):
#         self.Name=Name
#         self.__Rollno=Rollno
#         self._Subject=Subject
#         self.Primary_Skill= None
    
#     def get_subject (self):
#         return self._Subject
    
    
    
#     def set_subject (self,newSubject):
#          self._Subject=newSubject
         
         
#     def get_rollno (self):
#         return self.__Rollno
    
    
#     def set_rollno (self,newRollno):
#         self.__Rollno =newRollno
        
#     def display_student_details(self):
#         return F" name:{self.Name} rollno {self.__Rollno}  subject {self._Subject}"
    
    
#     def get_primarySkill (self):
#         return self.__Rollno
    
#     def set_primaySkill (self,newPrimarySkill):
#        self.newPrimarySkill=newPrimarySkill
       
       
# class DBDA_Student(Student):
#     def __init__(self,Name,Rollno,Subject,secondarySkills=None):
#         super().__init__(Name,Rollno,Subject)
#         self.secondarySkills= secondarySkills if secondarySkills else []
        
#     #override method 
#     def display_student_details(self):
#         return F" name{self.Name} rollno {self.__Rollno} subject{self._Subject}"
    
#     #  Override the set_primary_skill method to always have SQL as primary skill
    
    
#     def set_primary_skill (self):
#         self.Primary_Skill="Sql"
        
    
#     def get_rollno (self):
#         return self.__Rollno   
        
#     #comparision 
#     def __gt__(self,other):
#         return self.get_rollno() > other.get_rollno()
    
# def main():
#     stud1 = DBDA_Student("Tilak",239105,"Python",["HTML","CSS"])
#     stud2 = DBDA_Student("Vivk",239106,"History",["javascipt","react"])
    
#     print("rollNo :___")
#     print(stud1.get_rollno())
#     print(stud2.get_rollno())
    
    
#     print("old subject :___")
#     print(stud1.get_subject())
#     print(stud2.get_subject())
    
#     print("updated subject :___")
#     print(stud1.set_subject("programimg concept"))
#     print(stud2.set_subject("operating system "))
    
#     #comparisoion 
    
#     if stud1 > stud2:
#         print("if clause succesfull ")
#     else:
#         print("else clause succesfull ")
        
#     print("primary skills")
#     print(stud1.get_primarySkill())
#     print(stud2.get_primarySkill())
    
# if __name__== '__main__':
#     main()

#------------------------------------------------------


class Student:
    """
    Base class for a Student, demonstrating access modifiers:
    - Name: Public
    - __Rollno: Private (name-mangled in Python)
    - _Subject: Protected (convention in Python)
    """
    def __init__(self, name, rollno, subject):
     
        self.Name = name
        self.__Rollno = rollno
        self._Subject = subject
        self.primary_skill = "Unassigned"

    def get_subject(self):
        """Returns the protected subject."""
        return self._Subject

    def set_subject(self, new_subject):
        """Sets a new protected subject."""
        self._Subject = new_subject
        print(f"Subject for {self.Name} updated to: {self._Subject}")

    def get_rollno(self):
        """Returns the private roll number."""
        return self.__Rollno

    def set_rollno(self, new_rollno):
        """Sets a new private roll number."""
        self.__Rollno = new_rollno
        print(f"Roll No for {self.Name} updated to: {self.__Rollno}")

    def get_primary_skill(self):
        """Prints and returns the primary skill."""
        print(f"{self.Name}'s primary skill is: {self.primary_skill}")
        return self.primary_skill

    def set_primary_skill(self, skill):
        """Sets the primary skill."""
        self.primary_skill = skill
        print(f"Primary skill for {self.Name} set to: {self.primary_skill}")

    def display_student_details(self):
        """Prints the name, rollno, and subject."""
        print(f"Name: {self.Name}")
        print(f"Roll No: {self.get_rollno()}")
        print(f"Subject: {self.get_subject()}")
        print(f"Primary Skill: {self.primary_skill}")


class DBDA_student(Student):
    """
    Subclass for a DBDA student, inheriting from Student.
    Overrides set_primary_skill and display_student_details.
    """
    def __init__(self, name, rollno, subject, secondary_skills):
        super().__init__(name, rollno, subject)
        self.secondary_skills = secondary_skills


    def set_primary_skill(self, skill=None):
        """
        Overrides the parent method. **Always forces 'SQL'** as the primary skill.
        The 'skill' argument is ignored in this implementation.
        """
        self.primary_skill = "SQL"
        print(f"Primary skill for {self.Name} (DBDA) **overridden** to: {self.primary_skill}")

    def display_student_details(self):
        """
        Overrides the parent method to include primary_skill and secondary_skills.
        """
        print(f"DBDA Student Details for {self.Name} (Subclass)")
        print(f"Name: {self.Name}")
        print(f"Roll No: {self.get_rollno()}")
        print(f"Subject: {self.get_subject()}")
        print(f"Primary Skill: {self.primary_skill}")
        print(f"Secondary Skills: {', '.join(self.secondary_skills)}")
        print("=" * 45)



if __name__ == "__main__":
    print("1. Object Creation")
    Student1 = DBDA_student(
        name="Alice", 
        rollno=101, 
        subject="Data Warehousing", 
        secondary_skills=["Python", "R", "Tableau"]
    )

    Student2 = DBDA_student(
        name="Bob", 
        rollno=102, 
        subject="Machine Learning", 
        secondary_skills=["Java", "Cloud Computing"]
    )

    Student1.display_student_details()
    Student2.display_student_details()


    print("2. Display Initial Subject Names and Roll Numbers")
    print(f"Student1 Subject: {Student1.get_subject()}")
    print(f"Student2 Subject: {Student2.get_subject()}")
    
    print(f"Student1 Roll No: {Student1.get_rollno()}")
    print(f"Student2 Roll No: {Student2.get_rollno()}")


    print("3. Set New Subject Name")
    Student1.set_subject("Big Data Analytics")
    Student2.set_subject("Business Intelligence")


    print(" 4. Display Subject Names After Update")
    print(f"Student1 Updated Subject: {Student1.get_subject()}")
    print(f"Student2 Updated Subject: {Student2.get_subject()}")

    

    print("5. Comparison of Students (Using Roll No for > Logic)")
    if Student1.get_rollno() > Student2.get_rollno():
        print("If clause successful (Student1 Roll No > Student2 Roll No)")
    else:
        print("Else clause successful (Student1 Roll No <= Student2 Roll No)")

  

    print("6. Set and Print Primary Skill (Demonstrating Overriding)")
    Student1.set_primary_skill("Artificial Intelligence") 
    
    Student1.get_primary_skill()

    
    
    Student2.set_primary_skill("Cloud") 
    Student2.get_primary_skill()        

    # print("\n" + "#" * 50 + "\n")
    # print("Execution complete.")
