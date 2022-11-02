try:
    num = input("Enter the number: ")
    num = int(num)
    x = range(1, num)
    list1 = []
    for i in x:
        if num%i ==0:
            list1.append(i)
    print(list1)
except ValueError:
    print("The value type is not supported.")