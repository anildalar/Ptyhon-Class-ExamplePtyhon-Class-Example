class Parent():#PascalCase
    #1.Property
    name1 = "ParentName"
    #2.Constructor

    #3.Method
    def helloParent(self): #camelCase
        print("Hello "+self.name1+", How are you ?")

class Child(Parent): # PascalCase
    #1. Property
    name2 = "Khushansh"
    surname=""
    #2. Constructor
    def __init__(self,surname='DEVRIYA'): # The role of constructor is to initialize the members
        self.surname = surname

    #3. Method
    def helloChild(self): # camelCase
        print("Hello {} {}, How are you".format(self.name2,self.surname)) #3.6



#o = Parent()

#o.hello1()

# Lets define a  Class

childobject = Child("DOLLOR")
childobject.helloChild()

childobject.helloParent() #inheritance


# Parent/Base Class
# Child/Derived Class 
