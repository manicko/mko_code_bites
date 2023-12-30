path = ''
f_path = r'C:/py_exp/files/'
f_name = 'data.csv'


def read_csv(file_path, file_name, sep=','):

    with open(file_path + file_name, 'r', encoding='utf-8') as file:
        headers = file.readline().strip().split(sep)
        row_data = file.readlines()

    data = [x.strip().split(sep) for x in row_data]

    result = [{k: v for k, v in zip(headers, row)} for row in data]
    return result


print(read_csv(f_path, f_name))