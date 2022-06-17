
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



def q_intrest(numlist):
    global qcall
    qcall+=1
    cr = len(numlist)
    if cr == 1:
        return numlist[0]
    else:
        s = sum(sumtables[cr-1][-numlist[0]::])
        if numlist[1] >= numlist[0]:
            newnuml = [numlist[0]] * (cr-1)
            s += (q_intrest(numlist[1:]) - q_intrest(newnuml) + 1)

        return s


if __name__ == '__main__':
    L = 10
    R = 1000000000


    rs = int_to_list(R)
    ls = int_to_list(L)



    print(f'l = {ls}')
    normalize_left(ls)
    print(f'l_norm = {ls}')

    print(f'r = {rs}')
    normalize_right(rs)
    print(f'r_norm = {rs}')

    table0 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sumtables = [table0]

    for n in range(1, len(rs)):
        prev_sum = sumtables[n - 1]
        cur_sumtable = []
        for row in range(10):
            if row == 0:
                cur_sumtable.append(1)
            else:
                cur_sumtable.append(cur_sumtable[row-1] + prev_sum[row])
        sumtables.append(cur_sumtable)

    print(sumtables)

    # for i in range(150):
    #         print(i, q_intrest(int_to_list(i)))

    qcall = 0

    qt = q_intrest(rs)
    print(qt, qcall)
         # - q_intrest(ls)

    # divisor = 10**9+7
    # print(qt, qt % divisor)

    # i = 10
    # print(i, q_intrest(int_to_list(i)))
