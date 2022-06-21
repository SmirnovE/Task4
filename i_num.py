def int_to_list(num):
    r_list = []
    for ri in str(num):
        r_list.append(int(ri))
    return r_list


def q_intrest_g(n, r):
    if r == 1:
        return n
    else:
        return 1 + sum(sumtables[r-1][-n::])
        

def q_intrest(numlist):
    cr = len(numlist)
    if cr == 1:
        return numlist[0]
    else:
        s = sum(sumtables[cr-1][-numlist[0]::])
        if numlist[1] >= numlist[0]:
            s += (q_intrest(numlist[1:]) - q_intrest_g(numlist[0], cr-1) + 1)

        return s

def calc_tables(r):
    table0 = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sumtables.append(table0) 

    for n in range(1, r):
        prev_sum = sumtables[n - 1]
        cur_sumtable = []
        for row in range(10):
            if row == 0:
                cur_sumtable.append(1)
            else:
                cur_sumtable.append(cur_sumtable[row-1] + prev_sum[row])
        sumtables.append(cur_sumtable)



if __name__ == '__main__':
    L = 10
    R = 10**100

    sumtables = []
    
    rs = int_to_list(R)
    ls = int_to_list(L)

    calc_tables(len(rs))


    qt = q_intrest(rs)
    print(qt)

         # - q_intrest(ls)

    # divisor = 10**9+7
    # print(qt, qt % divisor)

