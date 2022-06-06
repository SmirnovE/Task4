N = 32718

NumOp = [0 if i==0 else 1 for i in range(N)]

calculatedN = 3


def min_operations(n:int):
    global calculatedN
    if n <= calculatedN:
        return NumOp[n-1]


    cand = [n-1]
    if n % 3 == 0:
        cand.append(n // 3)
    if n % 2 == 0:
        cand.append(n // 2)
    minimums = []
    for x in cand:
        minimums.append(min_operations(x))
        t = min(minimums)

    NumOp[n-1] = t + 1
    calculatedN = max(n, calculatedN)
    return  NumOp[n-1]

if __name__ == '__main__':
    for i in range(1, N+1):
        tmp = min_operations(i)

    print(N, tmp)
