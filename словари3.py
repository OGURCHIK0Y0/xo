users={}
command= input('че хотите ')
while command!="выход":
    if command =='регистрация':
        login = input("Введите логин ")
        password1 = input("Введите пороль ")
        password2=input("Введите пороль повторно ")
        if password1 == password2:
            print("вы зарегистрировались! ")
            users[login]=password1
        else:
            print('регистрация не удалась ')
            passwor2=input('повторите попытку ')
    elif command == 'авторизация':
        login = input('Введите логин ')
        password = input('Введите ппороль ')
        if login in users.keys():
            if password == users[login]:
                print('вы авторизовались! ')
            else:
                print("password не верный ")
        else:
            print('пользователь не найден ')
    command = input('че хотие ')
