def menu_initial():
    print('=' * 42)
    print(' ' * 12, 'Value Converter', ' ' * 12)
    print('=' * 42)
    print(' ')
    print('|  [1] convert decimal to binary         |')
    print('|  [2] convert decimal to octal          |')
    print('|  [3] convert decimal to hexadecimal    |')
    print('|  [4] convert binary to decimal         |')
    print('|  [5] convert binary to octal           |')
    print('|  [6] convert binary to hexadecimal     |')
    print('|  [7] convert octal to decimal          |')
    print('|  [8] convert octal to binário          |')
    print('|  [9] convert octal to hexadecimal      |')
    print('|  [10] convert hexadecimal to decimal   |')
    print('|  [11] convert hexadecimal to binary    |')
    print('|  [12] convert hexadecimal to octal     |')


def basic_conversions(choices):
    if choices == 1:
        number = int(input('Enter the number of your choice: '))
        print(f'The binary value is: {bin(number)[2:]}')

    elif choices == 2:
        number = int(input('Enter the number of your choice: '))
        print(f'The octal value is: {oct(number)[2:]}')

    elif choices == 3:
        number = int(input('Enter the number of your choice: '))
        print(f'The hexadecimal value is: {hex(number)[2:]}')


def conversions_binarias(choices):
    if choices == 4:
        binary = int(input("Enter the binary code: "))
        n = len(str(binary))
        result = 0
        i = 0
        while n >= 0:
            resto = binary % 10
            result = result + (resto * (2**i))
            n = n - 1
            i = i + 1
            binary = binary // 10
        print(F'The decimal value is: {result}')

    if choices == 5:
        list_trans = list()
        result = str()
        number = str(input('Enter the binary code: '))
        number_modif = '0'
        amount = len(number)
        accretion = amount % 3

        if accretion == 1:
            number_modif = '00' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 3
                N2 += 3

        elif accretion == 2:
            number_modif = '0' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 3
                N2 += 3

        elif accretion == 0:
            number_modif = number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 3
                N2 += 3
        value = len(list_trans)
        for base in range(0, value):
            if base == 0:
                if list_trans[base] == '000':
                    result = '0'
                elif list_trans[base] == '001':
                    result = '1'
                elif list_trans[base] == '010':
                    result = '2'
                elif list_trans[base] == '011':
                    result = '3'
                elif list_trans[base] == '100':
                    result = '4'
                elif list_trans[base] == '101':
                    result = '5'
                elif list_trans[base] == '110':
                    result = '6'
                elif list_trans[base] == '111':
                    result = '7'
            else:
                if list_trans[base] == '000':
                    result += '0'
                elif list_trans[base] == '001':
                    result += '1'
                elif list_trans[base] == '010':
                    result += '2'
                elif list_trans[base] == '011':
                    result += '3'
                elif list_trans[base] == '100':
                    result += '4'
                elif list_trans[base] == '101':
                    result += '5'
                elif list_trans[base] == '110':
                    result += '6'
                elif list_trans[base] == '111':
                    result += '7'
        print(f'The octal value is: {result}')

    if choices == 6:
        list_trans = list()
        result = str()
        number = (input('Enter binary code: '))
        number_modif = '0'
        amount = len(number)
        accretion = amount % 4

        if accretion == 1:
            number_modif = '000' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        elif accretion == 2:
            number_modif = '00' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        elif accretion == 3:
            number_modif = '0' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        elif accretion == 0:
            number_modif = number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        valuer = len(list_trans)
        for base in range(0, valuer):
            if base == 0:
                if list_trans[base] == '0000':
                    result = '0'
                elif list_trans[base] == '0001':
                    result = '1'
                elif list_trans[base] == '0010':
                    result = '2'
                elif list_trans[base] == '0011':
                    result = '3'
                elif list_trans[base] == '0100':
                    result = '4'
                elif list_trans[base] == '0101':
                    result = '5'
                elif list_trans[base] == '0110':
                    result = '6'
                elif list_trans[base] == '0111':
                    result = '7'
                elif list_trans[base] == '1000':
                    result = '8'
                elif list_trans[base] == '1001':
                    result = '9'
                elif list_trans[base] == '1010':
                    result = 'A'
                elif list_trans[base] == '1011':
                    result = 'B'
                elif list_trans[base] == '1100':
                    result = 'C'
                elif list_trans[base] == '1101':
                    result = 'D'
                elif list_trans[base] == '1110':
                    result = 'D'
                elif list_trans[base] == '1111':
                    result = 'E'
            else:
                if list_trans[base] == '0000':
                    result += '0'
                elif list_trans[base] == '0001':
                    result += '1'
                elif list_trans[base] == '0010':
                    result += '2'
                elif list_trans[base] == '0011':
                    result += '3'
                elif list_trans[base] == '0100':
                    result += '4'
                elif list_trans[base] == '0101':
                    result += '5'
                elif list_trans[base] == '0110':
                    result += '6'
                elif list_trans[base] == '0111':
                    result += '7'
                elif list_trans[base] == '1000':
                    result += '8'
                elif list_trans[base] == '1001':
                    result += '9'
                elif list_trans[base] == '1010':
                    result += 'A'
                elif list_trans[base] == '1011':
                    result += 'B'
                elif list_trans[base] == '1100':
                    result += 'C'
                elif list_trans[base] == '1101':
                    result += 'D'
                elif list_trans[base] == '1110':
                    result += 'D'
                elif list_trans[base] == '1111':
                    result += 'E'
        print(f'The hexadecimal value is: {result}')


def octal_conversions(choices):
    if choices == 7:
        octnum = int(input('Enter the octal code: '))

        chk = 0
        i = 0
        value = 0
        while octnum != 0:
            rem = octnum % 10
            if rem > 7:
                chk = 1
                break
            value = value + (rem * (8 ** i))
            i = i+1
            octnum = int(octnum/10)

        if chk == 0:
            print(F'The decimal value is: {value}')
        else:
            print("\nInvalid number!")

    if choices == 8:
        list_trans = list()
        value = str()
        number = str(input('Enter the octal code: '))
        amount = len(number)
        for trans in range(0, amount):
            list_trans.append(number[trans])
        value = len(list_trans)
        for base in range(0, value):
            if base == 0:
                if list_trans[base] == '0':
                    value = '0'
                elif list_trans[base] == '1':
                    value = '1'
                elif list_trans[base] == '2':
                    value = '10'
            else:
                if list_trans[base] == '0':
                    value += '000'
                elif list_trans[base] == '1':
                    value += '001'
                elif list_trans[base] == '2':
                    value += '010'
                elif list_trans[base] == '3':
                    value += '011'
                elif list_trans[base] == '4':
                    value += '100'
                elif list_trans[base] == '5':
                    value += '101'
                elif list_trans[base] == '6':
                    value += '110'
                elif list_trans[base] == '7':
                    value += '111'
        print(f'The binary value is: {value}')

    if choices == 9:
        list_trans = list()
        value = str()
        number = str(input('Enter the octal code: '))
        amount = len(number)
        for trans in range(0, amount):
            list_trans.append(number[trans])
        value = len(list_trans)
        for base in range(0, value):
            if base == 0:
                if list_trans[base] == '0':
                    value = '0'
                elif list_trans[base] == '1':
                    value = '1'
                elif list_trans[base] == '2':
                    value = '10'
            else:
                if list_trans[base] == '0':
                    value += '000'
                elif list_trans[base] == '1':
                    value += '001'
                elif list_trans[base] == '2':
                    value += '010'
                elif list_trans[base] == '3':
                    value += '011'
                elif list_trans[base] == '4':
                    value += '100'
                elif list_trans[base] == '5':
                    value += '101'
                elif list_trans[base] == '6':
                    value += '110'
                elif list_trans[base] == '7':
                    value += '111'
        list_trans_2 = list()
        result = str()
        number = value
        number_modif = '0'
        amount = len(number)
        accretion = amount % 4

        if accretion == 1:
            number_modif = '000' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans_2.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        elif accretion == 2:
            number_modif = '00' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans_2.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        elif accretion == 3:
            number_modif = '0' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans_2.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        elif accretion == 0:
            number_modif = number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, value_quant):
                list_trans_2.append(number_modif[N1:N2])
                N1 += 4
                N2 += 4

        value = len(list_trans_2)
        for base in range(0, value):
            if base == 0:
                if list_trans_2[base] == '0000':
                    result = '0'
                elif list_trans_2[base] == '0001':
                    result = '1'
                elif list_trans_2[base] == '0010':
                    result = '2'
                elif list_trans_2[base] == '0011':
                    result = '3'
                elif list_trans_2[base] == '0100':
                    result = '4'
                elif list_trans_2[base] == '0101':
                    result = '5'
                elif list_trans_2[base] == '0110':
                    result = '6'
                elif list_trans_2[base] == '0111':
                    result = '7'
                elif list_trans_2[base] == '1000':
                    result = '8'
                elif list_trans_2[base] == '1001':
                    result = '9'
                elif list_trans_2[base] == '1010':
                    result = 'A'
                elif list_trans_2[base] == '1011':
                    result = 'B'
                elif list_trans_2[base] == '1100':
                    result = 'C'
                elif list_trans_2[base] == '1101':
                    result = 'D'
                elif list_trans_2[base] == '1110':
                    result = 'D'
                elif list_trans_2[base] == '1111':
                    result = 'E'
            else:
                if list_trans_2[base] == '0000':
                    result += '0'
                elif list_trans_2[base] == '0001':
                    result += '1'
                elif list_trans_2[base] == '0010':
                    result += '2'
                elif list_trans_2[base] == '0011':
                    result += '3'
                elif list_trans_2[base] == '0100':
                    result += '4'
                elif list_trans_2[base] == '0101':
                    result += '5'
                elif list_trans_2[base] == '0110':
                    result += '6'
                elif list_trans_2[base] == '0111':
                    result += '7'
                elif list_trans_2[base] == '1000':
                    result += '8'
                elif list_trans_2[base] == '1001':
                    result += '9'
                elif list_trans_2[base] == '1010':
                    result += 'A'
                elif list_trans_2[base] == '1011':
                    result += 'B'
                elif list_trans_2[base] == '1100':
                    result += 'C'
                elif list_trans_2[base] == '1101':
                    result += 'D'
                elif list_trans_2[base] == '1110':
                    result += 'E'
                elif list_trans_2[base] == '1111':
                    result += 'F'
        print(f'The value hexadecimal is: {result}')


def hexadecimal_conversions(choices):

    if choices == 10:
        conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                            '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        hexadecimal = input("Enter the Hexadecimal value: ").strip().upper()
        decimal = 0
        power = len(hexadecimal) - 1

        for digit in hexadecimal:
            decimal += conversion_table[digit]*16**power
            power -= 1
        print(F'The decimal value is: {decimal}')

    if choices == 11:
        list_trans = list()
        code_hexa = input('Enter the hexadecimal code: ')
        amount = len(code_hexa)
        for trans in range(0, amount):
            list_trans.append(code_hexa[trans])
        for base in range(0, amount):
            if base == 0:
                if list_trans[base] == '0':
                    result = '0000'
                elif list_trans[base] == '1':
                    result = '1'
                elif list_trans[base] == '2':
                    result = '10'
                elif list_trans[base] == '3':
                    result = '11'
                elif list_trans[base] == '4':
                    result = '100'
                elif list_trans[base] == '5':
                    result = '101'
                elif list_trans[base] == '6':
                    result = '110'
                elif list_trans[base] == '7':
                    result = '111'
                elif list_trans[base] == '8':
                    result = '1000'
                elif list_trans[base] == '9':
                    result = '1001'
                elif list_trans[base] == 'A':
                    result = '1010'
                elif list_trans[base] == 'B':
                    result = '1011'
                elif list_trans[base] == 'C':
                    result = '1100'
                elif list_trans[base] == 'D':
                    result = '1101'
                elif list_trans[base] == 'E':
                    result = '1110'
                elif list_trans[base] == 'E':
                    result = '1111'
            else:
                if list_trans[base] == '0':
                    result += '0000'
                elif list_trans[base] == '1':
                    result += '0001'
                elif list_trans[base] == '2':
                    result += '0010'
                elif list_trans[base] == '3':
                    result += '0011'
                elif list_trans[base] == '4':
                    result += '0100'
                elif list_trans[base] == '5':
                    result += '0101'
                elif list_trans[base] == '6':
                    result += '0110'
                elif list_trans[base] == '7':
                    result += '0111'
                elif list_trans[base] == '8':
                    result += '1000'
                elif list_trans[base] == '9':
                    result += '1001'
                elif list_trans[base] == 'A':
                    result += '1010'
                elif list_trans[base] == 'B':
                    result += '1011'
                elif list_trans[base] == 'C':
                    result += '1100'
                elif list_trans[base] == 'D':
                    result += '1101'
                elif list_trans[base] == 'E':
                    result += '1110'
                elif list_trans[base] == 'F':
                    result += '1111'
        print(f'The value binário is: {result}')

    if choices == 12:
        list_trans = list()
        code_hexa = input('Enter the hexadecimal code: ')
        amount = len(code_hexa)
        result = str()
        for trans in range(0, amount):
            list_trans.append(code_hexa[trans])
        for base in range(0, amount):
            if base == 0:
                if list_trans[base] == '0':
                    result = '0000'
                elif list_trans[base] == '1':
                    result = '1'
                elif list_trans[base] == '2':
                    result = '10'
                elif list_trans[base] == '3':
                    result = '11'
                elif list_trans[base] == '4':
                    result = '100'
                elif list_trans[base] == '5':
                    result = '101'
                elif list_trans[base] == '6':
                    result = '110'
                elif list_trans[base] == '7':
                    result = '111'
                elif list_trans[base] == '8':
                    result = '1000'
                elif list_trans[base] == '9':
                    result = '1001'
                elif list_trans[base] == 'A':
                    result = '1010'
                elif list_trans[base] == 'B':
                    result = '1011'
                elif list_trans[base] == 'C':
                    result = '1100'
                elif list_trans[base] == 'D':
                    result = '1101'
                elif list_trans[base] == 'E':
                    result = '1110'
                elif list_trans[base] == 'E':
                    result = '1111'
            else:
                if list_trans[base] == '0':
                    result += '0000'
                elif list_trans[base] == '1':
                    result += '0001'
                elif list_trans[base] == '2':
                    result += '0010'
                elif list_trans[base] == '3':
                    result += '0011'
                elif list_trans[base] == '4':
                    result += '0100'
                elif list_trans[base] == '5':
                    result += '0101'
                elif list_trans[base] == '6':
                    result += '0110'
                elif list_trans[base] == '7':
                    result += '0111'
                elif list_trans[base] == '8':
                    result += '1000'
                elif list_trans[base] == '9':
                    result += '1001'
                elif list_trans[base] == 'A':
                    result += '1010'
                elif list_trans[base] == 'B':
                    result += '1011'
                elif list_trans[base] == 'C':
                    result += '1100'
                elif list_trans[base] == 'D':
                    result += '1101'
                elif list_trans[base] == 'E':
                    result += '1110'
                elif list_trans[base] == 'F':
                    result += '1111'
        list_trans = list()
        result = str()
        number = result
        number_modif = '0'
        amount = len(number)
        accretion = amount % 3

        if accretion == 1:
            number_modif = '00' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 3
                N2 += 3

        elif accretion == 2:
            number_modif = '0' + number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 3
                N2 += 3

        elif accretion == 0:
            number_modif = number
            amount_modif = len(number_modif)
            value_quant = amount_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, value_quant):
                list_trans.append(number_modif[N1:N2])
                N1 += 3
                N2 += 3
        value = len(list_trans)
        for base in range(0, value):
            if base == 0:
                if list_trans[base] == '000':
                    result = '0'
                elif list_trans[base] == '001':
                    result = '1'
                elif list_trans[base] == '010':
                    result = '2'
                elif list_trans[base] == '011':
                    result = '3'
                elif list_trans[base] == '100':
                    result = '4'
                elif list_trans[base] == '101':
                    result = '5'
                elif list_trans[base] == '110':
                    result = '6'
                elif list_trans[base] == '111':
                    result = '7'
            else:
                if list_trans[base] == '000':
                    result += '0'
                elif list_trans[base] == '001':
                    result += '1'
                elif list_trans[base] == '010':
                    result += '2'
                elif list_trans[base] == '011':
                    result += '3'
                elif list_trans[base] == '100':
                    result += '4'
                elif list_trans[base] == '101':
                    result += '5'
                elif list_trans[base] == '110':
                    result += '6'
                elif list_trans[base] == '111':
                    result += '7'
        print(result)
