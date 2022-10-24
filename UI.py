# Пункты меню главного и для ввода данных
from datetime import datetime as dt
import check_input
from os import system

def main_menu():
    choice_main_menu = int(check_input.check_taken('''
   Выберите действие:
    
 1 Ввести нового сотрудника         
 2 Удалить (уволить) сотрудника
 3 Вывести данные по сотрудникам                   
 4 Найти данные                 
 5 Очистить БД               
 6 Выход

 Ваш выбор (1 - 6): ''', "\n Ошибка!\n", 1, 6))
    return choice_main_menu

# Поиск уникального ID. Перебираем значения ключей ID сотрудников, записываем в list_id
# находим максимальное значение, в цикле перебираем числа от 1 до max_id + 1, если 
# какое то значение пропущено, возвращаем его, если нет, возвращаем id + 1,
# например, если пропущено id = 3, возвращаем 3, если id непрерывны, то возвращаем
# id + 1
def unique_id():
    with open('t_book.txt', 'a+', encoding="utf-8") as fp:
        max = 0
        list_id = []
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            list_id.append(int(dic["id"]))
            if int(dic["id"]) > max: max = int(dic["id"])
    fp.close()
    for i in range(1, len(list_id) + 1):
        if i not in list_id:
            return(i)
            # break
    return (len(list_id) + 1)    

def data_input():
    print('\n Будем вводить данные сотрудника')
    d = {'id' : unique_id()}   
    d['famaly'] = input('\n Введите ФИО в формате \'Фамилия Имя Отчество\': ')
    d['job_title'] = input('\n Введите должность: ')
    d['department'] = input('\n Введите отдел: ')
    d['salary'] = input('\n Введите оклад: ')
    d['telephone'] = input('\n Введите телефон в формате \'+1(234)567-89-12\': ')
    str = '''
 Статус телефонного номера:
   1 - Личный
   2 - Рабочий
   3 - Домашний 
 (1 - 3): '''
    d['own'] = finding_own(int(check_input.check_taken(str, "\n Ошибка!\n", 1, 3)))
    d['age'] = input('\n Введите возраст: ')
    str = '''
 Выберите пол:
   1 - Мужской
   2 - Женский
 (1 - 2): '''
    d['gender'] = finding_gender(int(check_input.check_taken(str, "\n Ошибка!\n", 1, 2)))   
    str = '''
 Выберите соцстатус:
   1 - Женат\Замужем
   2 - Холост
   3 - В разводе
 (1 - 3): '''
    d['status'] = finding_status(int(check_input.check_taken(str, "\n Ошибка!\n", 1, 3)))
    d['data_appointment'] = input('\n Введите дату приема на работу: ')
    # print (d)
    return d

def finding_own(owns):
    if owns == 1: return 'Личный'
    elif owns == 2: return 'Рабочий'
    else: return 'Домашний'

def finding_gender(gender):
    if gender == 1: return 'м'
    elif gender == 2: return 'ж'
    
def finding_status(status):
    if status == 1: return 'Женат\\Замужем'
    elif status == 2: return 'Холост'
    else: return 'В разводе'

# Сначала ищем абонента по фамилии, показываем совпадения, предлагаем выбрать ID удаляемого
def find_str_del():
    elem = str(input('''
     Кого будем удалять?
     Введите часть фамилии или фамилию целиком: '''))
    print ('')
    count = 0
    if elem == '' : print(" Не найдено!")
    else:
        with open('t_book.txt', 'r', encoding="utf-8") as fp:
            for n, line in enumerate(fp, 1):
                dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
                if elem.lower() in dic['famaly'].lower():
                    count += 1
                    print("{}. | id: {}, | ФИО:{:>16} | Должность:{:>18} | Отдел.:{:>9}"
                        .format(count, dic['id'], dic['famaly'], dic['job_title'], dic['department'], dic['gender'], dic['status']))                                    
        fp.close()
        if count == 0 :
            print(" Не найдено!\n")
            system("pause")
            return False
        else:
            nun_del = input('\n Выберите id удаляемого: ')
            return nun_del

def show_filds():
    list_filds = input('''
 Выберите для дополнительного показа (перечислите через пробел):

 1. Должность
 2. Отдел
 3. Оклад
 4. Телефон
 5. Статус телефона
 6. Возраст
 7. Пол
 8. Соцстатус
 9. Дата приема   
 
 ''').split()
    return list_filds

    