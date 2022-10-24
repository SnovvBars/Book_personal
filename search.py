import os

# Просто поиск, если в ключе famaly есть совпадение, выводим результат
def data_search():
    elem = str(input('\n Введите часть фамилии или фамилию целиком: '))
    print ('')
    if elem == '' : print(" Не найдено!")
    else:
        with open('t_book.txt', 'r', encoding="utf-8") as fp:
            count = 0
            for n, line in enumerate(fp, 1):
                dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
                if elem.lower() in dic['famaly'].lower():
                    count += 1
                    print(" {:>3}. ФИО:{:>18} | Должность:{:>10} | Отдел{} "
                        .format(count, dic['famaly'], dic['job_title'], dic['department']))            
            if count == 0 : print(" Не найдено!")
    print ('')
    os.system("pause")