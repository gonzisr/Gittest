# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 10:48:42 2016

@author: Israel
"""
from assignments import MaxSizeList, Createbook   # assumes "class MaxSizeList"
                                   # is in a script called "assignments.py"
book = Createbook("fly guy", "isreal", "hello", "hardcover")




"""
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
"""

"""
class Instancecounter(object):
    count = 0
    
    def __init__(self,val):
        self.val = val
        Instancecounter.count +=1
        
    def set_val(self, newval):
        self.val = newval
        
    def get_Val(self):
        return self.val
    
    def get_count(self):
        return Instancecounter.count
        
        
a = Instancecounter(125)
b = Instancecounter(456)
c = Instancecounter(675)

for obj in (a,b,c):
    print "val of object : %s" %( obj.get_Val())
    print "count: %s" %(obj.get_count())
"""        
