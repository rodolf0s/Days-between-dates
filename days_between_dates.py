#!/usr/bin/python

import sys


def leap_year(year):
    if ((year % 4 == 0 and not year % 100 == 0) or year % 400 == 0):
        return 366
    return 365


def day_month(month, year):
    if month > 0 and month < 8:
        if month % 2 == 0:
            if month != 2:
                return 30
            else:
                if leap_year(year) == 366:
                    return 29
                else:
                    return 28
        else:
            return 31
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30


def sum_month(month):
    result = 0
    while month >= 1:
        result = result + day_month(month)
        month = month - 1
    return result


def sum_years(year1, year2):
    sum_years = 0
    while year1 < year2:
        sum_years = sum_years + leap_year(year1)
        year1 = year1 + 1
    return sum_years


def sum_to_end(month, year, to_month = 12):
    sum_month = 0
    while month <= to_month:
        sum_month = sum_month + day_month(month, year)
        month = month + 1
    return sum_month


def sum_to_begin(month, year):
    sum_month = 0
    while month > 0:
        sum_month = sum_month + day_month(month, year)
        month = month - 1
    return sum_month


def days_between_dates(year1, month1, day1, year2, month2, day2):
    days = 0
    if year1 < year2:
        days = sum_to_end(month1, year1) - day1
        year1 = year1 + 1
        if year1 == year2:
            days = days + (sum_to_begin(month2 - 1, year2) + day2)
        else:
            days = days + sum_years(year1, year2)
            days = days + (sum_to_begin(month2 - 1, year2) + day2)
    else:
        days = sum_to_end(month1, year1, month2 - 1) - day1 + day2
            
    return days

# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print("Test case Failed!")
        else:
            print("Test case passed!, result = {0:d}".format(result))

#test()

def main(argv):
    if len(argv) == 6:
        print("The number of days is %d" % 
            days_between_dates(
                int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]),
                int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])))
    else:
        print("The number of arguments must be 6")
        print("Example: \n$ python days_between_dates.py 1900 1 1 1999 12 31")

if __name__ == "__main__":
   main(sys.argv[1:])
  
