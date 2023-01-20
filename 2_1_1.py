#СТРОКА 6 МЕТОД LIST COMPR



my_list = [2, 3, 5, 9, 3]
res = [ my_list[i] for i in range(len(my_list)) if i % 2 != 0]
    # if i % 2 != 0:
    #     res += my_list[i]
print(res)

summ = 0
for el in res:
  summ += el
  
print(summ)