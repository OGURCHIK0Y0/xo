v=input('введите команду ')
pers = {"имя":"Ваня","возраст":13,"качества":"добрый"}
while v != "выход":
    if v == 'добавить':
        a = input('что добавить? ')
        b = input('введите значение: ')
        pers[a] = b
    elif v == 'показать':
        print(pers)
    if v== 'особенности':
        s=input("какая особенность? ")
        print(pers[s])
    if v== 'измена будущего':
        g=input('что хочешь изменить? ')
        print('старое значение',pers[g])
        pers[g]=input('введи новое значение ')
    v=input('введите команду ')
