import math

def calc_offset(n):
    return max(3, 2+int(math.log10(n)))

def add_candidats(n, candidats, dist):
    if n % 3 == 0:
        candidats[n//3] = dist
    if n % 2 == 0:
        candidats[n//2] = dist

def calc_num_op(n, memo):
    if n in memo.keys():
        return memo[n]

    k = calc_offset(n)

    candidats = {}

    for i in range(1, k):
        add_candidats(n-i + 1, candidats, i)

    minimums = []
    for x in candidats.keys():
        minimums.append(calc_num_op(x, memo) + candidats[x])

    t = min(minimums)
    if n<
    memo[n] = t
    return t
  
  
if __name__ == '__main__':
    N = int(input())
    memo = {1: 0, 2: 1, 3: 1}
    print(N, calc_num_op(N, memo))

