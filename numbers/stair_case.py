#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k=n
    cnt=1
    while(k!=0):
        print(" "*(k-1) + "#"*cnt)
        k=k-1
        cnt=cnt+1



if __name__ == '__main__':
    n = int(input())

    if(n>0 and n<=100):
        staircase(int(n))
