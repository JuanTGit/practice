def everyOcc(S):
    occurrence = {}
    S = S.lower()

    for length in range(1, len(S) + 1):
        for i in range(len(S) - length + 1):
            uniques = S[i:i + length]

            if uniques.isalpha():
                if uniques in occurrence:
                    occurrence[uniques] += 1
                else:
                    occurrence[uniques] = 1
    
    ordered_occurrence = sorted(occurrence.items(), key = lambda x: (-x[1], x[0]))

    result = '\n'.join(f'{count}:{combination}' for combination, count in ordered_occurrence)

    return result    
    

print(everyOcc('Banana Boat.'))