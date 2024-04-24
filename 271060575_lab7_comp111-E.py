import math

print("question 1")

class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,length,width):
        super().area()
        self.length = length
        self.width = width
    def area(self):
        print("area of rectangle is: ")
        return self.length * self.width 
        
class Circle(Shape):
    def __init__(self,radius):
        super().area()
        self.radius = radius 
    def area(self):
        print("area of circle is :")
        return (math.pi) * self.radius**2
    
circ_rad_obj = int(input("enter radius of circle : "))    
circle_obj = Circle(circ_rad_obj)  
print(circle_obj.area()) 

rec_len_obj = int(input("enter length of rectangle : ")) 
rec_width_obj = int(input("enter width of rectangle : "))
rectangle_obj = Rectangle(rec_len_obj,rec_width_obj)
print(rectangle_obj.area())

print("question 2")

class Animal:
    def make_sound(self):
        print("some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("bark!") 

class Cat(Animal):
    def make_sound(self):
        print("meow!")  

cat_obj = Cat()
print(cat_obj.make_sound())   
dog_obj = Dog()
print(dog_obj.make_sound())  

print("question 3")

import datetime

class Vehicle:
    def __init__(self,year_manufactured,make,model):
        self.year_manufactured = year_manufactured
        self.model = model
        self.make=make
    def get_age(self):
        print("the age of vehicle is:")

class Car(Vehicle):
    def __init__(self,num_doors,year_manufactured,make,model):
        super().__init__(year_manufactured,make,model)
        self.num_doors = num_doors
    def get_door_descrip(self):
        print("num of doors are: ", self.num_doors)

class Truck(Vehicle):
    def __init__(self,bed_size,year_manufactured,make,model):
        super().__init__(year_manufactured,make,model) 
        self.bed_size = bed_size     
    def get_bed_descrip(self):
        print("size of bed is: ",self.bed_size)

truck_bed_obj = str(input("enter the size of bed : "))
truck_yr_obj =int(input("enter the year truck was manufactured : "))
truck_make_obj = str(input("when was the truck made : "))
truck_model_obj = str(input("what is the model of truck : "))        
truck_obj = Truck(truck_bed_obj,truck_yr_obj,truck_make_obj,truck_model_obj) 
print(truck_obj.get_bed_descrip()) 
print(truck_obj.get_age())

car_door_obj = int(input("enter num of doors the car has : "))
car_yr_obj = int(input("enter the year car was manufactured : "))
car_make_obj = str(input("when was the car made : "))
car_model_obj = str(input("what is the model of car : "))
car_obj = Car(car_door_obj,car_yr_obj,car_make_obj,car_model_obj)
print(car_obj.get_door_descrip())   
print(car_obj.get_age()) 

print("question 4")

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_info(self):
        print(f"person {self.name} age is {self.age} and gender is {self.gender}")

class Student(Person):
    def __init__(self,student_id,name,age,gender):
        super().__init__(name,age,gender)  
        self.student_id = student_id
    def get_student_info(self):
        print(f"student having ID {self.student_id} has name {self.name},age {self.age} and gender {self.gender} ")

student_id_obj = int(input("enter student ID: "))
student_name_obj = str(input("enter student's name :"))
student_age_obj = int(input("enter student's age : "))
student_gender_obj = str(input("enter student's gender : "))
student_obj = Student(student_id_obj,student_name_obj,student_age_obj,student_gender_obj)
print(student_obj.get_info())
print(student_obj.get_student_info())

print("question 5")

class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age= age
        self.salary = salary
    def get_salary(self):
        print("salary of emp is: ", self.salary)

class Manager(Emp):
    def __init__(self,bonus,name,age,salary):
        super().__init__(name,age,salary) 
        self.bonus = bonus
    def get_bonus(self):
        print("bonus of employee is :",self.bonus)

class Developer(Emp):
    def __init__(self,skills,name,age,salary):
        super().__init__(name,age,salary) 
        self.skills=skills
    def get_skills(self):
        print("the skills of employee are: ", self.skills)

man_bonus_obj =float(input("enter manager's bonus : "))
man_name_obj = str(input("enter name of manager : "))
man_age_obj = int(input("enter the age of manager : "))   
man_sal_obj = float(input("enter the salary of manager : "))      
skill_lst = ["leadership","management","HTML","CSS"]
manager_obj=Manager(man_bonus_obj,man_name_obj,man_age_obj,man_sal_obj)
print(manager_obj.get_salary())  
print(manager_obj.get_bonus())

dev_skill_obj = []
dev_skill_obj = str(input("enter the skills of developer separated by comma : "))
dev_name_obj = str(input("enter name of developer : "))
dev_age_obj = int(input("enter age of developer : "))
dev_sal_obj = float(input("enter salary of developer : "))
developer_obj = Developer(skill_lst,dev_name_obj,dev_age_obj,dev_sal_obj)
print(developer_obj.get_salary())
print(developer_obj.get_skills())   







