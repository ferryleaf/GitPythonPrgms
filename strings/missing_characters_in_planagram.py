'''
You are given a string s. You need to find the missing characters in the
string to make a panagram.
Note: The output characters will be lowercase and lexicographically sorted.

What is Planagram?
A pangram or holoalphabetic sentence is a sentence using every letter of a
given alphabet at least once. Pangrams have been used to display typefaces,
test equipment, and develop skills in handwriting, calligraphy, & keyboarding.
The best-known English pangram is "The quick brown fox jumps over the lazy dog"

Example 1:

Input:
s = Abcdefghijklmnopqrstuvwxy
Output: z


Example 2:

Input:
s = Abc
Output: defghijklmnopqrstuvwxyz

Your Task:

You only need to complete the function misssingPanagram()
that takes s as parameter and returns -1 if the string is a panagram,
else it returns a string that consists missing characters.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000

input - @s = given string

output - return -1 or required ans
'''


def missingPanagram(s):
    uniq = ''
    for i in range(97, 123, 1):
        if chr(i) not in s.lower():
            uniq = uniq + chr(i)

    if uniq is None:
        return -1
    else:
        return uniq


# Better Solution
def isPlanagram(a):
    arr = [0 for i in range(26)]
    flag = 0
    for ch in a:
        if ord(ch) >= 65 and ord(ch) <= 90:
            idx = ord(ch) - 65
        elif ord(ch) >= 97 and ord(ch) <= 122:
            idx = ord(ch) - 97
        arr[idx] = 1

    for i in range(len(arr)):
        if arr[i] == 0:
            print(chr(i + 97), end= ' ')
            flag = 1
    if flag == 0:
        print(-1)
    print()


if __name__ == '__main__':
    missingPanagram('Abc')      # defghijklmnopqrstuvwxyz
    missingPanagram('Abczvw')   # defghijklmnopqrstuxy
    missingPanagram('Abcdefghijklmnopqrstuvwxy')    # z

    isPlanagram("Abcdefghijklmnopqrstuvwxy")
    isPlanagram("defghijklmnopqrstuvwxyz")
    isPlanagram("The quick brown fox jumps over the lazy dog")
