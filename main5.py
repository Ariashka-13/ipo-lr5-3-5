s=str(input("Введите строку ")) #ввод строки 
gl='аоуыэиеёюя' #в переменную указываем гласные
gl_count=0 #счетчик количества гласных
for b in s: #использование цикла
    if b in gl: #если есть гласные в строке
        gl_count +=1 #работа счетчика количества гласных   
print("Количество гласных: ", gl_count) #вывод количества гласных