import UI
import r_txt
import remove
import print_data
import search

def button_click():
    item = UI.main_menu()
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    elif item == 2:
        item = UI.find_str_del()
        if item: remove.del_person(item)
    elif item == 3:
        item = UI.show_filds()
        print_data.print_select(item)
    elif item == 4:
        item = search.data_search()    
    elif item == 5:
        item = remove.del_all()      
    if item == 6:
        print("\n Good bye!!!\n")
        exit()