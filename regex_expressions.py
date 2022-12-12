# Быковский Сергей Сергеевич
# ИДБ-21-11
# Из документа HTML вывести все e-mail.

import re

#pattern = re.compile(r'[a-zA-Z0-9.-_]+@[a-zA-Z-]+\.(com|edu|net|ru|du)')
pattern = re.compile(r'[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

with open('data_page.html', 'r') as f:
    contents = f.read()

    matches = pattern.findall(contents)

    for match in matches:
        print(match)