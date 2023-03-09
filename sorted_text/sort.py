import os

file_names = ['1.txt', '2.txt', '3.txt']
file_contents = []

for file_name in file_names:
    with open(file_name, encoding='utf-8') as f:
        content = f.readlines()
        file_contents.append({'name': file_name,
                              'count': len(content),
                              'content': content})

file_contents_sorted = sorted(file_contents, key=lambda x: x['count'])

with open('result.txt', 'w', encoding='utf-8') as f:
    for file_content in file_contents_sorted:
        f.write(f"{file_content['name']}\n{file_content['count']}\n")
        f.write(''.join(file_content['content']))


