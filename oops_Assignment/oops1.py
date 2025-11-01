# A1) Relative superclass and subclasses

class Relative:
    def __init__(self, name, age, relation):
        self.name = name
        self.age = age
        self.relation = relation

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Relation: {self.relation}")


class Sister(Relative):
    def __init__(self, name, age, relation, hobby, school):
        super().__init__(name, age, relation)
        self.hobby = hobby
        self.school = school

    def printDetails(self):
        super().printDetails()
        print(f"Hobby: {self.hobby}, School: {self.school}")


class Uncle(Relative):
    def __init__(self, name, age, relation, job, city):
        super().__init__(name, age, relation)
        self.job = job
        self.city = city

    def printDetails(self):
        super().printDetails()
        print(f"Job: {self.job}, City: {self.city}")


# B2) Parent superclass and subclasses

class Parent:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def printDetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}")


class Mom(Parent):
    def __init__(self, name, age, occupation, favorite_recipe, hobby):
        super().__init__(name, age, occupation)
        self.favorite_recipe = favorite_recipe
        self.hobby = hobby

    def printDetails(self):
        super().printDetails()
        print(f"Favorite Recipe: {self.favorite_recipe}, Hobby: {self.hobby}")


class Dad(Parent):
    def __init__(self, name, age, occupation, favorite_sport, car_model):
        super().__init__(name, age, occupation)
        self.favorite_sport = favorite_sport
        self.car_model = car_model

    def printDetails(self):
        super().printDetails()
        print(f"Favorite Sport: {self.favorite_sport}, Car Model: {self.car_model}")


# C3) Appliance superclass and subclasses

class Appliance:
    def __init__(self, brand, power_usage, color):
        self.brand = brand
        self.power_usage = power_usage
        self.color = color

    def printDetails(self):
        print(f"Brand: {self.brand}, Power Usage: {self.power_usage}W, Color: {self.color}")


class Refrigerator(Appliance):
    def __init__(self, brand, power_usage, color, capacity, has_freezer):
        super().__init__(brand, power_usage, color)
        self.capacity = capacity
        self.has_freezer = has_freezer

    def printDetails(self):
        super().printDetails()
        print(f"Capacity: {self.capacity}L, Has Freezer: {self.has_freezer}")


class Oven(Appliance):
    def __init__(self, brand, power_usage, color, oven_type, temperature_range):
        super().__init__(brand, power_usage, color)
        self.oven_type = oven_type
        self.temperature_range = temperature_range

    def printDetails(self):
        super().printDetails()
        print(f"Oven Type: {self.oven_type}, Temperature Range: {self.temperature_range}")


# D4) Animal superclass and subclasses

class Animal:
    def __init__(self, species, age, color):
        self.species = species
        self.age = age
        self.color = color

    def printDetails(self):
        print(f"Species: {self.species}, Age: {self.age}, Color: {self.color}")


class Dog(Animal):
    def __init__(self, species, age, color, breed, owner_name):
        super().__init__(species, age, color)
        self.breed = breed
        self.owner_name = owner_name

    def printDetails(self):
        super().printDetails()
        print(f"Breed: {self.breed}, Owner Name: {self.owner_name}")


class Tiger(Animal):
    def __init__(self, species, age, color, origin, weight):
        super().__init__(species, age, color)
        self.origin = origin
        self.weight = weight

    def printDetails(self):
        super().printDetails()
        print(f"Origin: {self.origin}, Weight: {self.weight}kg")


# E5) Publication superclass and subclasses

class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def printDetails(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")


class Book(Publication):
    def __init__(self, title, author, year, pages, genre):
        super().__init__(title, author, year)
        self.pages = pages
        self.genre = genre

    def printDetails(self):
        super().printDetails()
        print(f"Pages: {self.pages}, Genre: {self.genre}")


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number, publisher):
        super().__init__(title, author, year)
        self.issue_number = issue_number
        self.publisher = publisher

    def printDetails(self):
        super().printDetails()
        print(f"Issue Number: {self.issue_number}, Publisher: {self.publisher}")



def main():
    #name, age, relation
    Rel = Relative("Tilak",23,"Son")
    #name, age, occupation
    par = Parent("Indu",53,"Maa")
    #brand, power_usage, color
    app =Appliance("Allen-Solly","25-GB","lIGHT-bLUE")
    # species, age, color
    Ani = Animal("animal",23,"black-white")
    #title, author, year
    Pub = Publication("The DARK nIGHT","j.j tHOMSON",2025)
    
    
    Rel.printDetails()
    par.printDetails()
    app.printDetails()
    Ani.printDetails()
    Pub.printDetails()
    
if __name__ == '__main__':
    main()