bookpath = "books/frankenstein.txt"

with open(bookpath) as f:
    file_contents = f.read()



letters_list = []

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    letters_list.append([file_contents.lower().count(letter), letter])



print(f"--- Begin report of {bookpath} ---")
print(len(file_contents.split()), "words were found in the document")
print()

letters_list.sort(reverse=True)

for element in letters_list:
    print(f"The '{element[1]}' character was found {element[0]} times")