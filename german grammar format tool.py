import nltk

def capitalize_nouns(input_string):
    # Tokenize the input string into individual words
    words = nltk.word_tokenize(input_string)

    # Tag each word with its part of speech
    tagged_words = nltk.pos_tag(words)

    # Capitalize nouns
    capitalized_words = [word.capitalize() if pos.startswith('N') else word for word, pos in tagged_words]

    # Join the capitalized words back into a string
    capitalized_string = ' '.join(capitalized_words)

    return capitalized_string

# Request input
input_string = input('Enter a sentence: ')
capitalized_string = capitalize_nouns(input_string)
print(capitalized_string)