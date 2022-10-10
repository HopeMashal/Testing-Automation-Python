class Course:
  def __init__(self,name,numOfHours,teacher,students='none'):
    self.name = name
    self.numOfHours = numOfHours
    self.teacher = teacher
    self.students = students