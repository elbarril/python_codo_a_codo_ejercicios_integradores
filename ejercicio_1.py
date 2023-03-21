def get_greatest_common_divisor(number_a:int, number_b:int) -> int:
    """ Calcule the GDC of two numbers
    
    :param number_a: first integer number.
    :param number_b: second integer number.
    :return: GDC value of number_a and number_b.
    """
    if number_b == 0:
        return number_a
    else:
        return get_greatest_common_divisor(number_b, number_a % number_b)
    
