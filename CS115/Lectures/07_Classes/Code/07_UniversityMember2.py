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
        return self.__name < other.__name
    
    def __str__(self):
        return self.__name
    
class UniversityMember(Person):
   nextIdNum=10000  # Identification Number
   
   def __init__(self, name):
       Person.__init__(self,name)
       self.__idNum = UniversityMember.nextIdNum
       UniversityMember.nextIdNum +=1
       
   def getIdNum(self):
       return self.__idNum
   
   def __lt__(self,other):
#       if isinstance(other, UniversityMember):
           return self.__idNum < other.__idNum
#       return False
   
   def __str__(self):
        return Person.__str__(self)+' '+str(self.__idNum)
   

p1=UniversityMember('Mark Guttag')
p2=UniversityMember('Billy Bob Beaver')
p3=UniversityMember('Billy Bob Beaver')
p4=Person('Billy Bob Beaver')

#print ('p1 < p2 = ', p1 < p2)
#print ('p3 < p2 = ', p3 < p2)
#print ('p4 < p1 = ', p4 < p1)