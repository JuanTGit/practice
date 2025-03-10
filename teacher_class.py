# User Defined Class
# Gradebook for a teacher
# 3 attributes
# subject = string , teacher  = string , gradebook = {"Nate": [100,90,20], "Mark": [100,100,100]}

# Method 1:
# method to add a new student to the gradebook

# Method 2:
# add a new score to the gradebook given a student name

# Method 3:
# calculate a student's avg score given a name

# Method 4:
# calculate overall class average

class Gradebook:
    def __init__(self, subject, teacher, gradebook={}):
        self.subject = subject
        self.teacher = teacher

    def add_student(self):
        pass