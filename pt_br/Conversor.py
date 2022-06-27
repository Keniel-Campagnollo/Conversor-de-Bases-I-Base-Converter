from Módulos import módulos

while True:
    módulos.menu_inicial()
    escolha = int(input('= '))
    
    if escolha == 1 or 2 or 3:
        módulos.conversões_básicas(escolhas=escolha)

    if escolha == 4 or 5 or 6 :
        módulos.conversões_binaria(escolhas=escolha)

    if escolha == 7 or 8 or 9 :
        módulos.conversões_octais(escolhas=escolha)

    if escolha == 10 or 11 or 12:
        módulos.conversões_hexadecimais(escolhas=escolha)
    
    if input('Deseja continuar: ').upper().strip()[0] != 'S':
        break
    