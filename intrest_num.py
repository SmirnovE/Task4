
def normalize_left(num_list):
    max_num = 0

    for i in range(len(num_list)):
        max_num = max(max_num, num_list[i])
        if num_list[i] < max_num:
            num_list[i] = max_num


def normalize_right(num_list):
    num_len = len(num_list)
    i = num_len - 2

    if i <= 0:
        return

    while i >= 0:

        if num_list[i] > num_list[i + 1]:
            num_list[i] -= 1
            for k in range(i + 1, num_len):
                num_list[k] = 9

        i -= 1

    if num_list[0] == 0:
        num_list.remove(0)

def int_to_list(num):
    r_list = []
    for ri in str(num):
        r_list.append(int(ri))
    return r_list

if __name__ == '__main__':
    L = 809
    R = 10**10


    rs = int_to_list(R)
    ls = int_to_list(L)



    print(f'l = {ls}')
    normalize_left(ls)
    print(f'l_norm = {ls}')

    print(f'r = {rs}')
    normalize_right(rs)
    print(f'r_norm = {rs}')

    tables = []
    table0 = (9, 8, 7, 6, 5, 4, 3, 2, 1)

    sumtables = []
    sumtables.append(table0)

    for n in range(1, len(rs) - 1):
        prev_sum = sumtables[n - 1]
        table_n = []
        for index in range(81):
            col = index // 9
            row = index - col * 9
            if col > row:
                table_n.append(0)
            else:
                table_n.append(prev_sum[row])

            tables.append(table_n)
        cur_sumtable = []
        for row in range(9):
            cur_sum = 0
            for col in range(9):
                cur_sum += table_n[row * 9 + col]
            cur_sumtable.append(cur_sum)
        sumtables.append(cur_sumtable)

    print(sumtables)
