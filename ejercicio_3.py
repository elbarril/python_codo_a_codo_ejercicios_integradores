NON_WORD_CHARACTERS = [",", ".", ":", ";", "?", "¿", "¡", "!", '"', "'"]

def remove_non_word_character(word:str) -> str:
    for non_word in NON_WORD_CHARACTERS:
        if non_word in word:
            word = word.replace(non_word, '')
    return word

def count_words(sentence:str) -> dict[str,int]:
    """ Calcule the amount of same words in a sentence
    
    :param sentence: string of words.
    :return: a dictionary that relate each word with the amount of repetitions (frequency).
    """
    words:list[str] =  [remove_non_word_character(word).lower() for word in sentence.split()]
    frequency:dict[str,int] = {}
    for word in words:
        frequency[word] = frequency[word] + 1 if word in frequency else 1
    return frequency