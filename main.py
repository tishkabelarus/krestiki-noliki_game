print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nприветсвую вас в игре "крестики нолики"!!!')
start = input("вы готовы? y/n    ")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
if start == "y":

    win_x = False
    win_0 = False
    game_status = True #основные параметры
    step_number = 0 
    symbol = ""

    row_number_1= ["- ","- ","- "] 
    row_number_2= ["- ","- ","- "] #само поле игры
    row_number_3= ["- ","- ","- "]
        
    while game_status == True:
        step_number += 1
        print(f"\n\n ход:{step_number}")
        if step_number%2==1:
            symbol = "0 "   #визуал
        else:
            symbol = 'X '
        if step_number !=10:
            print(f"\n\nваше поле:\n\n  1 2 3 \na {row_number_1[0]}{row_number_1[1]}{row_number_1[2]}\nb {row_number_2[0]}{row_number_2[1]}{row_number_2[2]}\nc {row_number_3[0]}{row_number_3[1]}{row_number_3[2]}\n\nвведите координаты где будет стоять '{symbol}'(сначала ряд:(a,b,c),потом столбец:(1,2,3)):\n\n")
        else:
            print(f"\n\nваше поле:\n\n  1 2 3 \na {row_number_1[0]}{row_number_1[1]}{row_number_1[2]}\nb {row_number_2[0]}{row_number_2[1]}{row_number_2[2]}\nc {row_number_3[0]}{row_number_3[1]}{row_number_3[2]}\n\nничья, до свидания!")
            input('\n\nнажмите enter чтобы выйти')
            break  



        row = input("ряд:   ")

        if row != "a" and row != "b" and row != "c":
            print('нет такого ряда')
            step_number -=1
            continue

        column = input("столбец:   ")
        
        if int(column) >= 4:
            print('\nнет такого столбца!!!')
            step_number -=1
            continue
        if row == "a":    
            if "-" not in row_number_1[int(column)-1]:
                print("\nэто место занято")
                step_number -=1
            else:
                row_number_1[int(column)-1]=symbol       
        elif row == "b":
            if "-" not in row_number_2[int(column)-1 ]:
                print("\nэто место занято")
                step_number -=1                                          #здесь пользователь ставит символ на поле если место не занято
            else:
                row_number_2[int(column)-1]=symbol
        elif row == "c":
            if "-" not in row_number_3[int(column)-1]:
                print("\nэто место занято")
                step_number -=1
            else:
                row_number_3[int(column)-1]=symbol
        game_status = True

 

        #ПО ГОРИЗОНТАЛИ
        if row_number_1[0] == "X " and row_number_1[1] == "X " and row_number_1[2] == "X ":
            win_x = True
        if row_number_1[0] == "0 " and row_number_1[1] == "0 " and row_number_1[2] == "0 ":
            win_0 = True

        if row_number_2[0] == "X " and row_number_2[1] == "X " and row_number_2[2] == "X ":
            win_x = True                                                                         #это все проверка выигрыша, решил сделать все без функций т.к. в такой простой игре они не пригодятся
        if row_number_2[0] == "0 " and row_number_2[1] == "0 " and row_number_2[2] == "0 ":
            win_0 = True

        if row_number_3[0] == "X " and row_number_3[1] == "X " and row_number_3[2] == "X ":
            win_x = True
        if row_number_3[0] == "0 " and row_number_3[1] == "0 " and row_number_3[2] == "0 ":
            win_0 = True

        #ПО ВЕРТИКАЛИ
        if row_number_1[0] == "X " and row_number_2[0] == "X " and row_number_3[0] == "X ":
            win_x = True
        if row_number_1[0] == "0 " and row_number_2[0] == "0 " and row_number_3[0] == "0 ":
            win_0 = True

        if row_number_1[1] == "X " and row_number_2[1] == "X " and row_number_3[1] == "X ":
            win_x = True
        if row_number_1[1] == "0 " and row_number_2[1] == "0 " and row_number_3[1] == "0 ":
            win_0 = True

        if row_number_1[2] == "X " and row_number_2[2] == "X " and row_number_3[2] == "X ":
            win_x = True
        if row_number_1[2] == "0 " and row_number_2[2] == "0 " and row_number_3[2] == "0 ":
            win_0 = True
        
        #НАИСКОСОК В НИЖНИЙ ПРАВЫЙ УГОЛ
        if row_number_1[0] == "X " and row_number_2[1] == "X " and row_number_3[2] == "X ":
            win_x = True
        if row_number_1[0] == "0 " and row_number_2[1] == "0 " and row_number_3[2] == "0 ":
            win_0 = True

        #НАИСКОСОК В НИЖНИЙ ЛЕВЫЙ УГОЛ
        if row_number_1[2] == "X " and row_number_2[1] == "X " and row_number_3[0] == "X ":
            win_x = True
        if row_number_1[2] == "0 " and row_number_2[1] == "0 " and row_number_3[0] == "0 ":
            win_0= True


        if win_x == True:
            print(f"\n\nваше поле:\n\n  1 2 3 \na {row_number_1[0]}{row_number_1[1]}{row_number_1[2]}\nb {row_number_2[0]}{row_number_2[1]}{row_number_2[2]}\nc {row_number_3[0]}{row_number_3[1]}{row_number_3[2]}\n\nпобеда Х!!!         до свидания!\n\n\n")
            input('\n\nнажмите enter чтобы выйти')
            break
        if win_0 == True:
            print(f"\n\nваше поле:\n\n  1 2 3 \na {row_number_1[0]}{row_number_1[1]}{row_number_1[2]}\nb {row_number_2[0]}{row_number_2[1]}{row_number_2[2]}\nc {row_number_3[0]}{row_number_3[1]}{row_number_3[2]}\n\nпобеда 0!!!         до свидания!\n\n\n")
            input('\n\nнажмите enter чтобы выйти')
            break
            

elif start == "n":
    print("тогда увидимся позже")
    input('\n\nнажмите enter чтобы выйти')                                       #если пользователь не хочет играть или ошибся
else:
    print("error alert: вы должны ввести либо 'y'- да, либо 'n'- нет")
    input('\n\nнажмите enter чтобы выйти')