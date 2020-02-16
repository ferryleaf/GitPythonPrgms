#!/bin/python3
'''
Given an array of integers,
calculate the fractions of its elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places,
though answers with absolute error of up to  10^-4 are acceptable

For example,
given the array  there are  elements,
two positive, two negative and one zero.
Their ratios should be printed as

0.400000
0.400000
0.200000

Function Description
Complete the plusMinus function in the editor below.
It should print out the ratio of positive, negative and zero items in the array,
each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):
arr: an array of integers

Input Format
The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Constraints
0< n <=100
-100 <= arr[i] <=100


Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size

Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667

Explanation

There are 3 positive numbers, 2 negative numbers, and  zero in the array.

'''
import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    leng = len(arr)
    pos=0
    neg=0
    zero=0
    for ele in arr:
        if(int(ele)>= -100 and int(ele)<=100):
            if(int(ele)>0):
                pos=pos+1
            elif (int(ele)<0):
                neg=neg+1
            else:
                zero+=1
    print('%.6f'%(pos/leng))
    print('%.6f'%(neg/leng))
    print('%.6f'%(zero/leng))

if __name__ == '__main__':
    n = int(input())
    if (n>0 and n<=100):
        arr = list(map(int, input().rstrip().split()))
        plusMinus(arr)
