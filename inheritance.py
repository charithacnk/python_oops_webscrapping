"""
"INHERITANCE"
single inheritance
multi level inheritance
multiple inheritance
hirarical inheritance

"""

# class parent():
#     def output(self):
#         print("I am the parent")

# class child(parent):
#     def outputc(self):
#         print("I am the child")

# c=child()
# c.outputc()
# c.output()


# class Grandfather():
#     def outputgf(self):
#         print(" I am Grandfather")

# class parent2(Grandfather):
#     def outputp2(self):
#         print(" I am father")

# class child(parent2):
#     def outputc(self):
#         print("I am Child")

# c=child()

# c.outputc()#child method

# c.outputgf()
# c.outputp2()


# class mother():
#     def outputm(self):
#         print(" I am mother")

# class father():
#     def outputf(self):
#         print(" I am father")

# class child(mother, father):
#     def outputc(self):
#         print("I am Child")

# c=child()
# c.outputm()
# c.outputf()

class mother():
    def outputm(self):
        print(" I am mother")

class child1(mother):
    def outputc1(self):
        print(" I am child1")

class child2(mother):
    def outputc2(self):
        print("I am Child2")

class child3(mother):
    def outputc3(self):
        print("I am Child3")

c1=child1()
c2=child2()
c3=child3()

c1.outputc1()
c2.outputc2()
c3.outputc3()
c2.outputm()