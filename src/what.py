import json

userID = '102'

with open ('studentAnswers.json', 'r') as f:
    data = json.load(f)

# print a list of all student IDs
print([item['studentID'] for item in data['testID'] if item['studentID'] == userID])

# # access the data for the specified student ID
# for i in data['testID']:
# 	if i['studentID'] == userID:
# 		answers = i['Test']['answers']
# 		print(answers)
# 		break
# 	else:
# 		print('Not found')

# if userID in data['testID']['studentID']:
# 	print('Yes')
# else:
# 	print('No')


# print('102' in data['studentID'])


# print out ALL lists of student answers
for i in data['testID']:
	answers2 = i['Test']['answers']
	print(answers2)




correct = ["a", "b", "a", "a", "d", "a", "c", "d", "a", "b"]

# print(alist)
# print(correct)

mark = 0
wrong = 0
total = 0

individualMark = 0



## ALL STUDENT MARKS

# for i in data['testID']:
# 	toMark = i['Test']['answers']
# 	print("Student Answers ({}): {} ".format(i['studentID'], toMark))

# 	for x in toMark:
# 		if correct[i] == x:
# 			mark += 1
# 			print("Question",x+1)
# 			print(x + "\t\tCorrect\n")
# 		else:
# 			wrong += 1
# 			print("Question",x+1)
# 			print(x + "\t\tIncorrect")
# 			print("Correct answer was: " + correct[x] + "\n") 


# 	print("\tTEST RESULTS\n-----------------------------\n\n")

# 	for x in range(10):
# 		if correct[x] == answers2[x]:
# 			mark += 1
# 			print("Question",x+1)
# 			print(answers2[x] + "\t\tCorrect\n")
# 		else:
# 			wrong += 1
# 			print("Question",x+1)
# 			print(answers2[x] + "\t\tIncorrect")
# 			print("Correct answer was: " + correct[x] + "\n") 

			

# 	print("Total Mark: " , mark,"/10\n\n")

# 	total += mark

# print(mark)
# print(len(i))
# print(total)
# average = total / (len(i)+1)
# print(average)


## STUDENT MARKS FOR SPECIFIED STUDENT

	
# print("\tTEST RESULTS\n-----------------------------\n\n")

# for s in range(10):
# 	if correct[s] == answers[s]:
# 		individualMark += 1
# 		print("Question",s+1)
# 		print(answers[s] + "\t\tCorrect\n")
# 	else:
# 		wrong += 1
# 		print("Question",s+1)
# 		print(answers[s] + "\t\tIncorrect")
# 		print("Correct answer was: " + correct[s] + "\n") 

			

# print("Total Mark: " , individualMark,"/10\n\n")
