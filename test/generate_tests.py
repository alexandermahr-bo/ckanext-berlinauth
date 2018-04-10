# encoding: utf-8

import json
import csv
import pprint
from jinja2 import Environment, FileSystemLoader

def convert_boolean(kv):
    lst = list(kv)
    if lst[1]=="+":
        lst[1] = True
    elif lst[1]=="-":
        lst[1] = False
    return tuple(lst)

with open('config.json') as json_data:
    config = json.load(json_data)

with open('test_matrix_datenregister.csv') as test_matrix_csv:
    reader = csv.DictReader(test_matrix_csv)
    test_matrix = []
    for line in reader:
        new_line = dict(map(convert_boolean, line.items()))
        test_matrix.append(new_line)

env = Environment(
    loader=FileSystemLoader('templates'),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template('package_actions.py.j2')
print template.render(config=config, matrix=test_matrix)