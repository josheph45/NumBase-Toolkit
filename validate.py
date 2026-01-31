from utils import *

def is_digits_string(input_string: str):
    return input_string.isdigit()


def is_valid_symbol_digit(input_base: str, input_digit: str):
    int_input_base = int(input_base)
    int_input_digit = convert_symbol_digit(input_digit)
    if int_input_digit < int_input_base:
        return True
    return False


def is_valid_symbol_number(input_base: str, input_number: str):
    number_list = convert_symbol_number(input_base, input_number)
    return number_list


def is_valid_digit(input_digit: str):
    aux_input_digit = convert_int(input_digit)
    return aux_input_digit in [2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]


def valid_number_for_base(input_base: str, input_number: str):
    int_input_base = int(input_base)
    if not is_digits_string(input_number):
        if is_valid_symbol_number(input_base, input_number):
            return True
        return False
    for elem in input_number:
        int_elem = int(elem)
        if int_elem >= int_input_base:
            return False
    return True


def valid_digit_for_base(input_base: str, input_digit: str):
    if is_digits_string(input_digit):
        int_input_digit = int(input_digit)
        int_input_base = int(input_base)
        if int_input_digit >= int_input_base:
            return False
    else:
        letter_base = convert_digit_letter(input_base)
        number_list = create_symbol_list(letter_base)
        if input_digit not in number_list:
            return False
    return True
