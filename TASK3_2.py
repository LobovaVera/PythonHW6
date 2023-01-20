# новый метод чтения файла


path = r'text.txt'

with open(path, 'r', encoding= 'UTF-8') as file:
    our_string = file.readline()

path = r'text2.txt'

with open(path, 'r', encoding= 'UTF-8') as file:
    our_string2 = file.readline()

our_string.replace(' ', '')
our_string2.replace(' ', '')

def unzip(our_string):
    num_string = ''
    letter_list = []
    for el in our_string:
        if el == '0':
            num_string += '0'
        else:
            try:
                if int(el):
                    num_string += el
            except:
                if el != ' ':
                    num_string += ' '
                    letter_list.append(el)
    num_list = num_string.split()
    
    for i in range(0, len(num_list)):
        for j in range(0, int(num_list[i])):
            print(letter_list[i], end='')


unzip(our_string2)
