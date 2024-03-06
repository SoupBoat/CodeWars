### Background
# Pat Programmer is worried about the future of jobs in programming because of the advance of AI tools like ChatGPT, and he decides to become a chef instead! So he wants to be an expert at flipping pancakes.

# A pancake is characterized by its diameter, a positive integer. Given a stack of pancakes, how can they be arranged in order by diameter, with the largest pancake at the bottom and the smallest at the top? You can insert a spatula under any pancake and then flip, which reverses the order of all the pancakes on top of the spatula.

### Task
# Write a function that takes a stack of pancakes and returns a sequence of flips that arranges them in order by diameter, with the largest pancake at the bottom and the smallest at the top. The pancakes are given as a list of positive integers, with the left end of the list being the top of the stack.

# Based on Problem 4.6.2 in Skiena & Revilla, "Programming Challenges".

### Example
# Consider the stack [1,5,8,3]. One way of achieving the desired order is as follows:

# The 8 is the biggest, so it should be at the bottom. Put the spatula under it (position 2 in the list) and flip.

# This transforms the stack into [8,5,1,3], with the 8 at the top. Then flip the entire stack (spatula position 3).

# This transforms the stack into [3,1,5,8], which has the 8 at the bottom. And since the 5 is in the correct position as well, now flip the 1 and 3 (spatula position 1).

# The stack is now [1,3,5,8], as desired. The function should return [2,3,1].

### Note
# You don't have to find the shortest sequence of flips. That is a hard problem - see https://en.wikipedia.org/wiki/Pancake_sorting. However, don't include unnecessary flips, in the following sense:

# (1) If 2 consecutive flips leave the stack in the same state, they should be omitted. For example, [2,3,2,2,1] also arranges [1,5,8,3] correctly, but 2,2 is unnecessary.

# (2) Flipping only the top pancake doesn't achieve anything.

def flip_pancakes(stack):
    flipOrder = []
    sortedStack = sorted(stack)
    print(stack)
    length = len(stack)
    print(length)
    # #I want to flip the array [2,1,3] into [3,1,2]
    flippedStack = stack[::-1]

    count =0
    print("################start#################")
    while stack != sortedStack:
        print(stack)
        
        for i in range(1, length+1):
            print("stack at len-" + str(i))
            print(stack[length-i])
            print("sortedStack at len-" + str(i))
            print(sortedStack[length-i])

            if stack[length-i] != sortedStack[length-i]:
                #find where sortedStack[len(sortedStack)-1] is in stack
                a = stack.index(sortedStack[length-i])
                b = sortedStack.index(stack[length-i])
                print(a)
                print(b)
                #flip stack from that point
                stack = stack[:a+1][::-1] + stack[a+1:]
                flipOrder.append(a)
                print(stack)
                print(flipOrder)
            
            if i == length:
                break
            print("done for loop " + str(i))
        count += 1
        # if count == 4:
        #     break


    return flipOrder


print(flip_pancakes([1,5,8,3]))



