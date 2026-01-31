import textwrap
from colorama import Fore, Style


def menu():
    """
    Meniul de comenzi al aplicatiei
    """
    print(f'Nume: {Fore.MAGENTA}Huja Andrei-Iosif{Style.RESET_ALL}      Grupa: {Fore.MAGENTA}213{Style.RESET_ALL}      Cod unic: {Fore.MAGENTA}6Y142794{Style.RESET_ALL}')
    enunt = '''
    Enunț:
    Aplicaţia trebuie să exemplifice cele trei metode de conversie ale numerelor naturale
    (împărţiri succesive, substituţie şi utilizarea unei baze intermediare, de obicei, baza 10)
    între două baze de numeraţie diferite de 10, conversiile rapide între bazele puteri ale lui 2
    (2, 4, 8, 16) şi operaţiile aritmetice într-o bază oarecare p (adunare, scădere, înmulţire cu o
    cifră şi împărţire la o cifră), fără a trece numărul prin baza 10 (p{2,3,...,9,10,16})
    '''
    print(textwrap.dedent(enunt))
    print('Meniul aplicatiei contine urmatoarele:\n'
          '[nume_instructiune] + functionalitatea instructiunii')
    comenzi = '''
    [conv-imp-suc]....metoda de conversie între două baze de numerație prin împărțiri succesive
    [conv-subst]......metoda de conversie între două baze de numerație prin substitutie
    [conv-baza-int]...metoda de conversie între două baze de numerație prin utilizarea unei baze intermediare
    [conv-rap]........metoda de conversii rapide între bazele puteri ale lui 2 (2, 4, 8, 16)
    [add].............adunare într-o bază oarecare p (2, 3, ..., 16) fără a trece numărul prin baza 10
    [sub].............scadere într-o bază oarecare p (2, 3, ..., 16) fără a trece numărul prin baza 10
    [mul].............înmulțire cu o cifră într-o bază oarecare p (2, 3, ..., 16) fără a trece numărul prin baza 10
    [div].............împărțire cu o cifră într-o bază oarecare p (2, 3, ..., 16) fără a trece numărul prin baza 10
    [x]...............închidere aplicație
    '''
    print(textwrap.dedent(comenzi))


def convert_int(input_string: str):
    return int(input_string)


def convert_symbol_digit(input_digit: str):
    if input_digit == 'A':
        return 10
    elif input_digit == 'B':
        return 11
    elif input_digit == 'C':
        return 12
    elif input_digit == 'D':
        return 13
    elif input_digit == 'E':
        return 14
    elif input_digit == 'F':
        return 15


def convert_digit_letter(input_base: str):
    if input_base == '11':
        return 'A'
    elif input_base == '12':
        return 'B'
    elif input_base == '13':
        return 'C'
    elif input_base == '14':
        return 'D'
    elif input_base == '15':
        return 'E'
    elif input_base == '16':
        return 'F'


def create_symbol_list(input_letter_base: str):
    if input_letter_base == 'A':
        return ['A']
    elif input_letter_base == 'B':
        return ['A', 'B']
    elif input_letter_base == 'C':
        return ['A', 'B', 'C']
    elif input_letter_base == 'D':
        return ['A', 'B', 'C', 'D']
    elif input_letter_base == 'E':
        return ['A', 'B', 'C', 'D', 'E']
    elif input_letter_base == 'F':
        return ['A', 'B', 'C', 'D', 'E', 'F']


def convert_symbol_to_number(input_number: str):
    symbol_list = [('A', '10'), ('B', '11'), ('C', '12'), ('D', '13'), ('E', '14'), ('F', '15')]
    for pair in symbol_list:
        if input_number == pair[0]:
            return pair[1]


def convert_number_to_symbol(input_symbol: str):
    letter_list = [('A', '10'), ('B', '11'), ('C', '12'), ('D', '13'), ('E', '14'), ('F', '15')]
    for pair in letter_list:
        if input_symbol == pair[1]:
            return pair[0]


def convert_symbol_number(input_base: str, input_number: str):
    number_list = []
    symbol_base = convert_digit_letter(input_base)
    valid_symbol = create_symbol_list(symbol_base)
    for elem in input_number:
        int_elem = elem
        if not elem.isdigit():
            if elem not in valid_symbol:
                return False
            int_elem = convert_symbol_to_number(int_elem)
        number_list.append(int_elem)
    return number_list


def convert_list_to_number(input_list: list):
    result = ''
    for index in range(len(input_list)):
        if int(input_list[index]) >= 10:
            input_list[index] = convert_number_to_symbol(str(input_list[index]))
        result += str(input_list[index])
    return result


def get_list_for_fast_conv(input_base: str, output_base: str):
    if input_base == '2':
        if output_base == '4':
            return [('00', '0'), ('01', '1'), ('10', '2'), ('11', '3')]
        elif output_base == '8':
            return [('000', '0'), ('001', '1'), ('010', '2'), ('011', '3'), ('100', '4'), ('101', '5'), ('110', '6'), ('111', '7')]
        else:
            return [('0000', '0'), ('0001', '1'), ('0010', '2'), ('0011', '3'), ('0100', '4'), ('0101', '5'), ('0110', '6'), ('0111', '7'), ('1000', '8'), ('1001', '9'), ('1010', '10'), ('1011', '11'), ('1100', '12'), ('1101', '13'), ('1110', '14'), ('1111', '15')]
