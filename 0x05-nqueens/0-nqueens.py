#!/usr/bin/python3
""" N queens """

import sys


def usage():
    """ Print usage information and exit """
    print("Usage: nqueens N")
    sys.exit(1)


def check_input():
    """ Check command-line arguments for validity """
    if len(sys.argv) != 2:
        usage()

    n = sys.argv[1]
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def queens(n, i=0, a=[], b=[], c=[]):
    """ Find possible positions for the queens on the chessboard """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """ Solve the N Queens problem and print all possible solutions """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0


if __name__ == "__main__":
    n = check_input()
    solve(n)
