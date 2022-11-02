usrStr = input("Original String is: ")
length = len(usrStr)
print(usrStr)
for i in range(length):
    if i%2 == 0:
        print(usrStr[i])
    else:
        continue