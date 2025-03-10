def solution(S):
    R = [0] * len(S)
    L = [0] * len(S)
    r_cars = 0
    l_cars = 0
    total = 0

    for i in range(len(S)):
        if S[i] == '.':
            R[i] = r_cars
        elif S[i] == '>':
            r_cars += 1

    for i in range(len(S) - 1, -1, -1):
        if S[i] == '.':
            L[i] = l_cars
        elif S[i] == '<':
            l_cars += 1

    for i in range(0, len(S)):
        total = total + L[i] + R[i]
    return total