from ejercicio_1 import get_greatest_common_divisor

def get_least_common_multiple(number_a:int, number_b:int) -> int:
    """ Calcule the LCM of two numbers
    
    :param number_a: first integer number.
    :param number_b: second integer number.
    :return: LCM value of number_a and number_b.
    """
    greatest_common_divisor:int = get_greatest_common_divisor(number_a, number_b)
    return (number_a*number_b) // greatest_common_divisor
    
