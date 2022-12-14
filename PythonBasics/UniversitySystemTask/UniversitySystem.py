# python -m venv .venv >> Create Virtual Environment

from Classes.Course import Course
from Classes.Teacher import Teacher
from Classes.Student import Student


if __name__ == '__main__':
  teacher_1 = Teacher("Ahmad","1234")
  teacher_1.printTeacherInfo()
  teacher_2 = Teacher("Sami","2345")
  teacher_2.printTeacherInfo()
  teacher_3 = Teacher("Amal","3456")
  teacher_3.printTeacherInfo()

  course_1 = Course("Math",3)
  course_1.printCourseInfo()
  teacher_1.assignToCourse(course_1)
  course_1.printTeacher()
  course_2 = Course("Art",2)
  course_2.printCourseInfo()
  teacher_1.assignToCourse(course_2)
  course_2.printTeacher()
  course_3 = Course("Engineering",5)
  course_3.printCourseInfo()
  teacher_2.assignToCourse(course_3)
  course_3.printTeacher()
  course_4 = Course("English",3)
  course_4.printCourseInfo()
  teacher_2.assignToCourse(course_4)
  course_4.printTeacher()
  course_5 = Course("Arabic",2)
  course_5.printCourseInfo()
  teacher_3.assignToCourse(course_5)
  course_5.printTeacher()
  course_6 = Course("Japanese",1)
  course_6.printCourseInfo()
  teacher_3.assignToCourse(course_6)
  course_6.printTeacher()
  teacher_1.printTeacherCourse()
  teacher_2.printTeacherCourse()
  teacher_3.printTeacherCourse()

  student_1 = Student("Hope","9876","Art","19/12/1990")
  student_1.registerCourse(course_2)
  student_1.registerCourse(course_4)
  student_1.printStudentInfo()
  student_1.printStudentCourse()
  student_2 = Student("Yuki","9874","Engineering","12/12/1990")
  student_2.registerCourse(course_1)
  student_2.registerCourse(course_3)
  student_2.printStudentInfo()
  student_2.printStudentCourse()
  student_3 = Student("Akira","9871","Arabic","17/12/1990")
  student_3.registerCourse(course_5)
  student_3.printStudentInfo()
  student_3.printStudentCourse()
  student_4 = Student("Mira","9870","English","13/12/1990")
  student_4.registerCourse(course_4)
  student_4.printStudentInfo()
  student_4.printStudentCourse()
  student_5 = Student("Samia","9879","Japanese","29/12/1990")
  student_5.registerCourse(course_6)
  student_5.printStudentInfo()
  student_5.printStudentCourse()
