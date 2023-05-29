# a = 1 
# b = True

#while True:
# if a == 2:
#     print ("Boo \nGotya" *4)
# else:
#     print("no " + str(a))
#     a = a + 1

    ## do "sample" into [sa] , [mp] , [le]
# i = 0
# s = 'sample'
# print(s)
# array = []

# while i < len(s):
#     temp = s[i] + s[i+1]
#     array.append(temp)
#     print (array)
#     i = i + 2


    ## do "samples" into [sa] , [mp] , [le] , [s_]
# i = 0
# s = 'samples'
# print(s)
# array = []

# if len(s)%2==1:
#     s = s + '_'

# while i < len(s):
#     temp = s[i] + s[i+1]
#     array.append(temp)
#     print (array)
#     i = i + 2


    ## convert text to its place in the alphabet. "aBcz" into "1 2 3 26"

# s = 'aBcz abc'
# a = ""

# for i in range(0,len(s)):
#     if s[i].isalpha():
#         a = a + str((ord((s[i]).lower()) - 96)) + " "
#     print(a)

    ## Write a function, persistence, that takes in a positive parameter 
    # num and returns its multiplicative persistence, which is the number 
    # of times you must multiply the digits in num until you reach a single 
    # digit. 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
    #999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
    #4 --> 0 (because 4 is already a one-digit number)

# n = 999
# c = 0

# while len(str(n)) > 1:
#     s = 1
#     for i in range(0, len(str(n))):
#         s = s * int(str(n)[i])    
#     n = s
#     c += 1
#     print(n)
# print(c)

    ##Write a function that takes an integer as input, and returns the number of bits 
    # that are equal to one in the binary representation of that number. You can guarantee 
    # that input is non-negative. # Example: The binary representation of 1234 is 10011010010, 
    # so the function should return 5 in this case

# a = bin(1234)
# a = a[2:]
# count = 0
# print(a)
# for c in range(0, len(a)):
#     if int(a[c]) == 1:
#         count +=1


    ##Build a pyramid-shaped tower, as an array/list of strings, given a positive 
    # integer number of floors. A tower block is represented with "*" character. 
    # For example, a tower with 3 floors looks like this:
    # [
    #   "  *  ",
    #   " *** ", 
    #   "*****"
    # ]

# n_floors = 3
# count = 0
# star = 1
# tree = []
# while count < n_floors:
#     tree.append(' '*(n_floors - count - 1) + "*"*(star) + ' '*(n_floors - count -1))
#     count +=1
#     star +=2
# print(tree)

    # If we list all the natural numbers below 10 that are multiples of 3 or 5, 
    # we get 3, 5, 6 and 9. The sum of these multiples is 23. Finish the 
    # solution so that it returns the sum of all the multiples of 3 or 5 below 
    # the number passed in. Additionally, if the number is negative, return 0 
    # (for languages that do have them).
    # Note: If the number is a multiple of both 3 and 5, only count it once.

# number = 10
# temp3 = 3
# temp5 = 5
# total = 0
# count3 = 1
# count5 = 1

# if number < 0:
#     pass #return 0
# else:
#     while temp3 < number:
#         total += temp3
#         count3 += 1
#         if temp3%5 == 0:
#             total -= temp3
#         temp3 = 3*count3
#         print("temp3 "+  str(temp3))
#         print("total " + str(total))
    
#     while temp5 < number:
#         total += temp5
#         count5 += 1
#         temp5 = 5*count5
#         print("temp5 "+  str(temp5))
#         print("total " + str(total))

    ## Complete the solution so that the function will 
    # break up camel casing, using a space between words.
    # "camelCasing"  =>  "camel Casing"
    # "identifier"   =>  "identifier"
    # ""             =>  ""

# s = "camelCasing"
# uncased = ""

# for i in range(0, len(s)):
#     if s[i].islower():
#         uncased += s[i]
#     elif s[i].isupper():
#         uncased += " " + s[i]
# print(uncased)








    








