class Car:  # abstract class means hide unnecessary things from the user and show only the necessary things to the user
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False

  def start(self):
    self.acc = True
    self.brk = False
    self.clutch = True
    print("Car is started")
car1 = Car()
car1.start()