#https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043adc7
import sys
import math
from sys import stdin,stdout
from math import gcd,floor,sqrt,log

inp    =lambda: int(input())
strng  =lambda: input().strip()
seq    =lambda: list(map(int,input().strip().split()))

T = inp()
for x in range(T):
    N,K,S = seq()
    # print(N,K,S)
    y = (K - 1)  + N + 1  #restart case
    fr =  (K-1) + (K-S) + (N - S + 1)
    if fr < y:
        y = fr
    print("Case #{}: {}".format(x+1,y))