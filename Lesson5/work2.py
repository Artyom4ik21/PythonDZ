# написать генератор нечётных чисел от 1 до n (включительно), не используя yield

n = int(input('Введите число: '))
odd_nums_gen = (num for num in range(1, n + 1, 2))

print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))

# etc