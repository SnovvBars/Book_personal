import os

# формируем шапку таблицы
def save_html():    
    str_html = '<html><body><table border = 1><tr><td>ID</td><td>ФИО</td><td>Должность</td><td>Отдел</td><td>Оклад</td><td>Телефон</td><td>Статус номера</td><td>Возраст</td><td>Пол</td><td>Соцстатус</td><td>Принят</td></tr><tr>'
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            str_html = str_html + form_line(dic)
    str_html = str_html + '</tr></table></body></html>'
    save_file_html(str_html)

# формируем строки таблицы
def form_line(line):
    str = '<tr>'
    for key in line:
        str = str + '<td>' + line[key] + '</td>'
    return str + '</tr>'

# перезаписываем htnl файл на основе файла t_book.txt
def save_file_html(html_str):
    if os.path.isfile('t_book.html'):
        os.remove('t_book.html')
    f = open("t_book.html", 'w', encoding = 'utf-8')
    f.write(html_str)
    f.close()