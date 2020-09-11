# Author: Shiao Zhuang sqz5328@psu.edu

def getGradePoint(Grade):
  if Grade == 'A': 
    Grade = 4.0
  elif Grade == 'A-': 
    Grade = 3.67
  elif Grade == 'B+': 
    Grade = 3.33
  elif Grade == 'B': 
    Grade = 3.0
  elif Grade == 'B-': 
    Grade = 2.67
  elif Grade == 'C+': 
    Grade = 2.33
  elif Grade == 'C': 
    Grade = 2.0
  elif Grade == 'D': 
    Grade = 1.0
  else : 
    Grade = 0.0
  return Grade


def run():
  Grade = input("Enter your course 1 letter grade: ")
  C1 = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {getGradePoint(Grade)}")
  P1 = float(getGradePoint(Grade))

  Grade = input("Enter your course 2 letter grade: ")
  C2 = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {getGradePoint(Grade)}")
  P2 = float(getGradePoint(Grade))

  Grade = input("Enter your course 3 letter grade: ")
  C3 = float(input("Enter your course 3 credit: "))
  print(f"Grade point for course 3 is: {getGradePoint(Grade)}")
  P3 = float(getGradePoint(Grade))

  print(f"Your GPA is: {(C1*P1+C2*P2+C3*P3)/(C1+C2+C3)}")
  
if __name__ == "__main__":
  run()