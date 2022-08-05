def square_digits(num):
    words = list(str(num)) # split the text
    for word in words:  # for each word in the line:
        print(int(word)**2, end="") # print the word

square = 9119

print(square_digits(square))