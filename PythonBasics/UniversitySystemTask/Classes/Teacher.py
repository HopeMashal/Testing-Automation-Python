class Teacher:
  courses=[]

  def __init__(self,name,id):
    self.name = name
    self.id = id
    self.courses = []
  
  def printTeacherInfo(self):
    print(f"Teacher name is {self.name}. His/Her ID is {self.id}.")
  
  def printTeacherCourse(self):
    if len(self.courses) == 0:
      print(f"Teacher name is {self.name}. This teacher doesn't have courses yet!!")
    elif len(self.courses) == 1:
      print(f"Teacher name is {self.name}. This teacher's course is {self.courses[0].name}")
    else :
      TeacherCourses = []
      for course in self.courses:
        TeacherCourses.append(course.name)
      print(f"Teacher name is {self.name}. This teacher's courses are {TeacherCourses}")
  
  def assignToCourse(self,course):
    self.courses.append(course)
    course.teacher = self