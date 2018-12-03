#!/usr/bin/env python3

def find_second_lowest(students_list):
    lowest_student = min(students_list, key=lambda x: x[1])
    second_lowest_student =  min([student for student in students_list if student[1] != lowest_student[1]], key=lambda x: x[1])
    sub_student = sorted([student[0] for student in students_list if student[1] == second_lowest_student[1]])
    print('\n'.join(sub_student))


if __name__ == '__main__':
    # students_list = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students_list.append([name, score])
    students_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    find_second_lowest(students_list)
