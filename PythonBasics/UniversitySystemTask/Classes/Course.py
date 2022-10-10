class Course:
  teacher = 'none'
  students = []

  def __init__(self,name,numOfHours,teacher,students):
    self.name = name
    self.numOfHours = numOfHours
    self.teacher = teacher
    self.students.extend(students)
  
  def printCourseInfo(self):
    print(f"Course name is {self.name}. Its number of hours is {self.numOfHours}.")
  
  def printStudentsList(self):
    if self.students == 'none':
      print(f"This course doesn't have students yet!!")
    elif len(self.students) == 1:
      print(f"The student of this course is {self.students}")
    else :
      print(f"The students of this course are {self.students}")
  
  def printTeacher(self):
    print(f"The teacher of this course is {self.teacher}")
