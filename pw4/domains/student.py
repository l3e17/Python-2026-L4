import math
import numpy as np


class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def get_gpa(self, courses, marks):
        scores = []
        credits = []
        for c in courses:
            ma_mon = c.name
            if ma_mon in marks and self.id in marks[ma_mon]:
                scores.append(marks[ma_mon][self.id])
                credits.append(c.credits)
                
        if len(scores) == 0:
            return 0.0
            
        np_scores = np.array(scores)
        np_credits = np.array(credits)
        gpa = np.dot(np_scores, np_credits) / np.sum(np_credits)
        return math.floor(gpa * 10) / 10