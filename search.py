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
    # dic_filds = { '1' : 'job_title', '2' : 'department', '3' : 'salary', 
    #               '4' : 'telephone', '5' : 'own', '6' : 'age', 
    #               '7' : 'gender', '8' : 'status', '9' : 'data_appointment' }
    # dic_filds_ru = { '1' : 'Должность', '2' : 'Отдел', '3' : 'Оклад', 
    #                  '4' : 'Телефон', '5' : 'Статус телефона', '6' : 'Возраст', 
    #                  '7' : 'Пол', '8' : 'Соцстатус', '9' : 'Дата приема' }
                    print(" {:>3}. ФИО:{:>18} | Должность:{:>10} | Отдел{} "
                        .format(count, dic['famaly'], dic['job_title'], dic['department']))            
            if count == 0 : print(" Не найдено!")
    print ('')
    os.system("pause")