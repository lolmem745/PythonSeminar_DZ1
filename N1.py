num = int(input())
if num < 6 and num > 0:
    print("Будни")
elif num < 8 and num > 5:
    print("Выходной")
else:
    print("Введите число в диапазоне недели")
