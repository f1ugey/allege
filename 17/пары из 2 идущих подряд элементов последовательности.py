# последовательность, в ней нужно найти пару, в которой одно число делится на 3. Найти количество пар, и максимальную
# сумму элементов
a = list(map(int, open('file.txt')))    # добавляется скачанный файл(копировать в загрузках и вставить в список слева)
count = 0  # количество найденных пар
s = []  # список со всеми суммами элементов пар
for i in range(len(a) - 1):
    if (a[i] % 3 == 0) or (a[i + 1] % 3 == 0):  # меняем по условию %(число на которое делится(==0) или не делится(==1))
        count += 1
        s.append(a[i] + a[i + 1])   # меняем на разность если есть в условии
print(count, max(s))    # меняем на min если в условии минимальная сумма
