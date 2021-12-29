import itertools
from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_tuple = (itertools.zip_longest(tutors, klasses, fillvalue='None'))
print(type(gen_tuple)) # <class 'itertools.zip_longest'> - работает как генератор

def finish_tuple():
    if len(tutors) < len(klasses):
        for name, klas in zip(tutors, klasses):
            yield name, klas
    else:
        for name, klas in zip_longest(tutors, klasses):
            yield name, klas


gen_tuple = finish_tuple()
print(type(gen_tuple)) # <class 'generator'>
print(next(gen_tuple)) # ('Иван', '9А')
print(next(gen_tuple)) # ('Анастасия', '7В')
print(next(gen_tuple)) # ('Петр', '9Б')
print(next(gen_tuple)) # ('Сергей', '9В')
print(next(gen_tuple)) # ('Дмитрий', '8Б')
print(next(gen_tuple)) # ('Борис', '10А')
print(next(gen_tuple)) # ('Елена', '10Б')
print(next(gen_tuple)) # ('None', '9А')
print(next(gen_tuple)) # StopIteration
print(next(gen_tuple)) # StopIteration