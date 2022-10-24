from os import system

def check_taken(text_invitation, error, min, max):             # Проверка ввода
    while True:
        input_data = input(text_invitation)
        if not input_data.isnumeric():
            print("\nВы ввели не число. Попробуйте снова: ")
            system("pause")
        elif not min <= int(input_data) <= max:
            print(error)
            system("pause")
        else:
            return input_data