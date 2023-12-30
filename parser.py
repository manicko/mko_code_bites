from functools import wraps, partial

input_data_file = r'C:\py_exp\files\in_data\2023_w13_palomars.csv'
output_data_file = r'C:\py_exp\files\out_data\2023_w13_palomars.csv'


def file_process(file_name: str, delimiter: str = ','):
    with open(file=file_name, mode='r', encoding='utf-8') as raw_data_file:
        for index, line in enumerate(raw_data_file):
            print("Line {}: {}".format(index, line.rstrip()))


with open(f_path+f_name_w, 'w') as file_w:
    for r in res:
        for n in r.keys():
            print(n, file=file_w)