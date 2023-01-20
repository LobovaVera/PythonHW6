#СТРОКА 11 LIST COMPR



your_list = [1.1, 2451.0002, 3.1, 5, 10.0001]
temp = 0
our_list = []
temp_list = []

int_list = list(map(int, your_list))
temp_list = [your_list[i] - int_list[i] for i in range(len(your_list))]
our_list = list(map(round, temp_list, [10 for i in range(len(your_list))]))
print (temp_list)

# for i in range(len(your_list)):
#     temp = int(your_list[i])
#     print(temp)
#     temp_list.append(your_list[i]-temp)
#     print(temp_list)
#     if temp_list[i] != 0:
#         our_list.append(round((temp_list[i]), 10))

print(our_list)

# find min and max
maxx = 0

for el in our_list:
    if el > maxx:
        maxx = el
minn = maxx
for el in our_list:
    if el < minn:
        minn = el
print(round((maxx-minn), 10))
