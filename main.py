def main():
    book_path = "books/frankenstein.txt"
    text = get_file_contents(book_path)
    num_words = get_num_words(text)
    num_letters = dict_to_sorted_array(count_letters(text))
    get_report(book_path, num_words, num_letters)

def get_report(book_path, number_words, number_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_words} words found in the document\n")
    for letter in number_letters:
        print(f"The '{letter[1]}' character was found {letter[0]} times")
    print(F"--- End report ---")

def dict_to_sorted_array(mydict):
    result = []
    for item in mydict:
        result.append([mydict[item], item])
    result.sort(reverse=True)
    return result
    
def get_file_contents(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(string):
    return len(string.split())

def count_letters(string):
    result = {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in string.lower():
        if letter not in result and letter in letters:
            result[letter] = 1
        elif letter in result and letter in letters:
            result[letter] += 1
    return result


main()