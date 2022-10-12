# Task: Create a program which deletes from a text all words containing 'abc'


with open('hw05_tsk01_inpt.txt', 'r') as input:
    text = input.readline()
    word = input.readline()
    print(f'Input text is: {text} Word to search is: {word}')

text = text.split()

text = list(filter(lambda x: word not in x, text))
print(f'Result text is: {text}')

with open('hw05_tsk01_otpt.txt', 'w') as output:
    for i in text:
        output.write(i + ' ')
