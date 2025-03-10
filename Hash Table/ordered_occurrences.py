def orderOccurrences(s):
    occurrences = {}
    s = ''.join([num for num in s if not num.isdigit() and num.isalnum()])

    for i in s.lower():
        occurrences[i] = occurrences.get(i, 0) + 1
    return occurrences


# print(orderOccurrences('Banana Boat'))

# sortedHash = sorted(hashTable.items(), key = lambda x: (-x[1], x[0]))

def orderedOccurrences(s):
    occurrences = {}
    words_list = s.split()

    for i in words_list:
        for j in range(len(i)):
            for k in range(j, len(i)):
                occurrences[i.lower()[j:k+1]] = occurrences.get(i.lower()[j:k+1], 0) + 1

    return sorted(occurrences.items(), key = lambda x: (-x[1], x[0]))

# print(orderedOccurrences('Banana Boat'))


def solution(S):
    # Create a dictionary that will map combinations to their frequencies
    combinations = {}
    
    # Convert the input string to lowercase
    S = S.lower()
    
    # Iterate over the length of the input string
    for length in range(len(S)):
        # Iterate over all substrings of the input string that have the current length
        for i in range(len(S) - length):
            substring = S[i:i+length]
            
            # Check if the substring is alphabetic (contains only letters)
            if substring.isalpha():
                # Update the frequency of the substring in the combinations dictionary
                if substring in combinations:
                    combinations[substring] += 1
                else:
                    combinations[substring] = 1
    
    # Sort the combinations by frequency and alphabetically
    sorted_combinations = sorted(combinations.items(), key=lambda x: (-x[1], x[0]))
    
    # Create the result string by joining the combinations and their frequencies
    result = '\n'.join(['{}: {}'.format(count, combination) for combination, count in sorted_combinations])
    
    return result

print(solution('Banana Boat.'))