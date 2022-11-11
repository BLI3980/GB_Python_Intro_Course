def view_data(title, data):
    print(f'\n{title} = {data}')


def get_operation():
    print('\nChoose which operation you want to perform:\n'
          '1. Subtract\n'
          '2. Sum\n'
          '3. Multiply\n'
          '4. Find a square root\n'
          '5. End the work\n')
    is_OK = False
    while not is_OK:
        try:
            choice = int(input('Enter the number of your choice: '))
            is_OK = True
            if choice not in range(1, 6):
                is_OK = False
                print('Please enter a number corresponding to operation.')
        except ValueError:
            print('This is not a number. Try again.')
    return choice


def ask_if_continue():
    print('\nDo you want to continue with another operation?')
    is_OK = False
    while not is_OK:
        # try:
        next = str(input('Choose Y/N: '))
        is_OK = True
        if next not in 'ynYN':
            is_OK = False
            print('Please enter letter "Y" or "N"')
        # except ValueError:
        #     print('This is not a letter. Please try again.')
    return next.lower()


def get_value():
    return float(input('value = '))
