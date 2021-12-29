# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
def odd_number(n):
    for num in range(1, n + 1, 2): # создаем диапазон
        yield num

odd_to_10 = odd_number(10)
print(next(odd_to_10)) # 1
print(next(odd_to_10)) # 3
print(next(odd_to_10)) # 5

# etc 