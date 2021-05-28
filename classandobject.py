#To Create A Class

class MyClass:
  x = 5

print(MyClass)

#To Create a Object
class MyClass:
      x = 5

p1 = MyClass()
print(p1.x)

#Init() function
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Amit", 36)

print(p1.name)
print(p1.age)


#Object Method
class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def myfunc(self):
         print("Hello my name is " + self.name)

p1 = Person("Amit", 36)
p1.myfunc()

#Self Parameter
class Person:
      def __init__(mysillyobject, name, age):
          mysillyobject.name = name
          mysillyobject.age = age

      def myfunc(abc):
          print("Hello my name is " + abc.name)

p1 = Person("Amit", 36)
p1.myfunc()


#Modify Object Properties
class Person:
      def __init__(self, name, age):
         self.name = name
         self.age = age

      def myfunc(self):
         print("Hello my name is " + self.name)

p1 = Person("Amit", 36)

p1.age = 40

print(p1.age)



#Delete Object Properties
class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age

      def myfunc(self):
         print("Hello my name is " + self.name)

p1 = Person("Amit", 36)

del p1

print(p1)

#Padss Statement
class Person:
      pass

# having an empty class definition like this, would raise an error without the pass statement





