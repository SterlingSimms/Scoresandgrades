import random
def scoresGrades():
    for grade in range(10):
        grade = random.randint(0, 100)
        if grade in range(0, 60):
            letter = "F. You failed!"
        elif grade in range(60, 70):
            letter = "D"
        elif grade in range(70, 80):
            letter = "C"
        elif grade in range(80, 90):
            letter = "B"
        elif grade in range(90, 101):
            letter = "A!"
        print("Score: {}; Your grade is: {}".format(grade, letter))
scoresGrades()
