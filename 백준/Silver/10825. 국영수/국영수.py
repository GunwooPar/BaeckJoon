import sys

input = sys.stdin.readline

class Student:
    def __init__(self,name,korean,english,math): 
        self.name = name
        self.korean = int(korean)
        self.english = int(english)
        self.math = int(math)







# main function

N = int(input())

student_list = []

for _ in range(N):
    name, korean, english, math = input().split()

    student_list.append(Student(name,korean,english,math))

student_list.sort(key=lambda stu:(-stu.korean,stu.english,-stu.math,stu.name))


for student in student_list:

    print(student.name)

