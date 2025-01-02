import os

print("""You will be given a set of Questions. Please Answer these as honeslty as possible. 
Rate each question with:
0 = Not at all
1 = Several days
2 = More than half the days
3 = Nearly every day""", end="\n\n")
questions = []

with open(r"C:\Users\sowme\StudioProjects\TDL_Project_new\ph9.txt", "r") as f:
    for ques in f:
        questions.append(ques)

depression_score = 0
for question in questions:
    print("\n" + question)
    answer = input("Rate the question: ")
    depression_score += int(answer)

print("""You will be given another set of Questions. Please Answer these as well as, as honeslty as possible. 
Rate each question with:
0 = Not at all
1 = Several days
2 = More than half the days
3 = Nearly every day""", end="\n\n")
questions = []

with open(r"C:\Users\sowme\StudioProjects\TDL_Project_new\gad7.txt", "r") as f:
    for ques in f:
        questions.append(ques)

anxiety_score = 0
for question in questions:
    print("\n" + question)
    answer = input("Rate the question: ")
    anxiety_score += int(answer)

print("\n\n")
print("Depression Score: " + str(depression_score))
print("Anxiety Score: " + str(anxiety_score))

"""For PHQ-9:

Sum all 9 scores (0-3 each)
Total range: 0-27
Severity levels:

0-4: Minimal
5-9: Mild
10-14: Moderate
15-19: Moderately severe
20-27: Severe



For GAD-7:

Sum all 7 scores (0-3 each)
Total range: 0-21
Severity levels:

0-4: Minimal
5-9: Mild
10-14: Moderate
15-21: Severe"""