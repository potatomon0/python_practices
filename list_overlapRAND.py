import list_overlap2 as l2
listA=[]
listB=[]
l2.randomNum.rlistA(listA)
l2.randomNum.rlistB(listB)

#print(listA)
#print(listB)
print(list(i for i in listA if i in listB))
