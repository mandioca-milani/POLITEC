import os
import random


import abin_2018_03_11_area_8
import pc_pb_2021_cargo_7
import pc_pb_2021_cargo_2

q = list()
q += abin_2018_03_11_area_8.q
q += pc_pb_2021_cargo_7.tecnologia
#q += pc_pb_2021_cargo_2.tecnologia
random.shuffle(q)


md = '\n---\n\n'
r = list()
for i, k in zip(q, range(1, len(q) + 1)):
    md += f'Questão {k}\n\n'
    for q in i['q']:
        md += q + '\n\n'
    if len(i['e']) == 5:
        random.shuffle(i['e'])
        md += '\n'.join([
            f'- a. {i["e"][0]}',
            f'- b. {i["e"][1]}',
            f'- c. {i["e"][2]}',
            f'- d. {i["e"][3]}',
            f'- e. {i["e"][4]}',
        ]) + '\n'
        if i['r'] == i['e'][0]:
            r += [f'{k} - A']
        elif i['r'] == i['e'][1]:
            r += [f'{k} - B']
        elif i['r'] == i['e'][2]:
            r += [f'{k} - C']
        elif i['r'] == i['e'][3]:
            r += [f'{k} - D']
        elif i['r'] == i['e'][4]:
            r += [f'{k} - E']
        else: r += [f'{k} - Nulo']
    else:
        md += '\n'.join([
            f'- {i["e"][0]}',
            f'- {i["e"][1]}',
        ]) + '\n'
        if i["r"]:
            r += [f'{k} - {i["r"]}']
        else:
            r += [f'{k} - Nulo']
    md += '\n---\n\n'

md += '|       | Gabarito |       |\n'
md += '| :---: | :------: | :---: |\n'
while len(r) % 3:
    r += ['']
while len(r):
    md += '| {} | {} | {} |\n'.format(
        r.pop(0), r.pop(0), r.pop(0),
    )

with open('./prova.md', 'w') as f:
    f.write(md)

os.system('pandoc ./prova.md -o ./prova.pdf')
os.system('pandoc ./prova.md -o ./prova.html')
