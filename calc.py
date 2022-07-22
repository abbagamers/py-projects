loop = True
while loop:
    in1 = str(input("What is your operator: "))
    in2 = int(input("What is your first number: "))
    in3 = int(input("What is your second number: "))
    if in1 == "/":
        print(str(in2) + " / " + str(in3) + " = " + str(in2 / in3))
    elif in1 == "+":
        print(str(in2) + " + " + str(in3) + " = " + str(in2 + in3))
    elif in1 == "*" or "x":
        print(str(in2) + " x " + str(in3) + " = " + str(in2 * in3))
    elif in1 == "-":
        print(str(in2) + " - " + str(in3) + " = " + str(in2 - in3))
    else:
        print("Invalid")
    in4 = input("Would you like to continue? (y/n) ")
    if in4.lower() == 'n':
        loop = False

