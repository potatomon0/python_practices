try:
    a=input("Enter first list separated by space: ")
    b=input("Enter second list separated by space: ")
    listA = a.split(" ")
    listB = b.replace(" ","")
    listA = [eval(x) for x in listA]
    listB = [eval(y) for y in listB]
    #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c=[]
    for i in listA:
        if i in listB:
            c.append(i)
    
        else:
            continue
    print(c)


except ValueError:
    print("uh oh")
    