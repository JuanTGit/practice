

def caesar(text, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_map = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(translation_map)

encrypted_phrase = "XJABSE USBJCPSO"

for shift in range(26): print(shift, caesar(encrypted_phrase, shift))


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(len(alphabet))