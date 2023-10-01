#Get input string
string = str(input())

#Separate the numerical characters from the +
string_list = string.split('+')

#Loop through the array and convert the numerical characters to integers
for i in range(len(string_list)):
    string_list[i] = int(string_list[i])

#Sort the numbers
string_list.sort()

#Convert the array of sorted number to a string, add the +, remove the [ ] and print
print(str(string_list).replace(', ', '+').replace('[','').replace(']',''))