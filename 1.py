import re

a = 'есть некоторый текст! изменить некоторый текст.'
print(''.join(map(lambda x: x.capitalize(), re.split(r'(!\s|\.\s)', a))))