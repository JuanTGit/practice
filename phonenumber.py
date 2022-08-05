def create_phone_number(n):
    s = "".join([str(i) for i in n])
    return f"({s[:3]}) {s[3:6]}-{s[6:]}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    