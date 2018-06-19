import numpy as np
import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(funcName)s - %(lineno)d - %(message)s')

#
# complete_inout = sys.stdin.read()
# print(complete_inout)

sys.stdin = open('input.txt', 'r')
# sys.stdin = open('A-large-practice.in', 'r')
# sys.stdin = open('A-small-practice.in', 'r')
sys.stdout = open('output.txt', 'w')


def solve_a_case(case_num):
    num_case = int(input())
    logging.debug("num_case = {}".format(num_case))
    cases = [int(n) for n in input().split()]

    num_city = max(cases)
    # num_city = 500     # 500 for small practice; 5000 for large practice
    logging.debug("num_city = %d" % num_city)

    x = np.asarray(cases)
    logging.debug("x.shape = {}".format(x.shape))

    y = np.zeros(num_city+1, dtype=int)

    for j in range(num_case):
        for k in range(x[j*2], x[j*2+1]+1):
            y[k] += 1
    logging.debug("y.shape = {}".format(y.shape))
    logging.debug("y = {}".format(y))

    p = int(input())

    out = []
    for n in range(1, p+1):
        out.append(y[int(input())])

    out_str = " ".join(map(str, out))

    return out_str


if __name__ == "__main__":
    num_test_case = int(input())

    for i in range(1, num_test_case+1):
        result = solve_a_case(i)
        print("Case #{}: {}".format(i, result))
        if i < num_test_case:
            input()  # read the empty line before next test case
        else:
            break

    logging.debug('This is a log message.')


