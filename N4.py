def inputNum():
    is_ok = False
    while not is_ok:
        try:
            a = int(input("Введите номер четверти: "))
            if 0 < a < 5:
                is_ok = True
            else:
                print("Такой координатной четверти нет. Попробуй ещё раз.")
                is_ok = False
        except ValueError:
            print("Ты ошибся. Вводить надо целые числа!")
    return a

def checkNum(x):
    if x == 1:
        print("x>0 и y>0")
    elif x == 2:
        print("x<0 и y>0")
    elif x == 3:
        print("x<0 и y<0")
    elif x == 4:
        print("x>0 и y<0")

num = inputNum()
checkNum(num)
