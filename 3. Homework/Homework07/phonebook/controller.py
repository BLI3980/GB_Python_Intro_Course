import c_user_interface as ui
import a_data_read as data
import format1 as format


def controller():
    ui.view('phonebook.csv')
    ui.show_menu()


controller()
