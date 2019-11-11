import string

# Create a string corpus that is the text without punctuation
my_text = "The cat kicked the dog! That cat... he's trouble."
translator = str.maketrans('', '', string.punctuation)
corpus = my_text.translate(translator)

frequencies = dict()

# After punctuation is removes, words are isolated into list, which is then
# digested into a dict of key word, value freq of word...
each_word = corpus.split()

for words in each_word:
    if words.lower() in frequencies:
        frequencies[words.lower()] += 1
    else:
        frequencies[words.lower()] = 1
frequencies["<LENGTH>"] = len(frequencies)
print(frequencies)