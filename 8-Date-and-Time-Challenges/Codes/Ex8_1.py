#!/usr/bin/env python3
import calendar

def find_weekday(input_date):
    date_sep = input_date.split()
    print(calendar.day_name[calendar.weekday(int(date_sep[2]), int(date_sep[0]), int(date_sep[1]))].upper())

if __name__ == '__main__':
    input_date = input() #mm dd yyyy
    find_weekday(input_date)
