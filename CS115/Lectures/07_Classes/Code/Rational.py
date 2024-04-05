# -*- coding: utf-8 -*-
"""
@author: CS115
"""

class Rational:
    def __init__(self,num,denom):
        self.__numerator=num
        if denom==0:
            denom=1
        elif denom<0:
             self.__numerator=-self.__numerator
             denom=-denom
        self.__denominator=int(denom)
        self.__numerator=int(self.__numerator)
        self.reduce()
         
    def reduce(self):
        if self.__numerator != 0:  
            common = gcd (abs(self.__numerator), self.__denominator)
            self.__numerator = self.__numerator // common
            self.__denominator = self.__denominator // common

    def reciprocal(self):
        return Rational(self.__denominator, self.__numerator); 
    
    def __add__(self,y):
        commonDenominator = self.__denominator * y.__denominator 
        numerator1 = self.__numerator * y.__denominator 
        numerator2 = y.__numerator  * self.__denominator 
        total = numerator1 + numerator2

        return Rational(total,commonDenominator)
    
    def __sub__(self,y):
        commonDenominator = self.__denominator * y.__denominator 
        numerator1 = self.__numerator * y.__denominator 
        numerator2 = y.__numerator  * self.__denominator 
        total = numerator1 - numerator2

        return Rational(total,commonDenominator)   
    
    def __mul__(self,y):
        numer = self.__numerator * y.__numerator
        denom = self.__denominator * y.__denominator

        return Rational(numer, denom)
    
    def __truediv__(self,y):
        return self.__mul__(y.reciprocal())
    
    def __eq__(self,y):
        return self.__numerator == y.__numerator and self.__denominator==y.__denominator
    
    def __lt__(self,y):
        return(self.__numerator*y.__denominator < self.__denominator*y.__numerator)
        
    def __gt__(self,y):
        return y<self
    
    def __str__(self):
       if self.__numerator == 0:
            return str(0)
       elif self.__denominator ==1:
            return str(self.__numerator)
       else:
            return str(self.__numerator)+"/"+str(self.__denominator)
     
    def __repr__(self):
        if self.__numerator == 0:
            return str(0)
        elif self.__denominator ==1:
            return str(self.__numerator)
        else:
            return str(self.__numerator)+"/"+str(self.__denominator)      

    
def gcd(num1,num2):
        while num1 != num2:
             if num1 > num2:
                 num1 = num1 - num2
             else:
                 num2 = num2 - num1
        return num1       
  