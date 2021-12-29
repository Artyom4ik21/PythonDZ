
import re

def email_parse(e_mail):
    pattern = re.compile(r'(?P<username>[A-z0-9/.]+)@(?P<domain>\w+\.\w+)')
    result = pattern.match(e_mail)

    if result:
        return result.groupdict()

    raise ValueError(f'Incorrect e-mail: {e_mail}')

print(email_parse('antongri.shin1994@mail.ru'))