import os
import r_html

# Удаляем выбранного абонента
def del_person(num):
    if os.path.isfile('t_book.tmp'):
        os.remove('t_book.tmp')
    with open('t_book.txt', 'r', encoding="utf-8") as fp:
        for n, line in enumerate(fp, 1):
            dic = dict(subString.split(":") for subString in line.replace('\n', '').split(", "))
            if int(dic['id']) != int(num):
                with open('t_book.tmp', 'a', encoding = 'UTF_8') as fp_tmp:
                    fp_tmp.write(line)
                fp_tmp.close()
    fp.close()

# Перезаписываем построчно тектовый файл в .tmp, потом заменяем им текстовый
    if os.path.isfile('t_book.txt'):
        os.remove('t_book.txt')
    else: print("File doesn't exists!")

    os.rename('t_book.tmp', 't_book.txt')
    r_html.save_html()
    print(" Сделано!\n")
    os.system("pause")