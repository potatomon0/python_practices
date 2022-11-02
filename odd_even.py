
try:
    number = int(input("Enter the number "))
    if number%4 == 0:
        print(f"{number} is divisible by 4")
    elif number%2 == 0:
        print(f"{number} is a even number ")
    elif number%4 != 0:
        print(f"{number} is an odd number")
except ValueError:
    print("The value is not valid")
