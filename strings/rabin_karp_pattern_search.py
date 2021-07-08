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

Like the Naive Algorithm, Rabin-Karp algorithm also slides the pattern one by
one. But unlike the Naive algorithm, Rabin Karp algorithm matches the hash
value of the pattern with the hash value of current substring of text, and
if the hash values match then only it starts matching individual characters.
So Rabin Karp algorithm needs to calculate hash values for following strings.
Pattern itself.

All the substrings of the text of length m, that is of the length of
pattern string.

Since we need to efficiently calculate hash values for all the substrings of
size m of text, we must have a hash function which has the following property.

Hash at the next shift must be efficiently computable from the current hash
value and next character in text or we can say hash(txt[s+1 .. s+m])
must be efficiently computable from hash(txt[s .. s+m-1]) and txt[s+m] i.e.,
hash(txt[s+1 .. s+m])= rehash(txt[s+m], hash(txt[s .. s+m-1])
and rehash must be O(1) operation.

The hash function suggested by Rabin and Karp calculates an integer value.
The integer value for a string is numeric value of a string.
For example, if all possible characters are from 1 to 10,
the numeric value of "122" will be 122. The number of possible characters is
higher than 10 (256 in general) and pattern length can be large.
So the numeric values cannot be practically stored as an integer.
Therefore, the numeric value is calculated using modular arithmetic to make
sure that the hash values can be stored in an integer variable
(can fit in memory words). To do rehashing, we need to take off the most
significant digit and add the new least significant digit for in hash value


Rehashing is done using the following formula.
hash( txt[s+1 .. s+m] ) = ( d ( hash( txt[s .. s+m-1]) - txt[s]*h )
                            + txt[s + m] ) mod q

Where,
hash( txt[s .. s+m-1] ) : Hash value at shift s.
hash( txt[s+1 .. s+m] ) : Hash value at next shift (or shift s+1)
d: Number of characters in the alphabet
q: A prime number
h: d^(m-1)


Pseudo Code:
RABIN -KARP -MATCHER (T, P, d, q)
    1 n = T.length
    2 m = P.length
    # Important Step 1
    3 h = d^(m-1) mod q
    4 p = 0
    5 t = 0

    # Important Step 2
    # preprocessing
    6 for i = 1 to m
    7 p = (d * p + P [i]) mod q
    8 t = (d * t + T [i]) mod q

    # matching
    9 for s = 0 to n-m
    10     if p == t
    11         if P [1... m] == T [s + 1...s + m]
    12             print “Pattern occurs with shift” s
    13     if s < n-m

    # Important Step 3
    14         t  = (d * (t - T[s + 1] * h) + T[s + m + 1]) mod q

Summary : Remember the hash functions
    d = 256 ; q = prime_no; m = len(Pattern); n = len(Text)
    p = hash_pattern; t = hash_text; s = index
    1. h = d^(m-1) mod q
    2. p = (d * p + P [i]) mod q
    3. t = (d * t + T [i]) mod q
    4. t = (d * (t - T[s + 1] * h) + T[s + m + 1]) mod q


Limitations of Rabin-Karp Algorithm
Spurious Hit: When the hash value of the pattern matches with the hash value
of a window of the text but the window is not the actual pattern.
Example:
            Hash_Pattern = Hash_Text_slidingWindow
            where pattern = 'abc', Text_slidingWindow = 'xyz'

Spurious hit increases the time complexity of the algorithm.
To minimize spurious hit, modulus is used.

In short, Hash Collision concepts

Time Complexity:
    Average/Best Case = O(n+m)
    Worst-case        = O(n*m)   e.g.> pat[] = "AAA" and txt[] = "AAAAAAA"

Programiz
https://www.programiz.com/dsa/rabin-karp-algorithm
GFG
https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

'''


# Programiz
def search(pattern, text, q):
    d = 10
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                print("Pattern is found at position: " + str(i+1))

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q


# GFG + Programiz
def rabin_karp_pattern_search(pattern, text, prime_no):
    m = len(pattern)
    n = len(text)
    hash_pat = 0
    hash_txt = 0
    hash = 1

    # hash = pow(256, m-1)%q
    hash = (256 ** (m - 1)) % prime_no

    # Hash Function to find Hash Value for both Pattern and Text.
    for i in range(m):
        # Number of ASCII characters: 256
        hash_pat = (256 * hash_pat + ord(pattern[i])) % prime_no
        hash_txt = (256 * hash_txt + ord(text[i])) % prime_no

    # Find the match by sliding the Pattern over Text one by one.
    for i in range(n-m+1):
        '''
        Check the hash values of current window of text and pattern.
        If the hash values match then only check for characters on by one.
        '''
        if hash_pat == hash_txt:
            # Check for characters one by one
            for j in range(m):
                if (text[i+j] != pattern[j]):
                    break
            j += 1
            if (j == m):
                print("Pattern found at index: ", i)

        if i < n-m:
            '''
            Remove leading digit's hash value & Add trailing digit's hash value
            hash_txt =
            (256 * (hash_txt - ord(text[character to be removed]) * hash)
            + ord(text[character to be added])) % prime_no

            # Add an element to hash
            t = (d * t + T [i]) mod q

            # Sliding Window hash
            t  = ( d * (t - T[s + 1] * h) + T [s + m + 1] ) mod q
            '''

            hash_txt = (256 * (hash_txt - ord(text[i]) * hash) + ord(text[i+m])) % prime_no

            # We might get -ive value of hash_txt, converting it to +ive
            if (hash_txt < 0):
                hash_txt = (hash_txt + prime_no)



if __name__ == '__main__':
    pattern = '4567'
    text = '12345678904567'
    prime_no = 101
    print(pattern, text)
    rabin_karp_pattern_search(pattern, text, prime_no)
    #search(pattern, text, prime_no)

    pattern = "CDD"
    text = "ABCCDDAEFG"
    print(pattern, text)
    rabin_karp_pattern_search(pattern, text, prime_no)
    #search(pattern, text, prime_no)
