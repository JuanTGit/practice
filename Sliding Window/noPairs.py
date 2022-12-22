# No Pairs Allowed

"""
Example
words = ['add', 'boook', 'break']

1. 'add': Change one d (1 change)
2. 'boook': Change the middle o (1 change)
3. 'break': No changes are necessart (0 changes)

The return array is [1,1,0]
"""

def minimalOperations(w):
    counter = []
    for word in w:
        l = 0
        r = 1
        subs = 0
        current_letter_count = 0
        while r < len(word):
            if word[l] == word[r]:
                if r == len(word)-1:
                    current_letter_count = r - l + 1
                    subs += current_letter_count // 2
                else:
                    current_letter_count = r - l + 1
                r += 1
            elif word[l] != word[r]:
                subs += current_letter_count // 2
                l = r
                r += 1
        counter.append(subs)
    return counter

words = ['add', 'boook', 'break']

print(minimalOperations(words))