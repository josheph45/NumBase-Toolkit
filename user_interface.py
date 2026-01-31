from colorama import Fore, Style
from domain import *


def ui_conv_baza_intermediara():
    try:
        base1 = input('Introduceți baza input: ')
        if not is_valid_digit(base1):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        number = input('Introduceți numărul de convertit: ')
        if not valid_number_for_base(base1, number):
            raise ValueError(f'Număr invalid pentru baza {base1}')
        base2 = input('Introduceți baza în care vreți să convertiți numărul: ')
        if not is_valid_digit(base2):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        result = domain_conv_baza_intermediara(base1, base2, number)
        print(f"{Fore.CYAN}{number}{Style.RESET_ALL}({Fore.YELLOW}{base1}{Style.RESET_ALL}) = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base2}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_conv_substitutie():
    try:
        base = input('Introduceți baza input: ')
        if not is_valid_digit(base):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        number = input('Introduceți numărul de convertit: ')
        if not valid_number_for_base(base, number):
            raise ValueError(f'Număr invalid pentru baza {base}')
        result = domain_conv_substitutie(base, number)
        print(f"{Fore.CYAN}{number}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL}) = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}10{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_conv_impartiri_succesive():
    try:
        number = input('Introduceți numărul de convertit(în baza 10): ')
        if not number.isdigit():
            raise ValueError('Număr invalid pentru baza 10')
        base = input('Introduceți baza în care vreți să convertiți numărul: ')
        if not is_valid_digit(base):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        result = domain_conv_impartiri_succesive(base, number)
        print(f"{Fore.CYAN}{number}{Style.RESET_ALL}({Fore.YELLOW}10{Style.RESET_ALL}) = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_conv_rapide():
    try:
        valid_base = ['2', '4', '8', '16']
        base1 = input('Introduceți baza input: ')
        if base1 not in valid_base:
            raise ValueError('Bază invalidă pentru converie rapidă(p{2, 4, 8, 16})')
        number = input('Introduceți numărul de convertit: ')
        if not valid_number_for_base(base1, number):
            raise ValueError(f'Număr invalid pentru baza {base1}')
        base2 = input('Introduceți baza în care vreți să convertiți numărul: ')
        if base2 not in valid_base:
            raise ValueError('Bază invalidă pentru conversie rapidă(p{2, 4, 8, 16})')
        if base1 != '2' and base2 != '2':
            raise ValueError('Baza input/output trebuie să fie 2')
        result = domain_conv_rapide(base1, base2, number)
        print(f"{Fore.CYAN}{number}{Style.RESET_ALL}({Fore.YELLOW}{base1}{Style.RESET_ALL}) = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base2}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_add():
    try:
        base = input('Introduceți baza în care vreți să efectuați adunarea: ')
        if not is_valid_digit(base):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        number1 = input('Introduceți numărul pe care vreți să îl adunați: ')
        if not valid_number_for_base(base, number1):
            raise ValueError(f'Număr invalid pentru baza {base}')
        number2 = input('Introduceți al doilea număr pe care vreți să îl adunați: ')
        if not valid_number_for_base(base, number2):
            raise ValueError(f'Număr invalid pentru baza {base}')
        result = domain_add(base, number1, number2)
        print(f"{Fore.CYAN}{number1}{Style.RESET_ALL} + {Fore.CYAN}{number2}{Style.RESET_ALL} = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_sub():
    try:
        base = input('Introduceți baza în care vreți să efectuați scăderea: ')
        if not is_valid_digit(base):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        number1 = input('Introduceți numărul din care vreți să scădeți: ')
        if not valid_number_for_base(base, number1):
            raise ValueError(f'Număr invalid pentru baza {base}')
        number2 = input('Introduceți numărul pe care vreți să îl scădeți: ')
        if not valid_number_for_base(base, number2):
            raise ValueError(f'Număr invalid pentru baza {base}')
        if not domain_valid_sub(base, number1, number2):
            raise ValueError(f'Descăzut trebuie să fie mai mare decât scăzător')
        result = domain_sub(base, number1, number2)
        print(f"{Fore.CYAN}{number1}{Style.RESET_ALL} - {Fore.CYAN}{number2}{Style.RESET_ALL} = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_mul():
    try:
        base = input('Introduceți baza în care vreți să efectuați înmulțirea: ')
        if not is_valid_digit(base):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        number = input('Introduceți numărul pe care vreți să îl înmulțiți: ')
        if not valid_number_for_base(base, number):
            raise ValueError(f'Număr invalid pentru baza {base}')
        digit = input(f'Introduceți cifra cu care vreți să înmulțiți numărul: ')
        if not valid_digit_for_base(base, digit):
            raise ValueError(f'Cifră invalidă pentru baza {base}')
        if digit != '0':
            result = domain_mul(base, number, digit)
        else:
            result = 0
        print(f"{Fore.CYAN}{number}{Style.RESET_ALL} * {Fore.CYAN}{digit}{Style.RESET_ALL} = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')


def ui_div():
    try:
        base = input('Introduceți baza în care vreți să efectuați împărțirea: ')
        if not is_valid_digit(base):
            raise ValueError('Bază invalidă (p{2,3,...,9,10,16})')
        number = input('Introduceți numărul pe care vreți să îl împărțiți: ')
        if not valid_number_for_base(base, number):
            raise ValueError(f'Număr invalid pentru baza {base}')
        digit = input(f'Introduceți cifra la care vreți să împărțiți numărul: ')
        if not valid_digit_for_base(base, digit):
            raise ValueError(f'Cifră invalidă pentru baza {base}')
        if digit == '0':
            raise ValueError(f'Împărțirea la 0 nedefinită')
        elif digit == '1':
            result = number
            print(f"{Fore.CYAN}{number}{Style.RESET_ALL} : {Fore.CYAN}{digit}{Style.RESET_ALL} = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL})")
        else:
            result, rest = domain_div(base, number, digit)
            if rest > 0:
                print(f"{Fore.CYAN}{number}{Style.RESET_ALL} : {Fore.CYAN}{digit}{Style.RESET_ALL} = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL}), rest {Fore.CYAN}{rest}{Style.RESET_ALL}")
            else:
                print(f"{Fore.CYAN}{number}{Style.RESET_ALL} : {Fore.CYAN}{digit}{Style.RESET_ALL} = {Fore.CYAN}{result}{Style.RESET_ALL}({Fore.YELLOW}{base}{Style.RESET_ALL})")
    except ValueError as ve:
        print(f'{Fore.RED}{ve}{Style.RESET_ALL}')
