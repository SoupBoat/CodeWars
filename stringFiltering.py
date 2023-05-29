## filters out all the strings in the list

l = [1,2,'a',4, 'd', 3, 'g', 'f', 5, 'c']
a = []
for c in l:
    if type(c) == int:
        a.append(c)
l = a



