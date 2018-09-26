#!/bin/python3
#https://www.hackerrank.com/challenges/mini-max-sum/problem
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sm = sum(arr,0)
    mn = sm
    mx = 0
    for i in arr:
        if((sm-i) <mn):
            mn = sm -i 
        if ((sm-i)>mx):
            mx = sm -i
    print (mn, mx)
        


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)