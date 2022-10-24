from os import system 

# Выводим все поля и все записи из текстового файла
def print_select(filds):    
# Словарь соответствия полей цифрам, введенным пользователем нужно для поика соответствующих ключей в записи
    dic_filds = { '1' : 'job_title', '2' : 'department', '3' : 'salary', 
                  '4' : 'telephone', '5' : 'own', '6' : 'age', 
                  '7' : 'gender', '8' : 'status', '9' : 'data_appointment' }
# То же на русском, нужно для вывода заголовков полей
    dic_filds_ru = { '1' : 'Должность', '2' : 'Отдел', '3' : 'Оклад', 
                     '4' : 'Телефон', '5' : 'Статус телефона', '6' : 'Возраст', 
                     '7' : 'Пол', '8' : 'Соцстатус', '9' : 'Дата приема' }
    count = 0
    print('\n')
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            final_str = ''
# Считываем строку из файла txt
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
# Если есть записи, запускаем счетчик строк
            if dic : count += 1
# Формируем строку по сотруднику для вывода
            final_str += str(count) + '. ФИО: ' + dic['famaly'] + ', '
# Для списка полей, переданных пользователем
            for item in filds:
# Находим поля заданные пользователем, соответствующие ключам в записи данных сотрудника
                if dic_filds[item] in dic.keys():
# Формируем чтроку для вывода из полейЮ заданных пользователем
                    final_str += dic_filds_ru[item] + ':' + dic[dic_filds[item]] + ', '
            print(final_str.strip(', '))
# Если файл пуст, то
    if count == 0: print(" Никого нет!")
    print ('')
    system("pause")