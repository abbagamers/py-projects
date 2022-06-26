
import time
q = "What type of conversion would you like to make? \n1)cm-in \n2)in-cm \n3)oz-ml \n4)ml-oz \n"
inp = str(input(q))
if inp == "1":
    cm = int(input("How many cm would you like to convert to inches?"))
    print(cm/2.54)
    time.sleep(0.5)
    quit()
elif inp == "2":
    inch = int(input("How many inches would you like to convert to cm?"))
    print(inch*2.54)
    time.sleep(0.5)
    quit()
elif inp == "3":
    oz = int(input("How many ounces would you like to convert to ml?"))
    print(oz*29.574)
    time.sleep(0.5)
    quit()
elif inp == "4":
    ml = int(input("How many ml would you like to convert to ml?"))
    print(ml/29.574)
    time.sleep(0.5)
    quit()
