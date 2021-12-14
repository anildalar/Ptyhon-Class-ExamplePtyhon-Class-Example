
#1. Lets Create the class Defination
class MyClass():
    #1. Property
    name="Anil"
    #2. Constructor
    #3. Method
    def hello5(self,std,**kwargs): # Self is internal referece to the current class object
        print(f"Hello {self.name},How are you? ")
        print(f"Hello {std},How are you? ")
        print(f"Hello {kwargs['friend1']},How are you? ")

#2. Lets create the class Object

# objectname = ClassName()

myobject = MyClass()

# Now you can access the class Members

# objectname.membername

# objectname.method()

myobject.hello5("Deepak",friend1="Sunil") 
