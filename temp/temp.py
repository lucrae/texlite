import re

s = 'Aliquam `convallis` felis *id* lacus ultricies.'
matches = re.findall('`(.*?)`', s)
for match in matches:
    s = s.replace(f'`{match}`', r'\texttt' + f'{{{match}}}')

print(matches)

print(s)