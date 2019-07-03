text = []
with open('M:\SBERP_180601_190623.txt', 'r') as f:
    for i in f.readlines():
        text.append(i)
list = []
for i in range(len(text)):
    list.append(text[i].split(','))
k169 = 0
schet = 0
schet1 = 0
schet2 = 0


# for i in range(1, len(list)):
#     schet2 += 1
#     print('{} | {:.2f} | {:.2f}'.format(list[i][2], float(list[i][6]), float(list[i][5])))
#     if float(list[i][6]) <= 169 and k169 == 0:
#         k169 += 1
#         schet += 1
#     if float(list[i][5]) >= 169*1.09 and k169 == 1:
#         k169 -= 1
#         schet1 += 1
# print(k169)
# print(schet, schet1)
# print(schet2)

def analyse(list, min, max, k):
    k169 = 0
    schet = 0
    schet1 = 0
    schet2 = 0
    sum_list = []
    sum_deals = 0

    for number in range(min, max):

        for i in range(1, len(list)):
            schet2 += 1
            if float(list[i][6]) <= number and k169 == 0:
                k169 += 1
                schet += 1
            if float(list[i][5]) >= number * k and k169 == 1:
                k169 -= 1
                schet1 += 1

        sum_list.append([number, k, schet, schet1])
    print(sum_list)


   # print(number, k, schet, schet1, number * schet1 * 10)
    #print(sum_deals)

    # for i in range(len(sum_list)):
    #     print(sum_list[i][4])




analyse(list, 150, 230, 1.03)


