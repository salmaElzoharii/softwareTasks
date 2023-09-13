import math
class ComplexNum:
    flag=0
    def __init__(self,complexStr):
        if(complexStr[0]=='-'):
            complexStr=complexStr.split('-',1)[1]
            self.flag=1
        if(complexStr.__contains__('+')):
            self.real=float((complexStr.split('+'))[0])
            self.img=float((((complexStr.split('+'))[1]).split('i'))[0])
        elif (complexStr.__contains__('-')):
            self.real = float((complexStr.split('-'))[0])
            self.img = float((((complexStr.split('-'))[1]).split('i'))[0])
            self.img=-1*self.img
        if(self.flag==1):
            self.real=self.real*-1
    def __str__(self):
        if self.img >= 0:
            return f"{self.real} + {self.img}i"
        else:
            return f"{self.real*1} - {(-1*self.img)}i"
    def __add__(self, other):
        real = self.real + other.real
        imaginary = self.img + other.img
        return ComplexNum(f"{real}+{imaginary}i")
    def __sub__(self, other):
        real = self.real - other.real
        imaginary = self.img - other.img
        return ComplexNum(f"{real}+{imaginary}i")
    def __mul__(self, other):
        real = (self.real *other.real)-(self.img*other.img)
        imaginary = (self.img *other.real)+(self.real*other.img)
        return ComplexNum(f"{real}+{imaginary}i")
    def __truediv__(self, other):
        divisor = (other.real ** 2) + (other.img** 2)
        real = round(((self.real * other.real) + (self.img * other.img)) / divisor,2)
        imaginary = round(((self.img * other.real) - (self.real * other.img)) / divisor,2)
        return ComplexNum(f"{real}+{imaginary}i")
complx1=ComplexNum(input("enter first complex number in the format a+bi: "))
complx2=ComplexNum(input("enter second complex number in the format a+bi: "))
addition = complx1 + complx2
print(f"complx1 + complx2 = {addition}")
substraction=complx1-complx2
print(f"complx1 - complx2 = {substraction}")
multiplication=complx1*complx2
print(f"complx1 * complx2 = {multiplication}")
division=complx1/complx2
print(f"complx1 / complx2 = {division}")
print("mod(complx1)=",round(math.sqrt((complx1.real**2)+(complx1.img**2)),2))
print("mod(complx2)=",round(math.sqrt((complx2.real**2)+(complx2.img**2)),2))