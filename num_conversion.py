def all_bases(num: int):
    base_val = {'bin': 2, 'oct': 8, 'hex': 16}
    for base in base_val.keys():
        print(dec_to_base(num, base))


def dec_to_base(num: int, base='bin'):
    base_val = {'bin': 2, 'oct': 8, 'hex': 16}
    hex_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    devisor = base_val[base]

    output = ''
    while num > 0:
        num, rest = divmod(num, devisor)
        if rest >= 10:
            rest = hex_letters[rest]
        output = str(rest) + output
    return output


n = int(input())
all_bases(n)
