import r_html

# Заменяем цифры нв значения, записываем в файл txt, на его основе генерим html
def write_txt(dic):
    # for key, value in dic.items():
    #     if key == 'own' : dic[key] = finding_own(value)
    #     elif key == 'gender' : dic[key] = finding_gender(value)
    #     elif key == 'status' : dic[key] = finding_status(value)
    with open('t_book.txt', 'a', encoding = 'UTF_8') as file:
        file.write('{}\n'
            .format(', '.join('{}: {}'.format(key, val) for key, val in dic.items())))
    file.close()
    r_html.save_html()