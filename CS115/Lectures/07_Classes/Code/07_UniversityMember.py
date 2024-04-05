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
        return self.__name<other.__name
    
    def __str__(self):
        return self.__name 
    
class UniversityMember(Person):
   
   def __init__(self, name, idnum):
       Person.__init__(self,name)
#       super().__init__(self,name)
       self.__idNum = idnum

       
   def getIdNum(self):
       return self.__idNum
   
   def __lt__(self,other):
       return self.__idNum < other.__idNum
   
#   def __str__(self):
#       return Person.__str__(self) + ' '+ str(self.__idNum)

#   def __str__(self):
#       return self.getName() + ' '+ str(self.__idNum)



p1 = UniversityMember('Barbara Beaver', 45678)
p2 = UniversityMember('Alexis Smith', 75678)

print( p1 )