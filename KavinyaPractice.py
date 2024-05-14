
# this is a list of names. a list is a type of array. 
# The names are strings which mean theyve got "" or '' around them. As long as its consistent per string theres no issue
names = ["Dan", "Kavinya", "Deniz"]

# this is a list of numbers. integers are green
numbers = [3, 2, 1]

# when your creating variables you don't need to declare their type (string, integer, float, boolean)
welcomeMessage = "hello"
number = 3
decimals = 0.005
yesOrNo = True      #booleans are dark blue. if the True or false doesnt turn blue then its reading it as a variabled called true and not a boolean

# if you want to mark a variable as a constant, make the variable name something in all caps.
# the reason you do this is to signal to other coders that it shouldnt be changed and overriding it is bad practice
# this will make it turn blue but it doesnt mean it cant be overwritten like in Java. 
# ie. if you choose to you can change what the constant is later (eg below) 
TWO = 2
TWO = 4     #this code will run and TWO will be overwritten. 

# print this
print(number)

if number in numbers:
    print("yes")
elif number == 3:   # == does a boolean check
    print("it is 3")
else:
    print("no")
    
# ## use control + slash to turn the below into not code and back
# helololo
# ur moma gay
# hahaha

# to move indents around use ctrl + close bracket or open bracket.
# it just lets you move multiple lines at the same time

# copy here for ease
names = ["Dan", "Kavinya", "Deniz"]

# example of for loop
for name in names:
    # two ways of doing the same print statement. second is short hand. same thing
    print(welcomeMessage + " to " + name)
    print(f"{welcomeMessage} to {name}")

# while loop
counter = 0
yesOrNo = True

while yesOrNo:
    counter = counter + 1
    if counter == 5:
        yesOrNo = False
    print(counter)

print("were freee~!")

