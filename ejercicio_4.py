from ejercicio_3 import remove_non_word_character, count_words

def get_most_frequent_word(frequency_words:dict[str,int]) -> tuple[str,int]:
    """ Get the most frequent word from a words frequency dictionary
    
    :param frequency_words: dictionary that relate each word with the amount of repetitions (frequency).
    :return: a tuple with the most frequent word in the frequency dictionary.
    """
    most_frequent_word:str = ""
    most_frequent_amount:int = 0
    if isinstance(frequency_words, dict) and len(frequency_words):
        for word, amount in frequency_words.items():
            if amount > most_frequent_amount:
                most_frequent_word = word
                most_frequent_amount = amount
    return most_frequent_word, most_frequent_amount