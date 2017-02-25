'''
from collections import namedtuple

#Student=namedtuple('Student','ID, MARKS, CLASS, NAME')
totalStudents=input()
coumnNames=map(str, raw_input().split())
print totalStudents
print ','.join(coumnNames)
Student=namedtuple('Student',','.join(coumnNames))

for j in xrange(totalStudents):
'''
from collections import namedtuple

n = int(input())
rec = namedtuple('Record', raw_input().split())
s = 0
for i in range(n):
    a = rec(*raw_input().split())
    print a
    s += int(a.MARKS)
print(s / float(n))