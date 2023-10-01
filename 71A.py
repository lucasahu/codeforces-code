#Get number of words that will be inputed
n = int(input())

#Store words in an empty array
words = []

#Get the input words and store them in the array
for i in range(n):
    string = str(input())
    words.append(string)

#Loop through the array and check each word for their length and apply the mutation if needed
for x in range(len(words)):
    current = words[x]
    if len(current) > 10:
        print(current[0] + str(len(current) - 2)+ current[len(current) - 1])
    else:
        print(current)