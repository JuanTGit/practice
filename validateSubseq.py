array = [1, 4, 7, -1, 8, 2]
seq = [4, -1, 2]


def validateSub(array, sequence):

    seq_pointer = 0
    for i in range(len(array)):
        if seq_pointer < len(sequence) and array[i] == sequence[seq_pointer]:
            seq_pointer += 1
    return seq_pointer == len(sequence)


print(validateSub(array, seq))