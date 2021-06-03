def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >=0 and grades[i]<=100:
            if grades[i]>=35 and grades[i]<=100:
                if abs(grades[i]- ((grades[i]//5)+1)*5) < 3:
                    grades[i] = ((grades[i]//5)+1)*5
                                     
    for i in grades:
        print(i)

    

if __name__ == '__main__':
    n = int(input('Please enter no of students: '))
    students_grade_list=[]
    for i in range(n):
        grade=int(input())
        students_grade_list.append(grade)
    gradingStudents(students_grade_list)    