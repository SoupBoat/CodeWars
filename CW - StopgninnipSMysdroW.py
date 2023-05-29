##  Stop gninnipS My sdroW!

# Write a function that takes in a string 
# of one or more words, and returns the same 
# string, but with all five or more letter words 
# reversed (Just like the name of this Kata). 
# Strings passed in will consist of only letters 
# and spaces. Spaces will be included only when 
# more than one word is present.

def spin_words(sentence):
    sentence += ' '
    word = ''
    IAmInSpin = ''
    counter = 0
    for i in range(0, len(sentence)):
        if sentence[i] != ' ':
            counter +=1 
            word += sentence[i]
        else:
            if counter >= 5:
                drow = ''
                for i in range(0, len(word)):
                    drow = word[i] + drow 
                word = drow
            IAmInSpin =  IAmInSpin + word + ' '
            word = ''
            counter = 0
    IAmInSpin = IAmInSpin[:-1]
    return IAmInSpin


## Answer I like

def spin_words(sentence):
    L = sentence.split()    #splits the sentence by the spaces and removes the space
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])      #equiv of appendleft
        else:
            new.append(word)
    string = " ".join(new)      #this will join the array with spaces in between
    return string


## Test Cases

print(spin_words('Welcome'))   #should output 'emocleW'

print(spin_words('Hey fellow warriors'))   #Hey wollef sroirraw
