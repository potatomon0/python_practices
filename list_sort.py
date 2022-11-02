
try:
    a=input("Enter the set of numbers separated by space: ")
    b=input("Enter the threshold number: ")
    b=int(b)
    listC=[]
    #listA = a.split(" ")
    listA = a.replace(" ","")
    #listA = list(listA)
    listB = [eval(i) for i in listA]
    for item in listB:
        if item < b:
            listC.append(item)
        else:
            continue
    print(listC)
except:
    print("The value entered is not supported")

