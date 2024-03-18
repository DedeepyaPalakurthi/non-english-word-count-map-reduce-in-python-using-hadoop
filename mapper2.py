import sys
import re
import enchant

#Initialize the English dictionary
english_dict = enchant.Dict("en_US")

# Read entire line from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.lower().split(" ")
    # Assign count one to each word
    for word in words:
        word = word.replace('\"', "")
        word = word.replace(",", "")
        word = word.replace(";", "")
        word = word.replace("!", "")
        word = word.replace("-", "")
        word = word.replace("_", "")
        word = word.replace("?", "")
        word = word.replace("|", "")
        if word != "":
            if not english_dict.check(word):
                print(f"{word}\t1")