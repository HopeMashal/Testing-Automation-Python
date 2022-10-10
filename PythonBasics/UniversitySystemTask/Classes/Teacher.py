class Teacher:
  def __init__(self,name,id,courses='none'):
    self.name = name
    self.id = id
    self.courses = courses
  
  def printTeacherInfo(self):
    print(f"Teacher name is {self.name}. His/Her ID is {self.id}.")
  
  def printTeacherCourse(self):
    if self.courses == 'none':
      print(f"This teacher doesn't have courses yet!!")
    elif len(self.courses) == 1:
      print(f"This teacher's course is {self.courses}")
    else :
      print(f"This teacher's courses are {self.courses}")