n = int(input("n = "))
list = [int(l) for l in input().split()]
tempList = []
for i in list:
    tempList.append(i)
    tempList.sort(reverse=True)
    for j in tempList:
        if len(tempList) > 5:
            tempList.remove(j)
    print(tempList)