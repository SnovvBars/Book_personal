import UI
import r_txt
import remove

def button_click():
    item = UI.main_menu()
    # print(type(item))
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    elif item == 2:
        item = UI.find_str_del()
        if item: remove.del_person(item)
    elif item == 3:
        item = UI.show_filds()
        print(item)
    # elif item == 4:
    #     item = search.data_search()    
    # elif item == 5:
    #     item = rem.data_delete()    
    # elif item == 6:
    #     item = rem.del_all()    
    if item == 6:
        # print(item)
        print("\n Good bye!!!\n")
        exit()