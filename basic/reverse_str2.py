#Palindrome is a number which is the same when reversed
#This function takes in a parameter called "number"
def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        remainder = number % 10
        print
        reverse_num = (reverse_num * 10) + remainder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")
#invoke the functions 
palindrome(121)
palindrome(125)
