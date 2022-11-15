
# Check correctness of the first symbol entry:
# The first symbol of operation is either '-' or a digit
def entry_check1():
    is_OK = False
    while not is_OK:
        try:
            entry = input('Enter: ')
            if entry.isdigit() or entry == '-':
                is_OK = True
            else:
                print('Only digit or "-" sign are accepted at this point.')
        except:
            print('How did you manage to get here?')
    return entry


# Check correctness of the second symbol entry:
# IF the first symbol was '-', ONLY a digit can the the second,
# ELSE either 1) a digit or 2) '.' or 3) any of simple math operators (+, -, *, /)
# can the second
def entry_check2(entry1, math_signs):
    is_OK = False

    while not is_OK:
        if entry1 == '-':
            try:
                entry2 = input('Enter: ')
                if entry2.isdigit():
                    is_OK = True
                else:
                    print('Only digit entry is accepted at this point.')
            except:
                print('How did you manage to get here?')
        else:
            try:
                entry2 = input('Enter: ')
                if entry2.isdigit() or entry2 == '.' or entry2 in math_signs:
                    is_OK = True
                else:
                    print(
                        'Only digit, "." or math operators are accepted at this point.')
            except:
                print('How did you manage to get here?')
    return entry1 + entry2


# Check correctness of the third and subsequent entries until a math operator:
# IF the previous symbol was '.', ONLY a digit can be the next;
# IF the previous symbol was not '.', but '.' was earlier, 1) a digit or 2) a math
# operator can be the next;
# IF '.' was not entered previously, 1) a digit or 2) '.' or 3) a math operator
# can be the next;
def entry_check_subs_1(previous, math_signs):
    is_OK = False
    while not is_OK:
        if previous[-1] == '.':
            try:
                entry = input('Enter: ')
                if entry.isdigit():
                    is_OK = True
                else:
                    print('Only digit entry is accepted at this point.')
            except:
                print('How did you manage to get here?')
        elif '.' in previous and previous[-1] != '.':
            try:
                entry = input('Enter: ')
                if entry.isdigit() or entry in math_signs:
                    is_OK = True
                else:
                    print('Only digit or math operators are accepted at this point.')
            except:
                print('How did you manage to get here?')
        else:
            try:
                entry = input('Enter: ')
                if entry.isdigit() or entry == '.' or entry in math_signs:
                    is_OK = True
                else:
                    print(
                        'Only digit, "." or math operators are accepted at this point.')
            except:
                print('How did you manage to get here?')
    return entry


# Check correctness of the third and subsequent entries until a '=' sign':
# Same logic as in the method above, except '=' is the stop trigger.
def entry_check_subs_2(previous, math_signs):
    is_OK = False
    while not is_OK:
        if previous[-1] == '.':
            try:
                entry = input('Enter: ')
                if entry.isdigit():
                    is_OK = True
                else:
                    print('Only digit entry is accepted at this point.')
            except:
                print('How did you manage to get here?')
        elif '.' in previous and previous[-1] != '.':
            try:
                entry = input('Enter: ')
                if entry.isdigit() or entry in math_signs:
                    is_OK = True
                else:
                    print('Only digit or "=" sign are accepted at this point.')
            except:
                print('How did you manage to get here?')
        else:
            try:
                entry = input('Enter: ')
                if entry.isdigit() or entry == '.' or entry in math_signs:
                    is_OK = True
                else:
                    print('Only digit, "." or "=" sign are accepted at this point.')
            except:
                print('How did you manage to get here?')
    return entry


# Handling the entry of the first number and math operator
def number1_and_operator():
    global operators
    entry1 = entry_check1()
    entry2 = entry_check2(entry1, operators)
    while entry2[-1] not in operators:
        entry2 += entry_check_subs_1(entry2, operators)

    if '.' in entry2:
        operand1 = float(entry2[:-1])
    else:
        operand1 = int(entry2[:-1])
    operator = entry2[-1]
    # print(operand1)
    # print(operator)
    return (operand1, operator)


# Handling the entry of the second number until equal sign
def number2():
    global equal
    entry1 = entry_check1()
    entry2 = entry_check2(entry1, equal)
    while entry2[-1] not in equal:
        entry2 += entry_check_subs_2(entry2, equal)

    if '.' in entry2:
        operand2 = float(entry2[:-1])
    else:
        operand2 = int(entry2[:-1])
    # operator = entry2[-1]
    # print(operand2)
    # print(operator)
    return (operand2)

# Performing the actual math operation and giving the result


def operation(operand1, operator, operand2):
    if operator == '+':
        result = operand1 + operand2
    if operator == '-':
        result = operand1 - operand2
    if operator == '*':
        result = operand1 * operand2
    if operator == '/':
        result = operand1 / operand2
    print(f'{operand1} {operator} {operand2} = {result}')
    return result


operators = '+-*/'
equal = '='

operand1, operator = number1_and_operator()
operand2 = number2()
print(operand1)
print(operator)
print(operand2)
operation(operand1, operator, operand2)
