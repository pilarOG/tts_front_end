import re


ALLOWED_CHARACTERS = ' 1234567890qwertyuioplkjhgfdsazxcvbnm.,;:-\'!?QWERTYUIOPLKJHGFDSAZXCVBNM'
PUNCTUATION = '.,;:-\'!?'

# split input text in sentences
def split_sentences(input_text):
    removed_symbols = []
    cleaned_symbols = []
    for symbol in input_text:
        if symbol in ALLOWED_CHARACTERS:
            cleaned_symbols.append(symbol)
        else:
            removed_symbols.append(symbol)
    input_text_marked = [symbol+' <S> ' if symbol in '.!?' else symbol for symbol in cleaned_symbols]
    sentences = ''.join(input_text_marked).split(' <S> ')
    return sentences, removed_symbols


# tokenizer: split input text into tokens
def tokenize(sentence):
    # detach punctuation
    for symbol in PUNCTUATION:
        sentence = sentence.replace(symbol, ' '+symbol+' ')

    words = sentence.split(' ')
    return words

# classify word given symbols
def classify_word(word):
    word = word.lower()
    # all numbers?
    if len(re.findall(r'[0-9]', word)) == len(word):
        word_class = 'number'
    # all alphabetical
    elif len(re.findall(r'[a-z]', word)) == len(word):
        if [n for n in word if n in 'aeiou']:
            word_class = 'alphabetical'
        else:
            word_class = 'abbreviation'
    else:
        word_class = 'other'

    return word_class


# test
sentences, _ = split_sentences('Horseshoe bats are a family of more than 100 bat species. They are found throughout Africa, Asia, Europe, and Oceania. While many are brown, some species have black, reddish, or orange fur. They are small, weighing less than 30 g (1.1 oz), and are named after the horseshoe-shaped flap of skin on their noses, which helps them echolocate.')
for sentence in sentences:
    words = tokenize(sentence)
    for word in words:
        if word:
            print (word)
            classify_word(word)
