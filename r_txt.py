import r_html
from os import system

# Записываем переданную строку в файл txt, на его основе генерим html
def write_txt(dic):
    with open('t_book.txt', 'a', encoding = 'UTF_8') as file:
        file.write('{}\n'
            .format(', '.join('{}: {}'.format(key, val) for key, val in dic.items())))
    file.close()
    r_html.save_html()
    print("\n Сделано\n")
    system("pause")
