# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.


def disemvowel(s):
    vowels = set('aeiouAEIOU')
    no_vowels = ''
    no_vowels_r = ''
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] not in vowels:
            no_vowels += s[l]
        l += 1
        if s[r] not in vowels:
            no_vowels_r += s[r]
        r -= 1
    return no_vowels + no_vowels_r[::-1]


sent = "This website is for losers LOL!"

print(disemvowel(sent))
