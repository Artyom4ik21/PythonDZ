import re
import requests


def currency_rates(cyr):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    r = requests.get(url)
    contents = r.text  # выводим текст
    char_code = re.findall(r'<CharCode>(.*?)</CharCode>', contents)  # выводим список кодов валюты
    value = re.findall(r'<Value>(.*?)</Value>', contents)  # выводим список курса валюты
    new_dict = dict(zip(char_code, value))  # делаем из двух списков словарь формата char_code : value
    return new_dict.get(cyr) # cyr вошла в char_code и вернула значение

#print(currency_rates('USD'))

if __name__ == '__main__':
    import sys
    result = currency_rates(sys.argv[1])
    print('Текущий курс:', result)