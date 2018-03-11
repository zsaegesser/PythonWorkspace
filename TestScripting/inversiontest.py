from random import randint

def createList(size_list):
    lst = [None]*size_list
    for i in list(range(0,size_list)):
        lst[i] = randint(0,size_list*5)
    return lst

def checkInversions(lstt):
    count =0
    for i in list(range(0,len(lstt)-1)):
        for j in list(range(i+1,len(lstt))):
            if lstt[i] > lstt[j]:
                count +=1
    return count
test1 = createList(10)
for i in list(range(0,len(test1))):
    print test1[i],
print "\n"
print(checkInversions(test1))
print "\n"
print "\n"

test2 = createList(100)
for i in list(range(0,len(test2))):
    print test2[i],
print "\n"
print checkInversions(test2)
print "\n"
print "\n"


test4 = list(range(0,90001))
test4 = test4[::-1]
for i in list(range(0,len(test4))):
    print test4[i],
print "\n"
print(90000*(90000-1)/2)
