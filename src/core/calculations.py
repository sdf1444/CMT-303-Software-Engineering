#!/usr/bin/env python3

"""Calculations functions"""

import json

def make_json(*grade):
    data = {"CMT-100" : {
        "0" : { "grades" : list(grade)}
    }}
    with open("data/marks.json", "w") as infile:
        json.dump(data, infile, indent=4)

def perc_pass(marks = [23, 56, 54, 76, 67, 65, 34, 76, 34, 76]):
    fifty_plus = 0
    less_than_fifty = 0
    for i in marks:
        if i < 50:
            less_than_fifty += 1
        elif i >= 50:
            fifty_plus += 1

    print(fifty_plus, less_than_fifty)

def avg_mark(marks = [23, 56, 54, 76, 67, 65, 34, 76, 34, 76]):

    mark_sum = 0
    mark_avg = 0

    for i in marks:
        mark_sum += i
    mark_avg = mark_sum / (len(marks))
    return mark_avg

def switch_marks( marks=[23, 56, 54, 76, 67, 65, 34, 76, 34, 76]):

    failure = 0
    passed = 0
    merit = 0
    distintion = 0
    for m in marks:
        if m < 50:
            failure += 1
        elif m > 50 and  m < 60:
            passed += 1
        elif m >= 60 and m < 70:
            merit += 1
        elif m >= 70:
            distintion += 1

    return (failure, passed, merit, distintion)


def main():
    marks = [23, 56, 54, 76, 67, 65, 34, 76, 34, 76]
    make_json(marks)
