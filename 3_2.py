#СТРОКА 98 МЕТОД ZIP


path = "file.txt"

with open(path, 'r', encoding='UTF-8') as file:
    eq_str1 = file.readline()
print(eq_str1) 

path2 = "file2.txt"

with open(path2, 'r', encoding='UTF-8') as file2:
    eq_str2 = file2.readline()
print(eq_str2) 


# path = "file.txt"
# equasion_str = open(path, 'r')

# path2 = "file2.txt"
# equasion_str2 = open(path2, 'r')
# eq_str1 = ""
# eq_str2 = ""


# for line in equasion_str:
#     eq_str1 = line + eq_str1
# equasion_str.close()

# print(eq_str1)


# for line in equasion_str2:
#     eq_str2 = line + eq_str2
# equasion_str2.close()

# print(eq_str2)




def get_coef_and_pow_list(eq_str):
    coef_dic = {}
    eq_str = eq_str.replace(' ', '').replace('*', '')
    print(eq_str)

    if eq_str[0] == 'x':
        eq_str = '1' + eq_str
        print(eq_str)

    for i in range(0, len(eq_str)):
        if eq_str[i] == 'x':
            if eq_str[i-1] == '+':
                if eq_str[i+1] != '+':
                    coef_dic[eq_str[i+1]] = 1
                else:
                    coef_dic['1'] = 1

            else:
                temp1 = ''
                j = 1
                while eq_str[i-j] != '+':
                    if i-j >= 0:
                        temp1 = eq_str[i-j] + temp1
                    j += 1
                if eq_str[i+1] != '+':
                    coef_dic[eq_str[i+1]] = int(temp1)
                else:
                    coef_dic[1] = 1

        if eq_str[i] == '=':
            if eq_str[i-1] != 'x':
                last_coef1 = ''
                k = 1
                while eq_str[i-k] != '+':
                    if i-k >= 0:
                        last_coef1 = eq_str[i-k] + last_coef1
                    k += 1
                print(f"last coef = {last_coef1}")
    coef_dic[0] = int(last_coef1)

    return coef_dic


coef_pow_dict1 = get_coef_and_pow_list(eq_str1)
coef_pow_dict2 = get_coef_and_pow_list(eq_str2)

print(coef_pow_dict1)
print(coef_pow_dict2)

# сложим значения словарей с одинаковыми ключами
# summ_dic = coef_pow_dict2.copy()
# for k, v in coef_pow_dict2.items():
#     summ_dic[k] = coef_pow_dict1.get(k) + v
# print(summ_dic)
summ_dic = dict(zip(coef_pow_dict2, coef_pow_dict1))
print(summ_dic)


summ_equasion = ""
for key, value in summ_dic.items():
    summ_equasion += str(value) + '*x**' + str(key) + " + " 


summ_equasion = summ_equasion[:len(summ_equasion) -3]
summ_equasion += ' = 0'
print(f"Сумма многочленов: {summ_equasion}")