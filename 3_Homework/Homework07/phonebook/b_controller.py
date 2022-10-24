import os
from time import sleep
import c_user_interface as ui

# Module coordinates modules and UI.

def controller():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = ui.show_menu()
    ui.choices(choice)
    if ui.if_continue() == 1:
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        controller()
    else:
        sleep(1)
        print('\n'+'='*15+' Have a good day! '+'='*15+'\n\n')
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')



