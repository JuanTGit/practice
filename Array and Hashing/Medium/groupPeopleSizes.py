
def groupThePeople(groupSizes):
    groups = {}
    res = []

    for i, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = []
        groups[size].append(i)

        if len(groups[size]) == size:
            res.append(groups[size])
            groups[size] = []
    return res

print(groupThePeople([3,3,3,3,3,1,3]))