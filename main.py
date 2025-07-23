from stats import count_words, get_char_freq, list_dict, sort_on
import sys

if len(sys.argv) < 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filename = sys.argv[1]  # Get the first argument after the script name
print(f"You passed in the file: {filename}")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    #print(get_book_text("./books/frankenstein.txt"))
    print(get_book_text(filename))

# main()



#num_words = count_words(get_book_text("./books/frankenstein.txt"))
#num_chars = get_char_freq(get_book_text("./books/frankenstein.txt"))
num_words = count_words(get_book_text(filename))
num_chars = get_char_freq(get_book_text(filename))

# print(f"{num_words} words found in the document")
# print(num_chars)

list_chars_dict = list_dict(num_chars)

list_chars_dict.sort(reverse=True, key=sort_on)
print(list_chars_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {filename}")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")

for item in list_chars_dict:
    if item["char"].isalpha():
        print(item["char"] + ": " + str(item["num"]))