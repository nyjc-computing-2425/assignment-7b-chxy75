# Built-in imports
import math

# Your code below
GRADE = {}
for score in range(0,40):
    GRADE[score] = 'U'
for score in range(40,45):
    GRADE[score] = 'S'
for score in range(45,50):
    GRADE[score] = 'E'
for score in range(50,55):
    GRADE[score] = 'D'
for score in range(55,60):
    GRADE[score] = 'C'
for score in range(60,70):
    GRADE[score] = 'B'
for score in range(70,101):
    GRADE[score] = 'A'


def read_testscores(filename: str) -> list:
    """
    Opens the CSV filename and returns student data as a list of dicts

    Parameters
    ----------
    filename : str
        The name of the CSV file to read

    Returns
    -------
    list
        A list of dicts with the student data

    Usage:
    studentdata = read_testscores(filename)
    """
    studentdata = []
    with open(filename,'r') as f:
        headers = f.readline().strip()  # Don't need to process header
        for line in f:
            class_, name, p1, p2, p3, p4 = line.split(',')
            p1, p2, p3, p4 = float(p1), float(p2), float(p3), float(p4)
            overall = 0
            for i in range(4):
                score = (p1,p2,p3,p4)[i]
                max_ = (30,40,80,30)[i]
                weight = (15,30,35,20)[i]
                overall += score / max_ * weight
            student = {'class': class_,
                       'name': name,
                       'overall': math.ceil(overall),
                       'grade': GRADE[math.ceil(overall)]}
            studentdata.append(student)
    return studentdata

def analyze_grades(studentdata: list) -> dict:
 """
Analyzes the student data and returns a dict of class: {grade: count}

Parameters
----------
studentdata : list
    A list of dicts with the student data

Returns
-------
dict
    A nested dict in the form {class: {grade: count}, ...}
 """
 analysis = {}
 for student in studentdata:
      class_ = student['class']
      grade = student['grade']
      if class_ not in analysis:
        analysis[class_] = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'S':0, 'U':0}

      if grade in analysis[class_]:
        analysis[class_][grade] += 1

 return analysis