# Write a script that takes a paragraph of text as its input, 
# and returns a dictionary containing the tally of how many 
# times each word in the alphabet was used in the text.
import string

def remove_punctuation(str):
    updated_str = ""
    for s in str:
        if s not in string.punctuation:
            updated_str += s
    return updated_str

def count_the_words(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

phrase = input("Enter a phrase ")
word_count = count_the_words(remove_punctuation(phrase))
print(word_count)