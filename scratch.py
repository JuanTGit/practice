list_1 = [2, 4, 8]
list_2 = [1, 3, 2]

def combine(l1, l2):
    new_list = []
    for i in range(len(l1)):
        new_list.append(l1[i]+l2[i])
    return new_list

# print(combine(list_1, list_2))


# answer = 5 * 8
# user_answer = int(input("What is 5 x 8?"))

# print(isinstance(user_answer, (int, float)))

# print(user_answer)

# help(enumerate)


def filter_list(l):
    int_arr = []
    for i in l:
        if type(i) is int:
            int_arr.append(i)
    return int_arr

new_arr = [1,'a','b',0,15]
# print(filter_list(new_arr))


def find_short(s):
    words = s.split(' ')
    words.sort(key=len)
    return len(words[0])

# print(find_short("bitcoin take over the world maybe who knows perhaps"))


def get_middle(s):
    sLen = len(s)
    if sLen % 2 == 0:
        return s[int(sLen/2-1): int(sLen/2+1)]
    else:
        return s[int(sLen/2)]


# print(get_middle('testing'))


def remove_char(s):
    return s[1:-1]

print(remove_char('Hello'))
