MAIN - запускает программу через вызов метода модуля CONTROLLER
файл main.ru

CONTROLLER - обеспечивает взаимодействие модулей:
1. через UI взаимодействует с пользователем
2. ищет сотрудника через модуль SEARCH
3. удаляет сотрудника через DEL_DATA
4. выводит данные на терминал через PRINT_DATA
файл controller.py

Пункты главного меню (UI):
1. Ввести нового сотрудника         
2. Удалить (уволить) сотрудника
3. Вывести данные по сотрудникам                   
4. Найти данные                 
5. Очистить БД               
6. Выход

Поля данных о сотруднике:
1. ID
2. Должность
3. Отдел
4. Оклад
5. Телефон
6. Статус телефона
7. Возраст
8. Пол
9. Соцстатус
10. Дата приема

Программа сохраняет данные в формате txt и html
в файлах t_book.txt и t_book.html

Реализованы поиск по фамилии, вывод инфо о сотруднике по выбранным полям