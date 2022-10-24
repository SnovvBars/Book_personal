# Пункты меню главного и для ввода данных
from datetime import datetime as dt
import check_input

def main_menu():
    choice_main_menu = int(check_input.check_taken('''
   Выберите действие:
    
 1 Ввести данные по сотруднику         
 2 Редактировать данные
 3 Вывести данные по сотрудникам                   
 4 Найти данные                 
 5 Очистить БД               
 6 Выход

 Ваш выбор (1 - 6): ''', "\n Ошибка!\n", 1, 6))
    # print(choice_main_menu)
    # if choice_main_menu == 1: data_input()
    return choice_main_menu

def unique_id():
    # str_html = '<html><body><table border = 1><tr><td>ID</td><td>ФИО</td><td>Должность</td><td>Отдел</td><td>Оклад</td><td>Телефон</td><td>Статус номера</td><td>Возраст</td><td>Пол</td><td>Соцстатус</td><td>Принят</td></tr><tr>'
    with open('t_book.txt', 'a+', encoding="utf-8") as fp:
        max = 0
        list_id = []
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            # str_html = str_html + form_line(dic)
    # str_html = str_html + '</tr></table></body></html>'
            list_id.append(int(dic["id"]))
            if int(dic["id"]) > max: max = int(dic["id"])
            # print(dic["id"], max, list_id)
    fp.close()
    # print(list_id)
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

    