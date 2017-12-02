#!/usr/bin/env python3

if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    student_marks = {}
    query_name = "Malika"
    student_marks['Krishna'] = list(map(float, "67 68 69".split()))
    student_marks['Arjun'] = list(map(float, "70 98 63".split()))
    student_marks['Malika'] = list(map(float, "52 56 60".split()))
    student_mark = sum(student_marks[query_name])/3
    print("{0:.2f}".format(student_mark))
