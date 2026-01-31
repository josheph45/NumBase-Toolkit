from validate import *
import math


def domain_conv_baza_intermediara(input_base: str, output_base: str, input_number: str):
    base_10_result = domain_conv_substitutie(input_base, input_number)
    base_10_result = str(base_10_result)
    result = domain_conv_impartiri_succesive(output_base, base_10_result)
    return result


def domain_conv_substitutie(input_base: str, input_number: str):
    int_input_base = int(input_base)
    result = 0
    number_list = is_valid_symbol_number(input_base, input_number)
    number_list = number_list[::-1]
    for index in range(len(number_list)):
        aux_digit = int(number_list[index])
        result += aux_digit * (int_input_base ** index)
    return result


def domain_conv_impartiri_succesive(output_base: str, input_number: str):
    int_output_base = int(output_base)
    result = []
    aux_input_number = int(input_number)
    while aux_input_number != 0:
        c = aux_input_number // int_output_base
        t = aux_input_number % int_output_base
        result.append(t)
        aux_input_number = c
    result = convert_list_to_number(result)
    result = result[::-1]
    first_non_zero_index = next((i for i, char in enumerate(result) if char != '0'), len(result))
    result = result[first_non_zero_index:]
    return result


def domain_conv_rapide(input_base: str, output_base: str, input_number: str):
    int_input_base = int(input_base)
    int_output_base = int(output_base)
    result = []
    if int_input_base == int_output_base:
        return input_number
    elif int_input_base == 2:
        conv_list = get_list_for_fast_conv(input_base, output_base)
        aux_index1 = math.log(int(output_base), int(input_base))
        aux_index1 = int(aux_index1)
        aux_index2 = aux_index1 - len(input_number) % aux_index1
        aux_input_number = input_number
        if aux_index2 != 0:
            aux_input_number = '0' * int(aux_index2) + input_number
        index = 0
        while index < len(aux_input_number):
            i = 0
            aux_conv = ''
            while i < aux_index1:
                aux_conv = aux_conv + aux_input_number[index+i]
                i += 1
            for elem in conv_list:
                if aux_conv == elem[0]:
                    aux_conv = elem[1]
            result.append(aux_conv)
            index += aux_index1
        first_non_zero_index = next((i for i, char in enumerate(result) if char != '0'), len(result))
        result = result[first_non_zero_index:]
        result = convert_list_to_number(result)
    else:
        conv_list = get_list_for_fast_conv(output_base, input_base)
        number_list = is_valid_symbol_number(input_base, input_number)
        for index in range(len(number_list)):
            aux_conv = number_list[index]
            for elem in conv_list:
                if aux_conv == elem[1]:
                    aux_conv = elem[0]
            result.append(aux_conv)
        result = ''.join(result)
        first_non_zero_index = next((i for i, char in enumerate(result) if char != '0'), len(result))
        result = result[first_non_zero_index:]
    return result


def domain_add(input_base: str, input_number1: str, input_number2: str):
    aux_input_base = convert_int(input_base)
    reverse_result = []
    t = 0
    number1_list = is_valid_symbol_number(input_base, input_number1)
    number2_list = is_valid_symbol_number(input_base, input_number2)
    reverse_list1 = number1_list.copy()
    reverse_list1.reverse()
    reverse_list2 = number2_list.copy()
    reverse_list2.reverse()
    if len(reverse_list1) > len(reverse_list2):
        aux_index = len(reverse_list2)
        while aux_index < len(reverse_list1):
            reverse_list2.append('0')
            aux_index += 1
    elif len(reverse_list2) > len(reverse_list1):
        aux_index = len(reverse_list1)
        while aux_index < len(reverse_list2):
            reverse_list1.append('0')
            aux_index += 1
    for digit1, digit2 in zip(reverse_list1, reverse_list2):
        int_number1 = int(digit1)
        int_number2 = int(digit2)
        aux_add = int_number1 + int_number2 + t
        if aux_add >= aux_input_base:
            t = 1
            aux_add -= aux_input_base
        else:
            t = 0
        reverse_result.append(aux_add)
    if t == 1:
        reverse_result.append(t)
    reverse_result = convert_list_to_number(reverse_result)
    result = reverse_result[::-1]
    return result


def domain_sub(input_base: str, input_number1: str, input_number2: str):
    aux_input_base = convert_int(input_base)
    reverse_result = []
    t = 0
    number1_list = is_valid_symbol_number(input_base, input_number1)
    number2_list = is_valid_symbol_number(input_base, input_number2)
    reverse_list1 = number1_list.copy()
    reverse_list1.reverse()
    reverse_list2 = number2_list.copy()
    reverse_list2.reverse()
    if len(reverse_list1) > len(reverse_list2):
        aux_index = len(reverse_list2)
        while aux_index < len(reverse_list1):
            reverse_list2.append('0')
            aux_index += 1
    for digit1, digit2 in zip(reverse_list1, reverse_list2):
        int_number1 = int(digit1)
        int_number2 = int(digit2)
        aux_sub = 0
        if t == -1:
            if int_number1 > 0:
                int_number1 -= 1
                t = 0
            else:
                int_number1 = aux_input_base - 1
                t = -1
        else:
            t = 0
        if int_number1 < int_number2:
            t = -1
        if int_number1 + t >= int_number2 and t == 0:
            aux_sub = int_number1 - int_number2 + t
        elif t == -1:
            aux_sub = int_number1 - int_number2 + aux_input_base
        reverse_result.append(aux_sub)
    reverse_result = convert_list_to_number(reverse_result)
    result = reverse_result[::-1]
    first_non_zero_index = next((i for i, char in enumerate(result) if char != '0'), len(result))
    result = result[first_non_zero_index:]
    return result


def domain_mul(input_base: str, input_number: str, input_digit: str):
    aux_input_base = convert_int(input_base)
    reverse_result = []
    if aux_input_base == 2:
        return input_number
    else:
        number_list = is_valid_symbol_number(input_base, input_number)
        reverse_list = number_list.copy()
        reverse_list.reverse()
        if is_digits_string(input_digit):
            int_input_digit = int(input_digit)
        else:
            int_input_digit = convert_symbol_digit(input_digit)
        t = 0
        for index in range(len(reverse_list)):
            int_number = int(reverse_list[index])
            aux_mul = int_number * int_input_digit + t
            t = aux_mul // aux_input_base
            c = aux_mul % aux_input_base
            reverse_result.append(c)
        if t > 0:
            reverse_result.append(t)
    reverse_result = convert_list_to_number(reverse_result)
    result = reverse_result[::-1]
    first_non_zero_index = next((i for i, char in enumerate(result) if char != '0'), len(result))
    result = result[first_non_zero_index:]
    return result


def domain_div(input_base: str, input_number: str, input_digit: str):
    aux_input_base = convert_int(input_base)
    result = []
    if aux_input_base == 2:
        return input_number, 0
    else:
        number_list = is_valid_symbol_number(input_base, input_number)
        if input_digit.isdigit():
            int_input_digit = int(input_digit)
        else:
            int_input_digit = convert_symbol_digit(input_digit)
        t = 0
        for index in range(len(number_list)):
            int_number = int(number_list[index])
            aux_div = int_number + t * aux_input_base
            if aux_div < int_input_digit and index == 1:
                aux_div = aux_div * aux_input_base + int(input_number[index+1])
                index += 1
            c = aux_div // int_input_digit
            t = aux_div % int_input_digit
            result.append(c)
    result = convert_list_to_number(result)
    first_non_zero_index = next((i for i, char in enumerate(result) if char != '0'), len(result))
    result = result[first_non_zero_index:]
    return result, t


def domain_valid_sub(input_base, input_number1: str, input_number2: str):
    number1_baza10 = domain_conv_substitutie(input_base, input_number1)
    number2_baza10 = domain_conv_substitutie(input_base, input_number2)
    number1_baza10 = int(number1_baza10)
    number2_baza10 = int(number2_baza10)
    if number2_baza10 > number1_baza10:
        return False
    return True
