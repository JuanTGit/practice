# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    l = 0
    r = 0
    s = list(text)
    while r < len(s):
        if s[r] == '!.%&?':
            r += 1
        if s[r] == s[-1]:
            s[l], s[r] = s[r], s[l] + 'ay'
        if s[r] == " ":
            s[l], s[r - 1] = s[r - 1], s[l] + 'ay'
            l = r + 1
            r = l + 1
        else:
            r += 1
    return ''.join(s)

print(pig_it('Pig latin is cool'))