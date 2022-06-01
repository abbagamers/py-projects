AnswersRight = 0
print("Welcome to a test quiz!")
playing = input("Do you want to play? ")
print(playing)
if playing != "yes":
    quit()
print("Ok, lets go :)")
cpu = input("What does CPU stand for? \n 1) Chad Power Unit \n 2) Central Processing Unit \n 3) Cold Process Uniform \n")
if cpu == "2":
    print("Correct!")
    AnswersRight = AnswersRight+1
else:
    print("Incorrect answer!")

ram = input("What does RAM stand for?  \n 1) Random Ass Man \n 2) Right All Memory \n 3) Random Access Memory \n")
if ram == "3":
    print("Correct!")
    AnswersRight = AnswersRight+1
else:
    print("Incorrect. Better Luck!")
#for the quiz, the blank code is:
#print("Ok, lets go :)")
#QuestionName= input("What does ____ stand for? \n 1) ____ \n 2) ____ \n 3) ____ \n")
#if QuestionName == "2":
#  print("Correct!")
#    AnswersRight = AnswersRight+1
#else:
#    print("Incorrect answer!")
print(f"You got  {AnswersRight}, answers right!")
quit()

