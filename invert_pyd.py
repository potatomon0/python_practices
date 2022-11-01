#my method:
sub = 5
for x in range(1,sub+1):
    for y in range(1,sub+1):  
        print(x, end = " ")
    sub -=1
    print("\t")

#web solution:
rows = 5
b = 0
for i in range(rows,0,-1):
    b+=1
    for j in range(1, i+1):
        print(b, end = " ")
    print("\r")

