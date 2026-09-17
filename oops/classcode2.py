class Student:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks
  @staticmethod # decorator 
  def hello():
      print("Hello from class method")
  def get_avg(self):
     sum = 0
     for val in self.marks:
       sum += val
     print("Hi",self.name,"your avg is:",sum/3)

s1 =Student("Kasif",[90,80,70])
s1.get_avg()
s1.hello()