# Task: Create a program with RLE algorithm.
# Input and output data in different files

with open('RLE_inpt.txt', 'r') as data:
    input = data.readline()
print(input)

count = 1
encode = ''
for i in range(1, len(input)):
    if i != len(input)-1:
        if input[i] == input[i-1]:
            count += 1
        else:
            encode = encode + str(count) + input[i-1]
            count = 1
    else:
        if input[i] == input[i-1]:
            count += 1
            encode = encode + str(count) + input[i]
        else:
            encode = encode + str(count) + input[i-1]
            count = 1
            encode = encode + str(count) + input[i]

with open('RLE_otpt.txt', 'a') as data:
    data.write(f'{encode}\n')
print(encode)


decode = ''
num_str = ''
for i in range(0, len(encode)):
    if encode[i].isdigit() and (encode[i-1].isalpha() or i == 0):
        num_str = encode[i]
    if encode[i].isdigit() and encode[i-1].isdigit():
        num_str = str(num_str) + encode[i]
    if encode[i].isalpha():
        decode = decode + encode[i]*int(num_str)
        num_str = 1

with open('RLE_otpt.txt', 'a') as data:
    data.write(decode)
print(decode)
