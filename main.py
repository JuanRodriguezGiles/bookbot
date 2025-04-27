import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words
from stats import get_num_chars
from stats import get_report

def main():
   if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   else:
      chars_dictionary = get_num_chars(get_book_text(sys.argv[1]))
      print("============ BOOKBOT ============")
      print(f"Analyzing book found at {sys.argv[1]}")
      print("----------- Word Count ----------")
      num_words = get_num_words(get_book_text(sys.argv[1]))
      print(f"Found {num_words} total words")
      print("--------- Character Count -------")
      chars_list = get_report(chars_dictionary)
      for dic in chars_list:
          if dic["char"].isalpha():
              print(f"{dic["char"]}: {dic["num"]}") 

main()