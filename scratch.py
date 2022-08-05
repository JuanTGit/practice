list_1 = [2, 4, 8]
list_2 = [1, 3, 2]

def combine(l1, l2):
    new_list = []
    for i in range(len(l1)):
        new_list.append(l1[i]+l2[i])
    return new_list

print(combine(list_1, list_2))