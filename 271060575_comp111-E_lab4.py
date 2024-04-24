'''
print("question 2")
class Calculator:
    def __init__(self,num1,num2) :
        self.num1 = num1
        self.num2 = num2
    def sum(self,num1,num2):
        return self.num1 + self.num2
    def diff(self,num1,num2):
        return self.num1 - self.num2
    def multp(self,num1,num2):
        return self.num1 * self.num2
    def div(self,num1,num2):
        return self.num1 / self.num2
num_1 = int(input("enter first num"))
num_2 = int(input("enter second num"))    
number = Calculator(num_1 , num_2)
print("sum:" , number.sum(num_1,num_2)) 
print("difference:" , number.diff(num_1,num_2)) 
print("multiple:" , number.multp(num_1,num_2)) 
print("division:" , number.div(num_1,num_2)) 

print("question 1")
class Calculation:
   def __init__(self,length,width,height,base) :
       self.length = length
       self.width = width
       self.height = height
       self.base = base
   def calc_area_rectangle(self,length,width):
       return self.length * self.width
   def calc_area_triangle(self,height,base):
       return (self.height * self.base) / 2
   def calc_perim_rectangle(self,length,width):
       return 2 * (self.length + self.width)
length1 = int(input("enter length of rectangle"))
width1 = int(input("enter width of rectangle")) 
height1 = int(input("enter height of triangle"))
base1 = int(input("enter base of triangle"))  
calc = Calculation(length1,width1,height1,base1)
print("area of rectangle:" , calc.calc_area_rectangle(length1,width1))
print("area of triangle:" , calc.calc_area_triangle(height1,base1))
print("perimeter of rectangle:" , calc.calc_perim_rectangle(length1,width1))
    
print("question 4")
class Book:
    def __init__(self,__title,__author,__status) :
        self.__title = __title
        self.__author=__author
        self.__status=__status
    def check_out(self,__status):
        if __status == "borrowed":
            print("book has already been borrowed")
        else: 
            self.__status = "borrowed"
            print("book has been borrowed")
    def return_book(self,__status):
        if __status == "available":
            print("book is already available")
        else:
            __status == "available"
            print("book is now available ")
    def get_status(self,__status):
        return __status                    
'''
class shape:
    def draw(self):
        print("drawing a circle")
class circle(shape):
    pass
c1 = circle()
print(c1.draw()) 

