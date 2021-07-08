'''
Given two strings 'str1' and 'str2', check if these two strings are
isomorphic to each other. Two strings str1 and str2 are called isomorphic if
there is a one to one mapping possible for every character of str1 to every
character of str2 while preserving the order.

Note: All occurrences of every character in ‘str1’ should map to the same
character in ‘str2’

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 1
Explanation: There are two different charactersin aab and xxy, i.e a and b
with frequency 2and 1 respectively.

Example 2:

Input:
str1 = aab
str2 = xyz
Output:
Explanation: There are two different charactersin aab but there are three
different charactersin xyz. So there won't be one to one mapping between
str1 and str2.

Your Task:
You don't need to read input or print anything.Your task is to complete the
function areIsomorphic() which takes the string str1 and string str2 as input
parameter and check if two strings are isomorphic. The function returns true
if strings are isomorphic else it returns false.

Expected Time Complexity: O(|str1|+|str2|).
Expected Auxiliary Space: O(Number of different characters).
Note: |s| represents the length of string s.

Constraints:
1 <= |str1|, |str2| <= 103

'''


# 0.33 seconds
def areIsomorphic(str1, str2):
    a = len(str1)
    b = len(str2)
    if a != b:
        return False

    a_mp = dict()
    for ele in str1:
        if a_mp.get(ele):
            a_mp[ele] = a_mp.get(ele) + 1
        else:
            a_mp[ele] = 1

    b_mp = dict()
    for ele in str2:
        if b_mp.get(ele):
            b_mp[ele] = b_mp.get(ele) + 1
        else:
            b_mp[ele] = 1

    if len(a_mp) != len(b_mp):
        return False

    for i in range(a):
        if (a_mp.get(str1[i]) != b_mp.get(str2[i])):
            return False

    return True


# 0.39 seconds
def areIsomorphic2(str1, str2):
    a = len(str1)
    b = len(str2)
    if a != b:
        return False

    a_mp = dict()
    b_mp = dict()
    for i in range(a):
        ele = str1[i]
        if a_mp.get(ele):
            a_mp[ele] = a_mp.get(ele) + 1
        else:
            a_mp[ele] = 1

        ele = str2[i]
        if b_mp.get(ele):
            b_mp[ele] = b_mp.get(ele) + 1
        else:
            b_mp[ele] = 1

    if len(a_mp) != len(b_mp):
        return False

    for i in range(a):
        if (a_mp.get(str1[i]) != b_mp.get(str2[i])):
            return False

    return True


if __name__ == '__main__':
    '''
    print(areIsomorphic('toayaxz', 'fbjbkrx'))  # False
    print(areIsomorphic('aab', 'xxy'))          # True
    print(areIsomorphic('aab', 'xyy'))          # False
    print(areIsomorphic('xudzhi', 'ftakcz'))    # True
    '''

    print(areIsomorphic2('toayaxz', 'fbjbkrx'))  # False
    print(areIsomorphic2('aab', 'xxy'))          # True
    print(areIsomorphic2('aab', 'xyy'))          # False
    print(areIsomorphic2('xudzhi', 'ftakcz'))    # True
