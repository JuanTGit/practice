# 605. Can Place Flowers
# Easy

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


def canPlaceFlowers(flowerbed, n):
    bigger_bed = [0] + flowerbed + [0]

    for flower in range(1, len(bigger_bed) - 1):
        if bigger_bed[flower] == 0 and bigger_bed[flower-1] == 0 and bigger_bed[flower+1] == 0 and n > 0:
            bigger_bed[flower] = 1
            n -= 1
            if n == 0:
                return True
        
    return False

# print(canPlaceFlowers([1, 0, 0, 0, 1], n=2))

def canPlaceFlower(flowerbed, n):

    for i in range(len(flowerbed)):
        if ((i == 0 or flowerbed[i - 1] == 0)
            and (flowerbed[i] == 0)
            and (i == len(flowerbed) or flowerbed[i + 1] == 0)):
            flowerbed[i] == 1
            n -= 1
    return n == 0

print(canPlaceFlower([1, 0, 0, 0, 1], n=1))