# https://inf-ege.sdamgia.ru/problem?id=27693
import re
print(len(max(re.findall(r'C+', open('24.txt').read()))))