#This code wont pass the test in codeforces but it passes them in my machine

first_line = input()
second_line = input()

def find_gap():
    inputs = list([int(y) for y in first_line.split(" ")])
    n = inputs[0]
    store_puzzles = list([int(x) for x in second_line.split(" ")])
    store_puzzles.sort()
    smallest = store_puzzles[0]
    biggest = store_puzzles[n - 1]

    return biggest - smallest

print(find_gap())