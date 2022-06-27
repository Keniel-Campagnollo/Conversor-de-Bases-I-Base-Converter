def menu_inicial():
    print('=' * 50)
    print(' '* 15,'Conversor de valores',' ' * 15 )
    print('=' * 50)
    print(' ')
    print('|  [1] para converter decimal para binário       |')
    print('|  [2] para converter decimal para octal         |')
    print('|  [3] para converter decimal para hexadecimal   |')
    print('|  [4] para converter binário para decimal       |')
    print('|  [5] para converter binário para octal         |')
    print('|  [6] para converter binário para hexadecimal   |')
    print('|  [7] para converter octal para decimal         |')
    print('|  [8] para converter octal para binário         |')
    print('|  [9] para converter octal para hexadecimal     |')
    print('|  [10] para converter hexadecimal para decimal  |')
    print('|  [11] para converter hexadecimal para binário  |')
    print('|  [12] para converter hexadecimal para octal    |')


def conversões_básicas(escolhas):
    if escolhas == 1:
        Numero = int(input('Digite o numero de sua escolha: '))
        print(f'O valor binário é: {bin(Numero)[2:]}')
   
    elif escolhas == 2:
        Numero = int(input('Digite o numero de sua escolha: '))
        print(f'O valor octal é: {oct(Numero)[2:]}')
        
    elif escolhas == 3:
        Numero = int(input('Digite um numero de sua escolha: '))
        print(f'O valor hexadecimal é: {hex(Numero)[2:]}')


def conversões_binaria(escolhas):
    if escolhas == 4:
        binario = int(input("Digite o número binário: "))
        n = len(str(binario))
        resultado = 0
        i = 0
        while n >= 0:
            resto = binario % 10
            resultado = resultado + (resto * (2**i))
            n = n - 1
            i = i + 1
            binario = binario // 10
        print(F'O valor decimal é: {resultado}')
    
    if escolhas == 5:
        lista_trans = list()
        Resultado = str()
        numero = str(input('Digite o código binário: '))
        numero_modif = '0'
        quantia = len(numero)
        acrecimo = quantia % 3
        
        if acrecimo == 1:
            numero_modif = '00' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 3
                N2 += 3
        
        elif acrecimo == 2:
            numero_modif = '0' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 3
                N2 += 3
        
        elif acrecimo == 0:
            numero_modif = numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 3
                N2 += 3
        valor = len(lista_trans)
        for base in range(0, valor):
            if base == 0:
                if lista_trans[base] == '000':
                    Resultado = '0'
                elif lista_trans[base] == '001':
                    Resultado = '1'
                elif lista_trans[base] == '010':
                    Resultado = '2'
                elif lista_trans[base] == '011':
                    Resultado = '3'
                elif lista_trans[base] == '100':
                    Resultado = '4'
                elif lista_trans[base] == '101':
                    Resultado = '5'
                elif lista_trans[base] == '110':
                    Resultado = '6'
                elif lista_trans[base] == '111':
                    Resultado = '7'
            else:
                if lista_trans[base] == '000':
                    Resultado += '0'
                elif lista_trans[base] == '001':
                    Resultado += '1'
                elif lista_trans[base] == '010':
                    Resultado += '2'
                elif lista_trans[base] == '011':
                    Resultado += '3'
                elif lista_trans[base] == '100':
                    Resultado += '4'
                elif lista_trans[base] == '101':
                    Resultado += '5'
                elif lista_trans[base] == '110':
                    Resultado += '6'
                elif lista_trans[base] == '111':
                    Resultado += '7'
        print(f'O valor octal é: {Resultado}')
    
    if escolhas == 6:
        lista_trans = list()
        Resultado = str()
        numero = (input('Digite o código binário: '))
        numero_modif = '0'
        quantia = len(numero)
        acrecimo = quantia % 4
        
        if acrecimo == 1:
            numero_modif = '000' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        elif acrecimo == 2:
            numero_modif = '00' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        elif acrecimo == 3:
            numero_modif = '0' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        elif acrecimo == 0:
            numero_modif = numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        valorr = len(lista_trans)
        for base in range(0, valorr):
            if base == 0:
                if lista_trans[base] == '0000':
                    Resultado = '0'
                elif lista_trans[base] == '0001':
                    Resultado = '1'
                elif lista_trans[base] == '0010':
                    Resultado = '2'
                elif lista_trans[base] == '0011':
                    Resultado = '3'
                elif lista_trans[base] == '0100':
                    Resultado = '4'
                elif lista_trans[base] == '0101':
                    Resultado = '5'
                elif lista_trans[base] == '0110':
                    Resultado = '6'
                elif lista_trans[base] == '0111':
                    Resultado = '7'
                elif lista_trans[base] == '1000':
                    Resultado = '8'
                elif lista_trans[base] == '1001':
                    Resultado = '9'
                elif lista_trans[base] == '1010':
                    Resultado = 'A'
                elif lista_trans[base] == '1011':
                    Resultado = 'B'
                elif lista_trans[base] == '1100':
                    Resultado = 'C'
                elif lista_trans[base] == '1101':
                    Resultado = 'D'
                elif lista_trans[base] == '1110':
                    Resultado = 'D'
                elif lista_trans[base] == '1111':
                    Resultado = 'E'
            else:
                if lista_trans[base] == '0000':
                    Resultado += '0'
                elif lista_trans[base] == '0001':
                    Resultado += '1'
                elif lista_trans[base] == '0010':
                    Resultado += '2'
                elif lista_trans[base] == '0011':
                    Resultado += '3'
                elif lista_trans[base] == '0100':
                    Resultado += '4'
                elif lista_trans[base] == '0101':
                    Resultado += '5'
                elif lista_trans[base] == '0110':
                    Resultado += '6'
                elif lista_trans[base] == '0111':
                    Resultado += '7'
                elif lista_trans[base] == '1000':
                    Resultado += '8'
                elif lista_trans[base] == '1001':
                    Resultado += '9'
                elif lista_trans[base] == '1010':
                    Resultado += 'A'
                elif lista_trans[base] == '1011':
                    Resultado += 'B'
                elif lista_trans[base] == '1100':
                    Resultado += 'C'
                elif lista_trans[base] == '1101':
                    Resultado += 'D'
                elif lista_trans[base] == '1110':
                    Resultado += 'D'
                elif lista_trans[base] == '1111':
                    Resultado += 'E'
        print(f'O valor hexadecimal é: {Resultado}')


def conversões_octais(escolhas):
    if escolhas == 7:
        octnum = int(input('Digite o numero octal: '))

        chk = 0
        i = 0
        valor = 0
        while octnum!=0:
            rem = octnum%10
            if rem>7:
                chk = 1
                break
            valor = valor + (rem * (8 ** i))
            i = i+1
            octnum = int(octnum/10)

        if chk == 0:
            print(F'O valor decimal é: {valor}')
        else:
            print("\nNumero invalido!")
    
    if escolhas == 8:
        lista_trans = list()
        valor = str()
        numero = str(input('Digite o código octal: '))
        quantia = len(numero)
        for trans in range(0, quantia):
            lista_trans.append(numero[trans])
        valor = len(lista_trans)
        for base in range(0, valor):
            if base == 0:
                if lista_trans[base] == '0':
                    valor = '0'
                elif lista_trans[base] == '1':
                    valor = '1'
                elif lista_trans[base] == '2':
                    valor = '10'
            else:
                if lista_trans[base] == '0':
                    valor += '000'
                elif lista_trans[base] == '1':
                    valor += '001'
                elif lista_trans[base] == '2':
                    valor += '010'
                elif lista_trans[base] == '3':
                    valor += '011'
                elif lista_trans[base] == '4':
                    valor += '100'
                elif lista_trans[base] == '5':
                    valor += '101'
                elif lista_trans[base] == '6':
                    valor += '110'
                elif lista_trans[base] == '7':
                    valor += '111'
        print(f'O valor binário é: {valor}')
    
    if escolhas == 9:
        lista_trans = list()
        valor = str()
        numero = str(input('Digite o código octal: '))
        quantia = len(numero)
        for trans in range(0, quantia):
            lista_trans.append(numero[trans])
        valor = len(lista_trans)
        for base in range(0, valor):
            if base == 0:
                if lista_trans[base] == '0':
                    valor = '0'
                elif lista_trans[base] == '1':
                    valor = '1'
                elif lista_trans[base] == '2':
                    valor = '10'
            else:
                if lista_trans[base] == '0':
                    valor += '000'
                elif lista_trans[base] == '1':
                    valor += '001'
                elif lista_trans[base] == '2':
                    valor += '010'
                elif lista_trans[base] == '3':
                    valor += '011'
                elif lista_trans[base] == '4':
                    valor += '100'
                elif lista_trans[base] == '5':
                    valor += '101'
                elif lista_trans[base] == '6':
                    valor += '110'
                elif lista_trans[base] == '7':
                    valor += '111'
        lista_trans_2 = list()
        Resultado = str()
        numero = valor
        numero_modif = '0'
        quantia = len(numero)
        acrecimo = quantia % 4
        
        if acrecimo == 1:
            numero_modif = '000' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans_2.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        elif acrecimo == 2:
            numero_modif = '00' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans_2.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        elif acrecimo == 3:
            numero_modif = '0' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans_2.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        elif acrecimo == 0:
            numero_modif = numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 4
            N1 = 0
            N2 = 4
            for trans in range(0, valor_quant):
                lista_trans_2.append(numero_modif[N1:N2])
                N1 += 4
                N2 += 4
        
        valor = len(lista_trans_2)
        for base in range(0, valor):
            if base == 0:
                if lista_trans_2[base] == '0000':
                    Resultado = '0'
                elif lista_trans_2[base] == '0001':
                    Resultado = '1'
                elif lista_trans_2[base] == '0010':
                    Resultado = '2'
                elif lista_trans_2[base] == '0011':
                    Resultado = '3'
                elif lista_trans_2[base] == '0100':
                    Resultado = '4'
                elif lista_trans_2[base] == '0101':
                    Resultado = '5'
                elif lista_trans_2[base] == '0110':
                    Resultado = '6'
                elif lista_trans_2[base] == '0111':
                    Resultado = '7'
                elif lista_trans_2[base] == '1000':
                    Resultado = '8'
                elif lista_trans_2[base] == '1001':
                    Resultado = '9'
                elif lista_trans_2[base] == '1010':
                    Resultado = 'A'
                elif lista_trans_2[base] == '1011':
                    Resultado = 'B'
                elif lista_trans_2[base] == '1100':
                    Resultado = 'C'
                elif lista_trans_2[base] == '1101':
                    Resultado = 'D'
                elif lista_trans_2[base] == '1110':
                    Resultado = 'D'
                elif lista_trans_2[base] == '1111':
                    Resultado = 'E'
            else:
                if lista_trans_2[base] == '0000':
                    Resultado += '0'
                elif lista_trans_2[base] == '0001':
                    Resultado += '1'
                elif lista_trans_2[base] == '0010':
                    Resultado += '2'
                elif lista_trans_2[base] == '0011':
                    Resultado += '3'
                elif lista_trans_2[base] == '0100':
                    Resultado += '4'
                elif lista_trans_2[base] == '0101':
                    Resultado += '5'
                elif lista_trans_2[base] == '0110':
                    Resultado += '6'
                elif lista_trans_2[base] == '0111':
                    Resultado += '7'
                elif lista_trans_2[base] == '1000':
                    Resultado += '8'
                elif lista_trans_2[base] == '1001':
                    Resultado += '9'
                elif lista_trans_2[base] == '1010':
                    Resultado += 'A'
                elif lista_trans_2[base] == '1011':
                    Resultado += 'B'
                elif lista_trans_2[base] == '1100':
                    Resultado += 'C'
                elif lista_trans_2[base] == '1101':
                    Resultado += 'D'
                elif lista_trans_2[base] == '1110':
                    Resultado += 'E'
                elif lista_trans_2[base] == '1111':
                    Resultado += 'F'
        print(f'O valor hexadecimal é: {Resultado}')


def conversões_hexadecimais(escolhas):
    
    if escolhas == 10:
        conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        hexadecimal = input("Digite o valor Hexadecimal: ").strip().upper()
        decimal = 0
        power = len(hexadecimal) -1

        for digit in hexadecimal:
            decimal += conversion_table[digit]*16**power
            power -= 1
        print(F'O valor decimal é: {decimal}')
    
    if escolhas == 11:
        lista_trans = list()
        codigo_hexa = input('Digite o código hexadecimal: ')
        quantia = len(codigo_hexa)
        for trans in range(0, quantia):
            lista_trans.append(codigo_hexa[trans])
        for base in range(0, quantia):
            if base == 0:
                if lista_trans[base] == '0':
                    Resultado = '0000'
                elif lista_trans[base] == '1':
                    Resultado = '1'
                elif lista_trans[base] == '2':
                    Resultado = '10'
                elif lista_trans[base] == '3':
                    Resultado = '11'
                elif lista_trans[base] == '4':
                    Resultado = '100'
                elif lista_trans[base] == '5':
                    Resultado = '101'
                elif lista_trans[base] == '6':
                    Resultado = '110'
                elif lista_trans[base] == '7':
                    Resultado = '111'
                elif lista_trans[base] == '8':
                    Resultado = '1000'
                elif lista_trans[base] == '9':
                    Resultado = '1001'
                elif lista_trans[base] == 'A':
                    Resultado = '1010'
                elif lista_trans[base] == 'B':
                    Resultado = '1011'
                elif lista_trans[base] == 'C':
                    Resultado = '1100'
                elif lista_trans[base] == 'D':
                    Resultado = '1101'
                elif lista_trans[base] == 'E':
                    Resultado = '1110'
                elif lista_trans[base] == 'E':
                    Resultado = '1111'
            else:
                if lista_trans[base] == '0':
                    Resultado += '0000'
                elif lista_trans[base] == '1':
                    Resultado += '0001'
                elif lista_trans[base] == '2':
                    Resultado += '0010'
                elif lista_trans[base] == '3':
                    Resultado += '0011'
                elif lista_trans[base] == '4':
                    Resultado += '0100'
                elif lista_trans[base] == '5':
                    Resultado += '0101'
                elif lista_trans[base] == '6':
                    Resultado += '0110'
                elif lista_trans[base] == '7':
                    Resultado += '0111'
                elif lista_trans[base] == '8':
                    Resultado += '1000'
                elif lista_trans[base] == '9':
                    Resultado += '1001'
                elif lista_trans[base] == 'A':
                    Resultado += '1010'
                elif lista_trans[base] == 'B':
                    Resultado += '1011'
                elif lista_trans[base] == 'C':
                    Resultado += '1100'
                elif lista_trans[base] == 'D':
                    Resultado += '1101'
                elif lista_trans[base] == 'E':
                    Resultado += '1110'
                elif lista_trans[base] == 'F':
                    Resultado += '1111'
        print(f'O valor binário é: {Resultado}')

    if escolhas == 12:
        lista_trans = list()
        codigo_hexa = input('Digite o código hexadecimal: ')
        quantia = len(codigo_hexa)
        Resultadoo = str()
        for trans in range(0, quantia):
            lista_trans.append(codigo_hexa[trans])
        for base in range(0, quantia):
            if base == 0:
                if lista_trans[base] == '0':
                    Resultadoo = '0000'
                elif lista_trans[base] == '1':
                    Resultadoo = '1'
                elif lista_trans[base] == '2':
                    Resultadoo = '10'
                elif lista_trans[base] == '3':
                    Resultadoo = '11'
                elif lista_trans[base] == '4':
                    Resultadoo = '100'
                elif lista_trans[base] == '5':
                    Resultadoo = '101'
                elif lista_trans[base] == '6':
                    Resultadoo = '110'
                elif lista_trans[base] == '7':
                    Resultadoo = '111'
                elif lista_trans[base] == '8':
                    Resultadoo = '1000'
                elif lista_trans[base] == '9':
                    Resultadoo = '1001'
                elif lista_trans[base] == 'A':
                    Resultadoo = '1010'
                elif lista_trans[base] == 'B':
                    Resultadoo = '1011'
                elif lista_trans[base] == 'C':
                    Resultadoo = '1100'
                elif lista_trans[base] == 'D':
                    Resultadoo = '1101'
                elif lista_trans[base] == 'E':
                    Resultadoo = '1110'
                elif lista_trans[base] == 'E':
                    Resultadoo = '1111'
            else:
                if lista_trans[base] == '0':
                    Resultadoo += '0000'
                elif lista_trans[base] == '1':
                    Resultadoo += '0001'
                elif lista_trans[base] == '2':
                    Resultadoo += '0010'
                elif lista_trans[base] == '3':
                    Resultadoo += '0011'
                elif lista_trans[base] == '4':
                    Resultadoo += '0100'
                elif lista_trans[base] == '5':
                    Resultadoo += '0101'
                elif lista_trans[base] == '6':
                    Resultadoo += '0110'
                elif lista_trans[base] == '7':
                    Resultadoo += '0111'
                elif lista_trans[base] == '8':
                    Resultadoo += '1000'
                elif lista_trans[base] == '9':
                    Resultadoo += '1001'
                elif lista_trans[base] == 'A':
                    Resultadoo += '1010'
                elif lista_trans[base] == 'B':
                    Resultadoo += '1011'
                elif lista_trans[base] == 'C':
                    Resultadoo += '1100'
                elif lista_trans[base] == 'D':
                    Resultadoo += '1101'
                elif lista_trans[base] == 'E':
                    Resultadoo += '1110'
                elif lista_trans[base] == 'F':
                    Resultadoo += '1111'
        lista_trans = list()
        Resultado = str()
        numero = Resultadoo
        numero_modif = '0'
        quantia = len(numero)
        acrecimo = quantia % 3
        
        if acrecimo == 1:
            numero_modif = '00' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 3
                N2 += 3
        
        elif acrecimo == 2:
            numero_modif = '0' + numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 3
                N2 += 3
        
        elif acrecimo == 0:
            numero_modif = numero
            quantia_modif = len(numero_modif)
            valor_quant = quantia_modif // 3
            N1 = 0
            N2 = 3
            for trans in range(0, valor_quant):
                lista_trans.append(numero_modif[N1:N2])
                N1 += 3
                N2 += 3
        valor = len(lista_trans)
        for base in range(0, valor):
            if base == 0:
                if lista_trans[base] == '000':
                    Resultado = '0'
                elif lista_trans[base] == '001':
                    Resultado = '1'
                elif lista_trans[base] == '010':
                    Resultado = '2'
                elif lista_trans[base] == '011':
                    Resultado = '3'
                elif lista_trans[base] == '100':
                    Resultado = '4'
                elif lista_trans[base] == '101':
                    Resultado = '5'
                elif lista_trans[base] == '110':
                    Resultado = '6'
                elif lista_trans[base] == '111':
                    Resultado = '7'
            else:
                if lista_trans[base] == '000':
                    Resultado += '0'
                elif lista_trans[base] == '001':
                    Resultado += '1'
                elif lista_trans[base] == '010':
                    Resultado += '2'
                elif lista_trans[base] == '011':
                    Resultado += '3'
                elif lista_trans[base] == '100':
                    Resultado += '4'
                elif lista_trans[base] == '101':
                    Resultado += '5'
                elif lista_trans[base] == '110':
                    Resultado += '6'
                elif lista_trans[base] == '111':
                    Resultado += '7'
        print(f'O valor octal é:{Resultado}')
                