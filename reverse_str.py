# txt = "Hello World"[::-1]
# print(txt)
num = input("enter number: ")
def palindrome(num):
    revNum = num[::-1]
    if num == revNum:
        print("The number is a palindrome number")
    else:
        print("The number is not a palindrome number")
    print(revNum)
palindrome(num)
