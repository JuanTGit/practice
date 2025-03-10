# def solution(number):
#     total = []
#     if number % 3 == 0 or number % 5 == 0:
#             total.append(number)
#     return sum(total)

def solution(number):
    total = 0
    for num in range(0, number):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

print(solution(10))