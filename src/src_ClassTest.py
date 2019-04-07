#!/usr/env python3
import random
import json

class Test:
    """Main Test Superclass.
    ========================================
    Contains the main TEST class and methods for writing the JSON databse into file
    :param name: String name of the test
    :param testOD: String ID of the test
    :param module: String name of the module for which the test belongs to.
    ========================================
    """

    def __init__ (self, name, testID, module):
        self.name = name
        self.testID = testID
        self.module = module
        self.Questions = {}
        self.testName = self.testNameGenerator()

    def addQuestion(self, is_save, question_number, question, correct, *wrong,mark='1',feedback=""):
        """Adds a Questions with four answers.
        :param question: String question for the test
        :param correct: String correct answer for this
        :param *wrong: list(String) contains all wrong answers"""

        self.question = question
        self.correct = correct
        self.wrong = list(wrong)
        if len(self.wrong) != 3:
                raise Exception ("Number of wrong answers needed: 3. Provided: {}".format(len(self.wrong)))

        options = ["a","b","c","d"]
        r = random.randint(0,3)
        if r == 0: letter = "a"
        if r == 1: letter = "b"
        if r == 2: letter = "c"
        if r == 3: letter = "d"

        wrong_shuffle = random.sample(wrong, len(wrong))
        options.remove(letter)
        wrong_letters = list(zip(wrong_shuffle, options))
        # print(wrong_letters)  #debug info
        print(is_save, 'issave=====>')
        print(question_number, 'question number =====>')
        if len(self.Questions) == 0:
        	if is_save:
        		self.Questions[0+1] =  {"q" : str(question), "correctA":[correct, letter], "wrongAs": wrong_letters,"mark":mark, "feedback":feedback }
        	else:
        		self.Questions[question_number] =  {"q" : str(question), "correctA":[correct, letter],"wrongAs": wrong_letters,"mark":mark, "feedback":feedback}
    

        elif len(self.Questions) > 0:
            i = len(self.Questions)
            if is_save:
            	print(is_save, question_number, '=========')
            	self.Questions[i+1] = {"q" : str(question), "correctA": [correct, letter],
                                       "wrongAs": wrong_letters, "mark":mark, "feedback":feedback}
            else:
            	print(is_save, question_number, '>>>..>>..>>')
            	self.Questions[question_number] = {"q" : str(question), "correctA": [correct, letter],
                                       "wrongAs": wrong_letters, "mark":mark, "feedback":feedback}          	

    def test_wrapper(self):
        """Main wrapper functions.  Converts the class into a dictionary
        :return wrapper: Dict of class Test instance"""
        wrapper =                 {"name" : self.name,
                                   "testID": self.testID,
                                   "module": self.module,
                                   "QnA" : self.Questions,
                                   "Start date": self.startdate,
                                   "End date": self.enddate}
        return wrapper
    
    def getMark(self,QuestionNo):
        #Newly added.
        return self.Questions[QuestionNo][1]['mark']
          
    def getFeedback(self,QuestionNo):
        #Newly added.
        return self.Questions[QuestionNo][1]['feedback']

    def calculateMark(self, correctList, answeredList):
        """Compares a list of correct answers with the list of answered submited
        :params correctList: List of characters.
        :params answeredList: List of characters.
        :return mark: int.
        """
        mark = 0
        wrong = 0

        if len(correctList) != len(answeredList):
            raise Exception("Incorrect list size")
        else:
            for i in range(len(correctList)):
                if correctList[i] == answeredList[i]:
                        mark += 1
                else:
                        wrong += 1
        return mark, wrong

    def save_json(self,path=""):
        #Modified to link to my GUI.
        saveTest = self.test_wrapper()
        filename = "%s/%s %s.json" % (path, self.module,self.name)

        with open(filename, "w") as outfile:
            json.dump(saveTest, outfile, indent=4)
        return

    def save(self,filename,path):
        self.save_json(path=path)
        return

    def testNameGenerator(self):
        """Generates an id for the tests
        :return testName: TestID"""
        testName = str(self.module) + " " + str(self.testID)
        return testName