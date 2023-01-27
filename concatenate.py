nums = [1, 2, 1]

def concatenate(n):
    ans = [i for i in n]
    for i in n:
        ans.append(i)
    return ans

print(concatenate(nums))

def concatenate2(n):
    return n*2


print(concatenate2(nums))