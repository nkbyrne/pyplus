#!/usr/bin/env python
from pprint import pprint
import textfsm

template_file = "ex1_show_int_status.txt"
template = open("ex7_template.tpl")

with open(template_file) as f:
    raw_text_data = f.read()

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

my_list = []

for line in data:
    my_dict = dict(zip(re_table.header, line))
    my_list.append(my_dict)

my_lenth = len(my_list)

for i in range(my_lenth):
    print()
    print("Device {}".format(i))
    print(my_list[i])
