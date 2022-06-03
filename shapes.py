import math


class Circle:
    def __init__(self,r):
        self.r=r 
       
        
    def area(self):
        A=math.pi*(self.r**2)
        return A

    def circumferance(self):
        c=2*math.pi*self.r
        return c

class Square:
    def __init__(self,a):
        self.a=a 

    def square_area(self):
        A=(self.a*self.a)  
        return A
    def perimeter(self):
        p=4*self.a  
        return p

class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l

    def area_rectangle(self):
        A=self.w*self.l
        return A 

    def perimeter(self):
        p=2*(self.l+self.w)
        return p    

class Sphere:
    def __init__(self,r):
        self.r=r
       
    def Surface_area(self):
        A=4*math.pi*(self.r*self.r)  
        return A  

    def Volume(self):
        V= 4/3*(math.pi*self.r*self.r*self.r)
        return V





        
