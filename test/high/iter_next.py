import os
import sys


liters = ['a','b','c']

i =iter(liters)

print(next(i))
print(next(i))




testlist = ['Linux', 'Java', 'Python', 'DevOps', 'Go']

it = iter(testlist)
print("Loop Start...")
while True:
    try:
        course = next(it)
        print(course)
    except StopIteration:
        print("Loop End")
        sys.exit(0)      #程序终止