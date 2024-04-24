class my_string:
    def __init__(self,string) :
        self.string = string
    def get_string(self,string):
        print(string)
    def print_string(self,string):
        return string.upper()
    def reverse_string(self,string):
        return string[::-1]
str_input = str(input("enter a string"))
str1 = my_string(str_input)
print("string in upper:" , str1.print_string(str_input))
print("string in reverse:" , str1.reverse_string(str_input))

class LibraryAccount:
    def __init__(self,CentralLibrary,acc_holder,acc_id,books_checked) :
        self.CentralLibrary = CentralLibrary
        self.acc_holder = acc_holder
        self.acc_id = acc_id
        self.books_checked = books_checked
    def DisplayAccountInfo(self,CentralLibrary,acc_holder,acc_id,books_checked):
        print(self.acc_id)
        print(self.acc_holder)
        print(self.CentralLibrary)    
        print(self.books_checked)
acc_id_input1 = int(input("enter your id(user 1):"))
acc_holder_input1 =str(input("enter your name(user 1) :"))
books_checked_input1 = int(input("enter number of books checked out(user 1):"))

acc_id_input2 = int(input("enter your id(user 2) "))
acc_holder_input2 =str(input("enter your name(user 2) :"))
books_checked_input2 = int(input("enter number of books checked out(user 2): "))

acc_id_input3 = int(input("enter your id(user 3): "))
acc_holder_input3 =str(input("enter your name(user 3): "))
books_checked_input3 = int(input("enter number of books checked out(user 3): "))
CentralLibrary = "CentralLibrary"
user1 = LibraryAccount(CentralLibrary,acc_holder_input1 ,acc_id_input1 ,books_checked_input1)
user2 = LibraryAccount(CentralLibrary,acc_holder_input2 ,acc_id_input2 ,books_checked_input2)
user3 = LibraryAccount(CentralLibrary,acc_holder_input3 ,acc_id_input3 ,books_checked_input3)
print(user1.DisplayAccountInfo(CentralLibrary,acc_holder_input1 ,acc_id_input1 ,books_checked_input1))
print(user2.DisplayAccountInfo(CentralLibrary,acc_holder_input2 ,acc_id_input2 ,books_checked_input2))
print(user3.DisplayAccountInfo(CentralLibrary,acc_holder_input3 ,acc_id_input3 ,books_checked_input3))

class Employee:
    def __init__(self,emp_id,emp_name,emp_salary) :
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
    def display_emp_info(self,emp_id,emp_name,emp_salary):
        print(self.emp_id)
        print(self.emp_name)
        print(self.emp_salary)
emp_1 = Employee(1234 , "fatima" , 456)
emp_2 = Employee(4143 , "john" , 765)
emp_3 = Employee(7346 , "tatheer" , 742)        
print(emp_1.display_emp_info(1234 , "fatima" , 456))
print(emp_2.display_emp_info(4143 , "john" , 765))
print(emp_3.display_emp_info(7346 , "tatheer" , 742))
emp_list = [emp_1 , emp_2 , emp_3]
print(emp_list)

class Manager:
    def __init__(self,man_id,man_name) :       
        self.man_id = man_id
        self.man_name = man_name
    def display_man_info(self,man_id,man_name) :
        print(self.man_name)
        print(self.man_id)    
manager_1 = Manager(23123 , "haroon")
manager_2 = Manager(87847 , "fatima")
print(manager_1.display_man_info(23123 , "haroon"))   
print(manager_2.display_man_info(87847 , "fatima"))     
manager_list = [manager_1 , manager_2]

