#!/bin/python3
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    mx = -1
    cnt = 0
    for i in ar:
        if(i>mx):
            mx = i
            cnt = 0
        if(mx==i):
            cnt+=1
    return cnt

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
