from Modules import modules

while True:
    modules.menu_initial()
    choose = int(input('= '))
    
    if choose == 1 or 2 or 3:
        modules.basic_conversions(choices=choose)

    if choose == 4 or 5 or 6 :
        modules.conversions_binarias(choices=choose)

    if choose == 7 or 8 or 9 :
        modules.octal_conversions(choices=choose)

    if choose == 10 or 11 or 12:
        modules.hexadecimal_conversions(choices=choose)
    
    if input('Would you like to continue: ').upper().strip()[0] != 'S':
        break
    