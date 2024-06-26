def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words
    
def sort_words(words):
    """Sort the words"""
    return sorted(words)
    
def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    return word
    
def print_last_word(words):
    """Prints the last word after popping it off"""
    words = words.pop(-1)
    return words
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last word of the sentence"""
    words = break_words(sentence)
    print(print_first_word(words))
    print(print_last_word(words))
    
def print_first_and_last_sorted(sentence):
    """Sorts the words and prints the first and last one"""
    words = sort_sentence(sentence)
    print(print_first_word(words))
    print(print_last_word(words))

sentence = "All good things come to those who wait."
print(break_words(sentence))
print(sort_words(sentence))
print(print_first_word(break_words(sentence)))
print(print_last_word(break_words(sentence)))
print(sort_sentence(sentence))
print(print_first_and_last(sentence))
print(print_first_and_last_sorted(sentence))
