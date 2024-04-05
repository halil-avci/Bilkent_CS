# -*- coding: utf-8 -*-

"""
@author: CS115
"""
class Person(object):
    def __init__(self, name):
        self.__name=name
        
    def getName(self):
        return self.__name
    
    def __lt__(self,other):
        return self.__name<other.name
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.__name == other.__name
        return False
    
    def __str__(self):
        return self.__name
    
class UniversityMember(Person):
   __nextIdNum=1  # Identification Number
   
   def __init__(self, name):
       Person.__init__(self,name)
       self.__idNum = UniversityMember.__nextIdNum
       UniversityMember.__nextIdNum +=1
       
   def getIdNum(self):
       return self.__idNum
   
   def __lt__(self,other):
       return self.__idNum < other.__idNum
   
   def isStudent(self):
       return isinstance(self, Student) 

class Student(UniversityMember):
    pass

class UG(Student):
    def __init__(self, name,classYear):
       UniversityMember.__init__(self,name)
       self.__year = classYear
       
    def getClass(self):
       return self.__year

class Grad(Student):
    pass

p3=UniversityMember('Billy Bob Beaver')
p5=Grad('Buzz Aldrin')
p6=UG('Billy Beaver',1984)

print (p5, 'is a graduate student is', p5.isStudent())
print (p6, 'is an undergraduate student is', p6.isStudent())
print (p3, 'is an undergraduate student is', p3.isStudent())
