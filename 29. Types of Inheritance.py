# Inheritance is the ability 
# to define a new class(child class) that is a modified version of an existing class(parent class)"

# Matlab kii humne kisi nayi class ko banakar uske under koi purani class ke attributes gather kr liye

"""
Types of Inheritance
1. Singhle Inheritance 
2. Multiple Inheritance
3. Multilevel Inheritance
"""

# Single Inheritance
# Matlab kisi single Class ne kisi ek class se properties inherit ki hai
# Example
class Parent():
    def first(self):
        print('\nParent function')
        
class Child(Parent): #(Parent) specifies that we have inherited the propertis of the "Parent" class.
    def second(self):
        print('Child function')

object1 = Child()
object1.first()
object1.second()

# Multiple Inheritance
# Matlab kisi single Class ne do ya do se jyada class se properties inherit ki hai
# Example
class Base1:
      def func1(self):
            print("\nThis is Base1 class")
class Base2:
      def func2(self):
            print("This is Base2 class")

class Child(Base1 , Base2):
      def func3(self):
            print("This is Base3 class")

obj = Child()
obj.func1()
obj.func2()
obj.func3()



# Multilevel Inheritance
# Matlab kisi class ne kisi esi class se properties inherit ki jisne khud hi kisi se property inherit kri hai 
# Example

class level1:
      def first(self):
            print ('\nCode')

class level2(level1): #inherit level1
      def second(self):
             print ('With')

class level3(level2): #inherit level2
      def third(self):
            print ('Harry')

obj=level3()
obj.first()
obj.second()
obj.third()