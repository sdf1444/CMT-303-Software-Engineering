#!/usr/bin/env python3

import json
from matplotlib import pyplot as plt
from math import sqrt
import numpy as np
import random

"""Ancillary functions """

def load_modules_1(quiz="Core/data/quizes.json"):
    with open(quiz, "r") as readfile:
        load = json.load(readfile)
    WHERE_IS_MODULES = load["Tests"]["modules"]
    module_list = list(WHERE_IS_MODULES.keys())
    return module_list

def load_modules():
    modules_list = ["Python", "Java", "Computational Systems", "Web Development"]
    return modules_list

def load_test_ids(moduleID):
    if moduleID == "Python":
        return ["General Knowledge"]
    if moduleID == "Java":
        return ["Capital Cities"]

def load_test_ids_1(moduleID, quiz="Core/data/quizes.json"):
    with open(quiz, "r") as readfile:
        load = json.load(readfile)
    WHERE_IS_TEST_ID = load["Tests"]["modules"][moduleID]
    test_list = list(WHERE_IS_TEST_ID.keys())
    return(test_list)

"""==================================================================
MATPLOTLIB
=================================================================="""

CLASIFICATION_GRADES = ["Fail", "Pass", "Merit", "Dist."]

def grade_generator(n=1001):
    grades_list = list()
    while len(grades_list) < n:
        ri = random.randrange(0,101, 10)
        if ri < 50:
            toss = random.randint(0,16)
            if toss == 0:
                grades_list.append(ri)
            else:
                continue
        elif ri > 59 and ri < 70:
            toss = random.randint(0,1)
            if toss ==0:
                grades_list.append(ri)
            else:
                continue
        elif ri > 69:
            toss = random.randint(0,8)
            if toss == 0:
                grades_list.append(ri)
            else:
                continue
        else:
            grades_list.append(ri)
    return grades_list

def java_grade_generator(n=1001):
    grades_list = list()
    while len(grades_list) < n:
        ri = random.randrange(0,101, 10)
        if ri < 50:
            toss = random.randint(0,1)
            if toss == 0:
                grades_list.append(ri)
            else:
                continue
        elif ri >= 50 and ri < 60:
            toss = random.randint(0,8)
            if toss == 0:
                grades_list.append(ri)
        elif ri > 59 and ri < 70:
            toss = random.randint(0,8)
            if toss ==0:
                grades_list.append(ri)
            else:
                continue
        elif ri > 69:
            toss = random.randint(0,1)
            if toss == 0:
                grades_list.append(ri)
            else:
                continue
        else:
            grades_list.append(ri)
    return grades_list


def classify_grades(grades_list):
    fail_sum = 0
    pass_sum = 0
    merit_sum = 0
    dist_sum = 0

    for i in grades_list:
        if i < 50:
            fail_sum += 1
        elif i >=50 and i < 60:
            pass_sum += 1
        elif i >= 60 and i < 70:
            merit_sum += 1
        elif i >= 70:
            dist_sum += 1
    return [fail_sum, pass_sum, merit_sum, dist_sum]

def _mu(grades_list):
    a = 0
    for i in grades_list:
        a += i
    return a / len(grades_list)

def _sigma_mu(mean, grades_list):
    a = list()
    b = 0
    for i in grades_list:
        a.append((i - mean) ** 2.0)
    for i in a:
        b += i
    return sqrt( b / len(a))



def make_plot():

    kilo_grade = java_grade_generator()
    grades = classify_grades(kilo_grade)
    plt.figure(2, figsize=(7,3))
    plt.subplot(131)
    plt.bar(CLASIFICATION_GRADES, grades,color=['firebrick', 'royalblue', 'forestgreen', 'gold'])
    plt.subplot(133)

    mu = _mu(kilo_grade)
    sigma = _sigma_mu(mu, kilo_grade)

    n, bins, patch = plt.hist(kilo_grade, bins=10, density=True)
    plt.title(r'Grades Hist., $\mu$={:3.3f}, $\sigma$={:3.3f}'.format(mu, sigma), fontsize=8)

    plt.xticks(range(0,101, 10), fontsize=7)

    y = (( 1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
    plt.plot(bins, y, '--r')


    plt.suptitle('Results')
    # plt.style.use("seaborn-paper")


    plt.savefig('core/data/pltfigure_python.png')
    plt.show()                  # DEBUG LINEx

# make_plot()
