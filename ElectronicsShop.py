#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    spent = -1
    
    for i in keyboards:
        for j in drives:
            if(i + j <= s):
                spent = max(spent, i + j)

    return spent
    
    #single-line implementation:
   # return max([sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]+[-1])
            

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
