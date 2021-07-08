'''
Given a text txt[0..n-1] and a pattern pat[0..m-1],
write a function search(char pat[], char txt[]) that prints all occurrences of
pat[] in txt[]. You may assume that n > m.

Examples:
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

Time Complexity: O(m*n) worst case
'''


def naive_pattern_search(pat, txt):
    m = len(pat)
    n = len(txt)
    idx = []
    for i in range(n - m + 1):
        if txt[i:i+m] == pat:
            idx.append(i+1)
    return idx


def display(pattern, text):
    print("Pattern:", pattern, " in given Text:", text,
    ", Found at Index:", naive_pattern_search(pattern, text))


if __name__ == '__main__':
    pattern = '4567'
    text = '12345678904567'
    display(pattern, text)

    text = 'AABAACAADAABAABA'
    pattern = 'AABA'
    display(pattern, text)
