scores = input("Enter scores : ")
scoresList = scores.split(" ")
scoresList2 = list()
studentGrades = list()
for score in scoresList:
    scoresList2.append(int(score))
bestGrade = max(scoresList2)


# print(bestGrade)
def calculateGrade(stgrade):
    a = bestGrade - 10
    b = bestGrade - 20
    c = bestGrade - 30
    d = bestGrade - 40
    if stgrade >= a:
        return "A"
    elif stgrade >= b:
        return "B"
    elif stgrade >= c:
        return "C"
    elif stgrade >= d:
        return "D"
    else:
        return "F"


for i in range(0, len(scoresList2)):
    stgradex = int(scoresList2[i])
    grade = calculateGrade(stgradex)
    studentGrades.append(grade)

for i in range(0, len(scoresList2)):
    print("Student ", i, " score is ", scoresList2[i], " and grade is ", studentGrades[i])
