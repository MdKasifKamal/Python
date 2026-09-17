class Student:
  def __init__(self, fullname):
    self.name = fullname
    print("This is code of class constructor")

s1 = Student("Kasif")
print(s1.name)
s2 = Student("Kaif")
