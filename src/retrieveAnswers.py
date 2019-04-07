import json

userID = '102'

# Need to get the actual student answers
with open ('studentAnswers.json', 'r') as f:
    data = json.load(f)

# print a list of all student IDs
print([item['studentID'] for item in data['testID']])

# access the data for the specified student ID
for i in data['testID']:
	if i['studentID'] == userID:
		answers = i['Test']['answers']
		print("Student: " + userID + "\nAnswers: {}".format(answers))
		break


#### CORRECT FILE PATH NEEDS TO BE SET ###
with open('Python General Knowledge.json', 'r') as file:
	testData = json.load(file)

print(testData["name"])

# Create a list of correct answers from the json
correctList = []

answer1 = testData["QnA"]["1"]["correctA"]
answer2 = testData["QnA"]["2"]["correctA"]
answer3 = testData["QnA"]["3"]["correctA"]
answer4 = testData["QnA"]["4"]["correctA"]
answer5 = testData["QnA"]["5"]["correctA"]
answer6 = testData["QnA"]["6"]["correctA"]
answer7 = testData["QnA"]["7"]["correctA"]
answer8 = testData["QnA"]["8"]["correctA"]
answer9 = testData["QnA"]["9"]["correctA"]
answer10 = testData["QnA"]["10"]["correctA"]
correctList.append(answer1)
correctList.append(answer2)
correctList.append(answer3)
correctList.append(answer4)
correctList.append(answer5)
correctList.append(answer6)
correctList.append(answer7)
correctList.append(answer8)
correctList.append(answer9)
correctList.append(answer10)
print(correctList)

# # print out ALL lists of student answers
# for i in data['testID']:
# 	answers2 = i['Test']['answers']
# 	print(answers2)




correct = ["a", "b", "a", "a", "d", "a", "c", "d", "a", "b"]

# print(alist)
# print(correct)

mark = 0
wrong = 0
total = 0

individualMark = 0