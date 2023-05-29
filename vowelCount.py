## count the number of vowels. Also ill be using this to 
# practice using libraries even though the task isn't actually suited.

vowels  = {'a':1, 'e': 1, 'i':1, 'o':1, 'u':1}

string = "heeeello"
count = 0

for c in string:
    print(c)
    if c in vowels:
        print("its a vowel")
        print(vowels[c])
        count = count + vowels[c]

print(count)
