import UI
import r_txt

def button_click():
    item = UI.main_menu()
    # print(type(item))
    if item == 1:
        item = UI.data_input()
        r_txt.write_txt(item)
    # elif item == 2:
    #     UI.unique_id()
    # elif item == 3:
    #     item = data_print.data_all()
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