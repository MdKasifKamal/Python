class Student:
  college = "ABC College"
  name = "anonymous"  #class attribute
  def __init__(self,name):
    self.name = name #obj attr > class attr
    print("This is code of class constructor")

s1 = Student("Kasif")
print(s1.name)
print(s1.college)
s2 = Student("Kaif")
print(s2.name)
print(s2.college)

print(Student.college)  # we can access class attribute using class name also
