import random as ran
try:
    randNum = ran.randint(1,9)
    state = True
    count = 1
    while state:
        usrNum = input("Take a guess of the number: ")
        if usrNum.lower()=="exit":
            break
        usrNum = int(usrNum)
        if usrNum >= 1 and usrNum <= 9:
            if usrNum < randNum:
                print("Your guess is too low, try again")
            elif usrNum > randNum:
                print("Your guess is too high, try again")
            elif usrNum == randNum:
                print(f"You got it! The secret number is {randNum}")
                print(f"It took you {count} tries!")
                state = False    
        else:
            print("Enter a number within the range")
        count+=1
except ValueError:
    print("Value type is not supported")