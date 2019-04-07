#!/usr/bin/env python3
"""Student answers generator
@requires: random
@return ans_list: a list of student answers"""

import random

def create_ans_list(n=10):
    """@param int n: number of answers, default = 10"""
    options = ['a', 'b', 'c', 'd']
    ans_list = list()
    super_random = random.SystemRandom()  # criptographycally secure random.
    for i in range(n):
        student_answer = super_random.choice(options)
        ans_list.append(student_answer)

    if len(ans_list) == n:
        return ans_list
    else:
        raise Exception("answer list is not equal to n")

def write_to_file(which_file, n):
    """@params str which_file: filename
       @params int n: """
    with open(which_file, 'w') as outfile:
        for i in range(n):
            ans_list = create_ans_list()
            outfile.write(str(ans_list) + "\n")
        return

def student_ans_main():
    """Creates 10 lists of 10 random student answers
    """
    write_to_file("student_answers.txt", 10)

# student_ans_main()                                                  # Uncomment this line for running
