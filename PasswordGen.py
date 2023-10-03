
try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint



#MainFunc
def isEven(integer):

#---Определение функции isEven(integer), которая принимает целое число integer и возвращает True, если оно четное, и False, если нечетное
#---Эта функция будет использоваться для определения некоторых параметров генерации пароля

    return integer % 2 == 0

def RandPass(size = 8):

#---Определение функции RandPass(size=8) для генерации пароля
#---Функция принимает аргумент size, который по умолчанию равен 8


#----Определение трех наборов символов

    s0 = "!@#$%^&*- _~+-=" #---Специальные символы
    s1 = ascii_letters #---Буквы верхнего и нижнего регистра (латиница) 
    s3 = digits #---Цифры от 0 до 9
    
#---Генерация частей пароля

    s = s0 + s1  
    s_full = s + s3 
    passlen = size.get() #длина пароля
    new_password = ""

    
    if isEven(passlen) == True:
        front = passlen // 5
    else:
        front = passlen // 2
    mid = 2
    previous = passlen - (front + mid) - 1

    pass0 = "".join(choice(s0)) #---Выбор одного случайного символа из s0. Этот символ будет использоваться в начале пароля
    pass1 = "".join(sample(s_full,front )) #---Выбор случайных символов из s_full для части front пароля
    pass2 = "".join(sample(s3,mid)) #---Выбор случайных цифр из s3 для части mid пароля
    pass3 = "".join(sample(s, previous )) #---Выбор случайных символов из s для части previous пароля
    
    if passlen != len(pass0 + pass1 + pass2 + pass3):
        pass2 = "".join(sample(s3,passlen - (front+previous+1) ))

    if pass3[:-1] == ' ':
        temp = list(pass3)
        temp[:-1] = choice(s)
        pass3 = ''.join(str(e) for e in temp)
    new_password = pass0 + pass1 + pass2 + pass3   #Сборка всех частей пароля в строку
    

    #---Определение переменных msg и colorVal в зависимости от длины пароля
    #---Данные переменные будут использоваться для отображения силы пароля в интерфейсе

    if passlen <= 8:
        msg = 'VERY WEAK'
        colorVal = "#6d0001"
    elif passlen <=10:
        msg = 'WEAK'
        colorVal = "#cc0000"
    elif passlen <=12:
        msg = 'DECENT'
        colorVal = "#fc8600"
    elif passlen <=14:
        msg = 'GOOD'
        colorVal = "#eae200"
    elif passlen <=16:
        msg = 'STRONG'
        colorVal = "#9ff400"
    elif passlen <=18:
        msg = 'VERY STRONG'
        colorVal = "#007715"
    elif passlen >18:
        msg = 'EXCELLENT'
        colorVal = "#001fef"
    else:
        pass

    return new_password, msg, colorVal

#---Возврат сгенерированного пароля new_password, сообщения о его силе msg и цвета colorVal
