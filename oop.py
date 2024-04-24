
class circle:
    def __init__(self,radius) :
        self.radius = radius
    def get_area(self,radius):
        return 3.14 * radius ** 2
    def circum(self,radius):
        return 2 * 3.14 * radius
radius_input = int(input("enter radius of circle"))
rad = circle(radius_input)
print("area of cirle:" , rad.get_area(radius_input))
print("circum of circ:" , rad.circum(radius_input))     
class temperature:
    def __init__(self,farhen,cels) :   
        self.farhen = farhen
        self.cels = cels
    def cels_conv(self,cels):
        return (cels * 9/5)  + 32
    def farhen_conv(self,farhen):
        return (farhen - 32) * 5/9 
cels_input = int(input("enter cels temperature"))
farhen_input = int(input("enter farhen temperature"))
temp = temperature(cels_input , farhen_input)
print("cels to farhen:" , temp.cels_conv(cels_input))
print("farhen to cels:" , temp.farhen_conv(farhen_input))    
class square:
    def __init__(self,side) :
        self.side = side
    def area(self,side):
        return side ** 2
    def perimeter(self,side):
        return 4 * side 
side_input = int(input("enter side of square"))
side_square = square(side_input)
print("area of square:" , side_square.area(side_input)) 
print("perim of square:" , side_square.perimeter(side_input))   


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_info(self,name,emp_id):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
    
    def set_salary(self, salary):
        self.salary = salary
        print("Salary:", self.salary)
    
    def set_department(self, department):
        self.department = department
        print("Department:", self.department)

dept = str(input("enter your departemnt"))
salr = int(input("enter your slary"))
name_emp = str(input("enter your name"))
id_emp = int(input("enter your id"))
emp_info = Employee(name_emp , id_emp)
emp_info.set_salary(salr)
emp_info.set_department(dept)

print("Employee information:")
emp_info.display_info(name_emp , id_emp)

class BankAcc:
    def __init__(self, acc_num , balance):
        self.acc_num = acc_num
        self.balance = balance
    def deposit(self,amount ,balance):
        self.amount = amount
        return self.amount + self.balance
    def withdraw(self,amount,balance):
        if self.amount > self.balance:
            print("insuffiecient balance")
        else:
            print(self.amount - self.balance)    
    def display_balance(self,balance):
        print(self.balance)
    def display_info(self,acc_num , balance):
        print(self.acc_num)
        print(self.balance)    
acc_input = int(input("enter acc num: " )) 
balance_input = int(input("enter current balnce: "))
amount_input= int(input("enter amount amount to be withdrawn/deposited: "))           
balance_info = BankAcc(acc_input,balance_input)  
balance_info.deposit(amount_input,balance_input)
balance_info.withdraw(amount_input, balance_input) 
print("bank account informaion")
balance_info.deposit(amount_input,balance_input) 

class sec_data:
    def __init__(self, data, pswrd):
        self.__data = data
        self.__pswrd = pswrd
    
    def set_pswrd(self, new_pswrd):
        if self.__pswrd is not None:
            print("Changing password")
        else:
            print("Setting new password")
        self.__pswrd = new_pswrd
    
    def store_data(self):
        while True:
            password_new = input("Enter password: ")
            if password_new == self.__pswrd:
                print("Correct password!")
                data_input = input("Enter data: ")
                self.__data = data_input
                break
            else:
                print("Incorrect password. Try again.")
    
    def get_data(self):
        while True:
            password_input = input("Enter password: ")
            if password_input == self.__pswrd:
                print("Data:", self.__data)
                break
            else:
                print("Incorrect password. Try again.")
    
    def pswrd_length(self):
        if self.__pswrd is not None:
            return len(self.__pswrd)
        else:
            return 0

# Example usage
data = "Initial data"
password = input("Enter password: ")
obj = sec_data(data, password)
obj.store_data()
obj.get_data()
obj.set_pswrd("new_password")
print("New password length:", obj.pswrd_length())


class park:
    def __init__(self,garden,swing):
        self.garden = garden
        self.swing = swing
    def park_mdt(self):
        print(self.swing)
     
class new_park(park):
    def __init__(self,garden,swing,slide,plground):
        super().__init__(garden,swing)
        self.slide = slide
        self.plground = plground    
    def park_gulberg(self):
        print(self.slide)           
        print(self.garden)
new_park_1 = new_park("ttr","rrr","2","three")
print(new_park_1.park_gulberg())


class product:
    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity
    def set_name(self,a):
        self.__name = a
    def set_price(self,b):
        if b >= 0:
            self.__price = b
        else:
            print("price can not be negative")  
    def set_quantity(self,c):
        if c >= 0:
             self.__quantity = c
        else:
            print("quantity must be positive")  

class product:
    def __init__(self,name= "undefined", price = 0.0, stock = 0):
        self.name = name
        self.price = price
        self.stock = stock
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_stock(self):
        return self.stock
    def set_name(self,a):
        self.name = a
    def set_price(self,b):
        self.price = b
    def set_stock(self,c):
        self.stock = c
    def tostring(self):
        print(f"the name of the product is {self.name} price is {self.price} stock is {self.stock}")            
  
class electronic(product):
    def __init__(self,name= "undefined", price = 0.0, stock = 0,brand = "nishat",war_period = 2003):
        super().__init__(name,price,stock)      
        self.brand = brand
        self.war_period = war_period
    def tostring(self):
        print(f"brand is{self.brand} with warranty period {self.war_period}")
electronic_one = electronic()
print(electronic_one.tostring())

class emp:
    def __init__(self,name):
        self.name= name
    def show(self):
        print(f"name is {self.name}")    

class dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"dance is {self.dance}")
class danceremp(dancer,emp):
    def __init__(self,dance,name,cards,kites):
        super().__init__(dance,name)
        self.cards = cards
        self.kites = kites
    def method(self):
        print(f"name{self.name} dance is{self.dance} cards left {self.cards}")    
obj = danceremp("katha" , "tatheer", 27 , "threee")
print(obj.method())
print(danceremp.mro())

class secure_data:
    def __init__(self, data, password):
        self.data = data
        self.password = password
    
    def set_password(self):
        action = input("Enter 'set' to set a new password or 'change' to change the password: ")
        if action == "set":
            new_password = input("Enter new password: ")
            self.password = new_password
        elif action == "change":
            current_password = input("Enter current password: ")
            if current_password == self.password:
                new_password = input("Enter new password: ")
                self.password = new_password
            else:
                print("Incorrect password. Try again.")
        else:
            print("Invalid action.")
    
    def store_data(self):
        checker = input("Enter password to verify: ")
        if checker == self.password:
            new_data = input("Enter data to store: ")
            self.data = new_data
        else:
            print("Incorrect password. Try again.")
    
    def get_data(self):
        checker = input("Enter password to verify: ")
        if checker == self.password:
            print(self.data)
        else:
            print("Incorrect password. Try again.")
    
    def password_length(self):
        return len(self.password)           

# Example usage:
data1 = secure_data("initial_data", "initial_password")
data1.set_password()
data1.store_data()
data1.get_data()
print("Password length:", data1.password_length())

class Bug:
    def __init__(self, initial_position):
        self.position = initial_position
        self.direction = "right"  # Bug initially moves to the right
    
    def turn(self):
        # Change direction
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
    
    def move(self):
        # Move one unit in the current direction
        if self.direction == "right":
            self.position += 1
        else:
            self.position -= 1
    
    def get_position(self):
        return self.position

# Example usage:
bug = Bug(22)  # Create a Bug object starting at position 0
print("Initial position:", bug.get_position())

bug.move()  # Move the bug
print("Position after moving:", bug.get_position())

bug.turn()  # Turn the bug
bug.move()  # Move again after turning
print("Position after turning and moving:", bug.get_position())

class ComboLock:
    def __init__(self, sec1, sec2, sec3):
        self.combination = [sec1, sec2, sec3]
        self.reset()

    def reset(self):
        self.current_position = 0

    def turn_left(self, ticks):
        self.current_position = (self.current_position - ticks) % 40

    def turn_right(self, ticks):
        self.current_position = (self.current_position + ticks) % 40

    def open(self):
        if (
            self.current_position == self.combination[0]
            and self.combination[1] == self.combination[1]
            and self.current_position == self.combination[2]
        ):
            return True
        return False

# Example usage:
lock = ComboLock(10, 20, 30)
print(lock.open())  # Output: False

lock.turn_right(10)
lock.turn_left(10)
lock.turn_right(10)
print(lock.open())  # Output: True

# aggregation
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12) + self.bonus
class Employee:
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.sal = sal
    def total_salary(self):
        return self.sal.annual_salary()
sal = Salary(1234,22)    
emp_obj = Employee("titi",12,sal)
print(emp_obj.total_salary())                   
              
class ContainedClass:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
    
    def contained_method(self):
        return f"Contained Method: {self.attr1}, {self.attr2}"

class ContainerClass:
    def __init__(self):
        self.contained_objects = []  # Initialize the list to hold contained objects

    def add_contained_object(self, contained_obj):
        self.contained_objects.append(contained_obj)
    
    def container_method(self):
        # Access methods of contained objects
        for obj in self.contained_objects:
            print(obj.contained_method())
contained_obj1 = ContainedClass("value1", "value2")
contained_obj2 = ContainedClass("value3", "value4")

container_obj = ContainerClass()

container_obj.add_contained_object(contained_obj1)
container_obj.add_contained_object(contained_obj2)

container_obj.container_method()

# composition 
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12) + self.bonus
class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.obj_sal = Salary(pay,bonus)
    def total_salary(self):
        return self.obj_sal.annual_salary()
emp_obj = Employee("titi",12,21234,22)
print(emp_obj.total_salary())         
'''
class Engine:
    def __init__(self,horsepower=123,fuel_type="petrol"):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
    def start(self):
        print(f"car started , now at {self.horsepower}")    
    def stop(self):
        print(f"car stopped,now at {self.horsepower}")    
class Wheel:
    def __init__(self,size,material):
        self.size = size
        self.material = material
class FuelTank:
    def __init__(self,capacity=222,current_level=444):
        self.capacity = capacity
        self.current_level = current_level
    def before_fuel(self):
        print(f"engien at {self.capacity} ") 
    def after_fuel(self):    
        print(f"after refilling {self.current_level}")   
class Car:
    def __init__(self,horsepower,capacity,current_level):
        self.horsepower = Engine(horsepower)
        self.capacity = FuelTank(capacity)
        self.current_level = FuelTank(current_level)   
    def start_car(self):
        print("starting the car")
        self.horsepower.start()
    def stop_car(self):
        print("stopping the car")
        self.horsepower.stop()  
    def refuel(self):
        print("fuelling the car")
        self.capacity.before_fuel()
        self.current_level.after_fuel()      
car_obj = Car(1232,222,444)
car_obj.start_car()    
car_obj.stop_car()
car_obj.refuel()     

class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def detail(self):
        print(self.title)
        print(self.author)
        print(self.isbn)    
class Member:
    def __init__(self,name,member_id,title,author,isbn):
        self.name = name
        self.member_id = member_id
        self.obj_book = Book(title,author,isbn)
    def borrow_book(self):
        self.obj_book == "borrowed"
        print(f"member {self.name} has borrowed book having details:" ) 
        print(self.obj_book.detail())   
    def return_book(self):
        self.obj_book == "returned"
        print(f"member {self.name} has returned book having details:" ) 
        print(self.obj_book.detail())      
class Library:
    def __init__(self,name,member_id,title,author,isbn):
        self.obj_book = Book(title,author,isbn)
        self.obj_member = Member(name,member_id)
        self.book_list = []
    def add_book(self):
        if self.obj_book not in self.book_list:
            self.book_list += self.obj_book
        else:
            print("book already exists")
    def remove_book(self):
        if self.obj_book in self.book_list:
            self.book_list.remove(self.obj_book)
        else:
            print("book already removed")
lib_obj = Library("tatheer",12345,"fault in stars" , "john green" ,5432)  
print(lib_obj.add_book())                              

class Address:
    def __init__(self,street,city,zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode
    def detail(self):
        print(self.street)
        print(self.city)
        print(self.zipcode)    

class Person:
    def __init__(self,name,age,street,city,zipcode):
        self.name = name
        self.age = age
        self.obj_address = Address(street,city,zipcode)
    def detail(self):
        print(f"person having name{self.name} and age {self.age} lives in :")   
        return self.obj_address.detail()
person_obj = Person("tatheer","12","lre12","lahore","12345")    
print(person_obj.detail())

class Course:
    def __init__(self,course_code,title,department,professor):
        self.course_code = course_code
        self.title = title
        self.department = department
        self.professor=professor
    def detail(self):
        print(self.course_code,self.professor,self.title,self.department)  
class Professor:
    def __init__(self,name,emp_id,department,course_code,title,professor):
        self.name = name
        self.emp_id = emp_id
        self.course_obj = Course(course_code,title,department,professor)
    def detail(self):
        print(self.name)
        print(self.emp_id)
        print(self.course_obj.detail())   
class Department:
    def __init__(self,dept_name,name,emp_id,department,course_code,title,professor):
        self.dept_name = dept_name
        self.prof_obj = Professor(name,emp_id,department,course_code,title,professor) 
    def detail(self):
        print(self.dept_name)
        print(self.prof_obj.detail())            
class University:
    def __init__(self,dept_name,name,emp_id,department,course_code,title,professor):
        self.dept_obj = Department(dept_name,name,emp_id,department,course_code,title,professor)        
    def detail(self):
        print(self.dept_obj.detail())
uni_obj = University("english","tatheer","12340","urdu","1234","dvanced end","tahir hassan")   
print(uni_obj.detail())     

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def detail(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.collection = []

    def add_book(self, book_obj):
        if book_obj not in self.collection:
            self.collection.append(book_obj)
        else:
            return "Book already in collection"

    def display(self):
        return [book.detail() for book in self.collection]

book_obj = Book("Fault in Our Stars", "John Green", 1234)
lib_obj = Library()
print(lib_obj.add_book(book_obj))
print(lib_obj.display())

class Student:
    def __init__(self,name,grade,roll_num):
        self.name = name
        self.grade = grade
        self.roll_num = roll_num
    def student_info(self):
        return f"{self.name},{self.roll_num},{self.grade}" 
class School:
    def __init__(self,):
        self.all_students = []
    def add_student(self,st_to_add):
        if st_to_add not in self.all_students:
            self.all_students.append(st_to_add)
    def display_all_student(self):
        for obj in self.all_students:
            print(obj.student_info())   
Student_obj = Student("tatheer","b+",1232146)
Student_obj1 = Student("fatima","A+",4224326)
school_obj = School()                 
print(school_obj.add_student(Student_obj))
print(school_obj.add_student(Student_obj1))
print(school_obj.display_all_student())

class Student:
    def __init__(self,name,roll_num,grade):
        self.name = name
        self.grade = grade
        self.roll_num = roll_num
    def display_student(self):
        return f"name {self.name} roll num {self.roll_num} grade {self.grade}"
class Classroom:
    def __init__(self):
        self.all_students = []
    def add_student(self,st_to_add):
        if st_to_add not in self.all_students:
            return self.all_students.append(st_to_add)
        else:
            return "student already added"
    def remove_student(self,st_to_remove):
        if st_to_remove in self.all_students:
            return self.all_students.remove(st_to_remove)
        else:
            return "student does not exist"
    def list_student(self):
        for i in self.all_students:
            print(i.display_student())   
Student_obj = Student("tatheer","b+",1232146)
Student_obj1 = Student("fatima","A+",4224326)   
class_obj = Classroom()                                  
print(class_obj.add_student(Student_obj))
print(class_obj.add_student(Student_obj1))
print(class_obj.list_student())

class BankAcc:
    def __init__(self,acc_id,acc_title,balance,email_id):
        self.__acc_id = acc_id
        self.__acc_title = acc_title
        self.__balance = balance
        self.__email_id = email_id
    def get_acc_id(self):
        return self.__acc_id
    def get_title(self):
        return self.__acc_title
    def get_balance(self):
        return self.__balance
    def get_email_id(self):
        return self.__email_id
    def set_acc_id(self,a):
        self.__acc_id = a    
    def set_title(self,b):
        self.__acc_title = b
    def set_balance(self,c):
        self.__balance = c  
    def set_email_id(self,d):
        self.__email_id = d  
    def deposit(self,amount):
        print(f"you deposited {amount}")
        print("your balance is :")
        self.__balance+=amount
        print(self.__balance)
    def withdraw(self,amount):
        print(f"you want to withdraw {amount}")
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"remaining balance is {self.__balance}")    
        else:
            print("insufficient funds")
bank_obj = BankAcc(1234,"new fund" , 245,"dsag344")
print(bank_obj.withdraw(26))                

class Phonebook:
    def __init__(self):
        self.all_contact = {}
    def insert(self,name,number):
        print("lest add number in phonebook")
        self.all_contact[name]=number
    def show_contact(self):
        for i in self.all_contact:
            print(i)    
    def search_contact(self,name):
        if name in self.all_contact:
            print("yes founded")
        else:
            print("not found")         
phone = Phonebook()
print(phone.insert("tatheer",3456465))
print(phone.show_contact())
print(phone.search_contact("tatheer"))
'''
'''
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.order_list = []

    def add_item(self, item, quantity):
        self.order_list.append([item, quantity])

    def calculate_bill(self):
        total_bill = 0
        for item, quantity in self.order_list:
            total_bill += item.price * quantity
        return total_bill

# Create Item objects
item1 = Item("Burger", 5)
item2 = Item("Pizza", 10)
item3 = Item("Salad", 7)

# Store items in menu list
menu = [item1, item2, item3]

# Create Order object
order1 = Order(1)

# Display menu and take orders
while True:
    print("Menu:")
    for index, item in enumerate(menu, start=1):
        print(f"{index}. {item.name} - ${item.price}")
    choice = input("Enter item number to order (or 'exit' to exit): ")
    if choice.lower() == 'exit':
        break
    try:
        choice = int(choice)
        if choice < 1 or choice > len(menu):
            print("Invalid choice. Please choose a number from the menu.")
            continue
        quantity = int(input("Enter quantity: "))
        order1.add_item(menu[choice-1], quantity)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate bill and display
total_bill = order1.calculate_bill()
print(f"Total bill for order {order1.order_number}: ${total_bill}")
'''          


