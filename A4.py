#Line 2 is to get an input
w = int(input())

#and w > 3 is added because the result of diving w has to be an even number but if w = 2, 2 / 2 = 1 so its uneven and it fails
if w % 2 == 0 and w > 3:
    print('YES')
else:
    print('NO')