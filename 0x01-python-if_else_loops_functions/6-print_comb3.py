#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if i == 8 and j == 9:
            print('{}{}'.format(i, j))
        else:
            if i != j:
                print('{}{}'.format(i, j), end=', ')
