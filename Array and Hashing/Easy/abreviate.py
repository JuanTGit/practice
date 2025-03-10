def abbrev_name(name):
    output = ''
    name = name.upper()
    
    for word in name.split():
        output += word[0]
    return '.'.join(output)

print(abbrev_name('Rachel Smith'))