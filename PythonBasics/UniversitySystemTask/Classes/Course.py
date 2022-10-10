class Course:
  teacher = 'none'
  students = []

  def __init__(self,name,numOfHours):
    self.name = name
    self.numOfHours = numOfHours
  
  def printCourseInfo(self):
    print(f"Course name is {self.name}. Its number of hours is {self.numOfHours}.")
  
  def printStudentsList(self):
    if self.students == 'none':
      print(f"Course name is {self.name}. This course doesn't have students yet!!")
    elif len(self.students) == 1:
      print(f"Course name is {self.name}. The student of this course is {self.students[0].name}")
    else :
      CourseStudents = []
      for student in self.students:
        CourseStudents.append(student)
      print(f"Course name is {self.name}. The students of this course are {CourseStudents}")
  
  def printTeacher(self):
    print(f"Course name is {self.name}. The teacher of this course is {self.teacher.name}")
  
