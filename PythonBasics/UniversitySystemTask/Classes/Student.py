class Student:
  courses=[]

  def __init__(self,name,id,major,birthDate):
    self.name = name
    self.id = id
    self.major = major
    self.birthDate = birthDate
    self.courses = []
  
  def printStudentInfo(self):
    print(f"Student name is {self.name}. His/Her major is {self.major}. His/Her ID is {self.id}. His/Her birthdate is {self.birthDate}")
  
  def printStudentCourse(self):
    if len(self.courses) == 0:
      print(f"Student name is {self.name}. This student doesn't have courses yet!!")
    elif len(self.courses) == 1:
      print(f"Student name is {self.name}. This student's course is {self.courses[0].name}")
    else :
      StudentCourses = []
      for course in self.courses:
        StudentCourses.append(course.name)
      print(f"Student name is {self.name}. This student's courses are {StudentCourses}")
  
  def registerCourse(self,course):
    self.courses.append(course)
    course.students.append(self)

