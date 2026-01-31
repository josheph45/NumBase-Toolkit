from user_interface import *


def run_app():
    """
    Functia principala de rulare a aplicatiei
    """
    menu()
    while True:
        command = input('>>> ')
        command.lower().strip()
        if command == 'x':
            print('Aplicație închisă :(')
            return
        elif command == 'add':
            ui_add()
        elif command == 'sub':
            ui_sub()
        elif command == 'mul':
            ui_mul()
        elif command == 'div':
            ui_div()
        elif command == 'conv-rap':
            ui_conv_rapide()
        elif command == 'conv-imp-suc':
            ui_conv_impartiri_succesive()
        elif command == 'conv-subst':
            ui_conv_substitutie()
        elif command == 'conv-baza-int':
            ui_conv_baza_intermediara()
        else:
            print('Comandă invalida')
