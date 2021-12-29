# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_src = set()
double_src = set()
for el in src:
    if el not in double_src:
        unique_src.add(el)
    else:
        unique_src.discard(el)
    double_src.add(el)

#print(double_src) # {1, 2, 3, 4, 7, 10, 11, 44, 23}
#print(unique_src) # {1, 3, 4, 10, 11, 23}

unique_src_ord = [el for el in src if el in unique_src]
print(unique_src_ord) # [23, 1, 3, 10, 4, 11]