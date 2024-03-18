import sys

# Initialize variables to store previous word and count
previous_word = None
previous_count = 0

# Read input from standard input (STDIN) line by line
for line in sys.stdin:
    # Remove leading and trailing whitespace from the line
    line = line.strip()

    # Split the line into word and count based on tab delimiter
    current_word = line.split('\t')[0]
    count = 1  # Since each line represents one word, count is always 1

    # Check if the current word is the same as the previous word
    if previous_word == current_word:
        # If the current word is the same, increment the count
        previous_count += int(count)
    else:
        # If the current word is different, print the previous word and its count
        if previous_word:
            print(f"{previous_word}\t{previous_count}")

        # Update previous_word to the current word and reset count
        previous_word = current_word
        previous_count = count

# Print the last word and its count if it exists
if previous_word:
    print(f"{previous_word}\t{previous_count}")


