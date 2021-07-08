'''
Given two strings s1 and s2. The task is to check if s2 is a rotated version
of the string s1. The characters in the strings are in lowercase.


Example 1:

Input:
geeksforgeeks
forgeeksgeeks
Output:
1
Explanation: s1 is geeksforgeeks, s2 is
forgeeksgeeks. Clearly, s2 is a rotated
version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.


Example 2:

Input:
mightandmagic
andmagicmigth
Output:
0
Explanation: Here with any amount of
rotation s2 can't be obtained by s1.


Your Task:
The task is to complete the function areRotations() which checks if the two
strings are rotations of each other. The function returns true if string 1 can
be obtained by rotating string 2, else it returns false.



Expected Time Complexity: O(N).
Expected Space Complexity: O(N).
Note: N = |s1|.



Constraints:
1 <= |s1|, |s2| <= 107
'''


def areRotations(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len != s2_len:
        return False

    s1 += s1
    cnt = 0
    for i in range(len(s1)):
        if s2[cnt] == s1[i]:
            cnt += 1
            if cnt == s2_len-1:
                return 1
        else:
            cnt = 0
    return 0


# geeksforgeeksgeeksforgeeks
if __name__ == '__main__':
    print(areRotations("geeksforgeeks", "forgeeksgeeks"))
    print(areRotations("mightandmagic", "andmagicmigth"))
    print(areRotations("gfeksforgeeks", "forgeeksgfeks"))
