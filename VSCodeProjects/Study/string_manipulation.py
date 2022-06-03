course = 'Python for beginners'

print(course.upper()) #uppers all
print(course.lower())
print(course)
print(course.title()) #upper just firts letters

print(course.find('P')) #starts with 0, sensitive to lower and upper case.
print(course.find('O')) # -1 because dont exist.
print(course.find('beginners')) #starts at 11.

print(course.replace('beginners', 'absolute beg.')) #whats replace, sensitive as well.
print(course.replace('P', 'j'))

print('Python' in course) # if is inside and produces bollian value.
print('python' in course) # sensitive.

print(len(course)) #number os characters in course.