import random
q = input("Would you like to flip a coin? ")
if q == "yes":
    randint = random.randint(1, 2)
else:
    quit()
if randint == 1:
    print("You got heads!")
else:
    print("You got tails!")
rptq = str(input("Would you like to try again?"))
if rptq != "yes":
    quit()
else:
    randint = random.randint(1, 2)
    if randint == 1:
        print("You got heads!")
    else:
        print("You got tails! ")