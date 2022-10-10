class Student:
  def __init__(self,name,id,major,birthDate,courses='none'):
    self.name = name
    self.id = id
    self.major = major
    self.birthDate = birthDate
    self.courses = courses
  
  def printStudentInfo(self):
    print(f"Student name is {self.name}. His/Her major is {self.major}. His/Her ID is {self.id}. His/Her birthdate is {self.birthDate}")
  
  def printStudentCourse(self):
    if self.courses == 'none':
      print(f"This student doesn't have courses yet!!")
    elif len(self.courses) == 1:
      print(f"This student's course is {self.courses}")
    else :
      print(f"This student's courses are {self.courses}")

