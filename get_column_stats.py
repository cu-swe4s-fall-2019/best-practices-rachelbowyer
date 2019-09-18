import sys
import math
import argparse
import csv


def main(file, col):
    # setting files name
    file_name = file  # set file name

    f = open(file_name, 'r')
    V = []

    # checking to see if user input is integer
    if type(col) == int:
        col_num = int(col)
    else:
        col = str(col)
        if '.' not in col:
            col_num = int(col)
        else:
            print('Must specify integer for col num')
            raise ValueError

    for l in f:
        A = [int(float(x)) for x in l.split()]
        # check if user input is in range
        if col_num >= len(A):
            print('Col number out of bounds')
            raise ValueError
        elif col_num < 0:
            print('Col number out of bounds')
            raise ValueError
        else:
            V.append(A[col_num])

    mean = sum(V)/len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)

    return round(mean, 4), round(stdev, 4)


if __name__ == '__main__':
    # argparse setup
    parser = argparse.ArgumentParser(description="Specify col for calc")
    parser.add_argument('file', type=str, help='specify files')
    parser.add_argument('col_num', type=str, help='choose col num, start @ 0')
    args = parser.parse_args()

    main(args.file, args.col_num)
