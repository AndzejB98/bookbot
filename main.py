import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
     filepath = sys.argv[1]

from stats import get_num_words

get_num_words(filepath)