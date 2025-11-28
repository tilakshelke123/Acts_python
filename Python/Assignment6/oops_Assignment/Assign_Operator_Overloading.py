class Student:
    # Constructor: this runs automatically when you create a new student
    def __init__(self, name, rollno, subject):
        # These are instance variables
        self.name = name
        self.rollno = rollno
        self.subject = subject

    # Method to get the subject of the student
    def get_subject(self):
        return self.subject

    # Method to change (set) the subject of the student
    def set_subject(self, new_subject):
        self.subject = new_subject

    # Comparison methods (compare based on roll number)
    def __gt__(self, other):   # Greater than >
        return self.rollno > other.rollno

    def __lt__(self, other):   # Less than <
        return self.rollno < other.rollno

    def __ge__(self, other):   # Greater than or equal to >=
        return self.rollno >= other.rollno

    def __le__(self, other):   # Less than or equal to <=
        return self.rollno <= other.rollno

    def __eq__(self, other):   # Equal to ==
        return self.rollno == other.rollno


# Main program starts here
if __name__ == "__main__":
    # Create two student objects
    student1 = Student("Alice", 101, "Math")
    student2 = Student("Bob", 102, "Science")

    # Display their subjects
    print(f"{student1.name}'s subject: {student1.get_subject()}")
    print(f"{student2.name}'s subject: {student2.get_subject()}")

    # Change their subjects
    student1.set_subject("Physics")
    student2.set_subject("Chemistry")

    # Display subjects again after changing
    print("\nAfter changing subjects:")
    print(f"{student1.name}'s new subject: {student1.get_subject()}")
    print(f"{student2.name}'s new subject: {student2.get_subject()}")

    # Compare the two students using relational operators
    print("\nComparing students:")

    if student1 > student2:
        print("If clause successful for >")
    else:
        print("Else clause successful for >")

    if student1 < student2:
        print("If clause successful for <")
    else:
        print("Else clause successful for <")

    if student1 >= student2:
        print("If clause successful for >=")
    else:
        print("Else clause successful for >=")

    if student1 <= student2:
        print("If clause successful for <=")
    else:
        print("Else clause successful for <=")

    if student1 == student2:
        print("If clause successful for ==")
    else:
        print("Else clause successful for ==")
