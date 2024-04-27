"""
variables and methods in to single unit

public
private__
protected_
"""

# class demo():
#     __a=2 #private
#     _b=4 #protected
#     print(__a)
#     print(_b)

#data encapsulation

# class demo():
#     def __init__(self,a,b):# so that we access anywhere
#         self.__a=a #private
#         self._b=b #protected
# class demo1(demo):
#     def output(self):
#         print(self.__a)

# d=demo1(3,4)
# d.output()

# polymorphism
def add(a,b):
    print(a+b)
add(1,2)
add('a','b')
add([3,4],[5,6])
add((3,4),(5,6))