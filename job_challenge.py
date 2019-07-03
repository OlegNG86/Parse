example = ['лампа', 'медведь', 'медведь' 'лампа']
minimal = 10

def searchDouble(list, minimal):

    if not list == []:

        for i in range(1, len(list)):

            if list[0] == list[i]:
                if minimal > i:
                    minimal = i
                    print('Минимальный дубликат найден, это: ', list[minimal], '. Расстояние между дубликанами: ', minimal, ' значений')
        return searchDouble(list[1:], minimal)
    else:
        print('Программа завершена')


searchDouble(example, minimal)

