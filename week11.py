import string


def analyze_text(text):
    # Create a string corpus that is the text without punctuation
    translator = str.maketrans('', '', string.punctuation)
    corpus = text.translate(translator)
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
    return frequencies


def get_input(file_name):
    """Loads an input file.  The file must be in the same directory as the .py file
    """
    try:
        with open(file_name + ".txt", 'r') as f:
            whole_file = f.read()
    except:
        print(f"Could not load input.")
    return whole_file


def output(file_name, data):
    """Saves output to a file.  The file must be in the same directory as the .py file
    """
    try:
        with open(file_name + ".txt", 'w') as f:
            f.write(str(data))
    except:
        print(f"Could not save output.")


menu_text = """
What would you like to do:
1. Analyze file
2. Analyze file + save output to file
3. Display contents of file
Please enter a number (1-2): """
while True:
    response = int(input(menu_text))
    if response == 1:
        text = get_input(input("Enter the filename of file to analyze (no extension): "))
        print(analyze_text(text))
    elif response == 2:
        text = get_input(input("Enter the filename of file to analyze (no extension): "))
        output_file = input("Enter the filename to save output to (no extension): ")
        output(output_file, analyze_text(text))
    elif response == 3:
        print(get_input(input("Enter the filename of file to display (no extension): ")))
