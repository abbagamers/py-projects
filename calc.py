loop = True
while loop:
    in1 = str(input("What is your operator: "))
    in2 = int(input("What is your first number: "))
    in3 = int(input("What is your second number: "))
    if in1 in ['/', '*', '+', '-']:
        print(f"{in2} {in1} {in3} = {eval(f'{in2}{in1}{in3}')}")
    else:
        print("Invalid")
    in4 = input("Would you like to continue? (y/n) ")
    if in4.lower() == 'n':
        loop = False

