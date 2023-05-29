lst = [1,0,1,2,0,1,3]
n = 0

while 0 in lst:     #while there are 0s in the list
    lst.remove(0)       #remove the value 0 from list
    n += 1
for i in range(n):      #for the number of times a 0 was removed
    lst.append(0)