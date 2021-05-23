print("Если сумма чисел X, Y, Z меньше 10, то наименьшее из них заменить полусуммой двух других, иначе меньшее из X и Y заменить на наибольшее из X, Y, Z.")
X=input("X:")
Y=input("Y:")
Z=input("Z:")
SUMMA = int(X) + int(Y) + int(Z)
m = X
#global MAX
MAX = X
#Вычисляем максимум
if MAX < Y:
    MAX = Y
if MAX < Z:
    MAX = Z
print("Максимум",MAX)
if SUMMA < 10:
    #Считаем наименьшее
    print("Сумма меньше 10")
    if m > Y:
        m = Y
    if m > Z:
        m = Z
    #Высчитываем полусумму двух других
        PS = (int(X) + int(Y))/2       
    #Выводим минимальное
    print("Минимальное:",m)
    #Заменяем
    m = PS
    print("Заменено:",m)
else:
    print("Сумма больше 10")
    if X > Y:
        Y = MAX
        print("Замена(Y на MAX):",Y)
    else:
        X = MAX
    print("Замена(X на MAX):",X)    
    

    
