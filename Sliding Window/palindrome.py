def isPal(word):
    if word == word[::-1]:
        return True
    return False

def pointerPal(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l].isalnum() and s[r].isalnum():
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        elif s[l].isalnum():
            r -= 1
        elif s[r].isalnum():
            l += 1
        else:
            l += 1
            r -= 1
    return True


pal = 'Hannah'
palfalse = 'coding'
palindrome = 'racecar'
s = 'race a car'

print(pointerPal(pal))
print(pointerPal(palfalse))
print(pointerPal(palindrome))
print(pointerPal(s))