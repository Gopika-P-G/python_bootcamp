student_heights = input("Enter list of student heights: ")
student_heights= student_heights.split() 

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_student_height=0
for height in student_heights:
    total_student_height+=height

  
total_student = 0
for student in student_heights:
    total_student+=1
    
average_height = total_student_height/total_student
print(round(average_height))