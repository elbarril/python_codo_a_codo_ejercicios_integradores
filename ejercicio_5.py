PROMPT_MESSAGE = "Please enter an integer number: "
VALUE_ERROR_MESSAGE = "The value is not a number. Try again."

def get_int_recursively(prompt:str=PROMPT_MESSAGE) -> int:
    """ Get integer from a string
    
    :param prompt: message to show in console before user input string value
    :return: integer from string
    """
    try:
        number = int(input(prompt))
        return number
    except ValueError:
        print(VALUE_ERROR_MESSAGE)
        return get_int_recursively(prompt)


def get_int_iteratively() -> int:
    """ Get integer from a string
    
    :return: integer from string
    """

    while True:
        try:
            number = int(input(PROMPT_MESSAGE))
            return number
        except ValueError:
            print(VALUE_ERROR_MESSAGE)