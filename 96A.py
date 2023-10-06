#define a function because i need the return statements to stop the excecution of the code incase i reach a YES case
def checkSit():

    #Get input from user, initialize the consecutive char counter to 0, and initialize a variable to keep track of the last char
    situation = input()
    count = 0
    last = situation[0]
    
    #loop through the input string
    for i in range(len(situation)):

        #if the current char is the same as the last, add 1 to the concurrent char count
        if situation[i] == last:
            count = count + 1
        
        #if the current char is not the same, assign the current char to last so that we look for consecutives of this char, and reset the counter to 1 because the streak was broken
        else:
            last = situation[i]
            count = 1
        
        #if we happen to hit 7 or more consecutive chars we exit out of the function and print YES
        if count >= 7:
            return print("YES")
    
    #if we never hit 7 or more consecutive chars during the loop, we print NO
    return print("NO")

#call the function
checkSit()



