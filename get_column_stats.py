import sys
import math
import argparse
import csv

# argparse setup
parser = argparse.ArgumentParser(description="Specify col for std, mean calc")
parser.add_argument('file', type=str, help='specify files')
parser.add_argument('col_num', type=str, help='choose column num, start at 0')
args = parser.parse_args()

# setting files name
file_name = args.file  # set file name

# checking to see if user input is integer
try:
    int(args.col_num)
    col_num = int(args.col_num)
except Exception:
    print('Must specify integer for col num')
    sys.exit(1)


f = open(file_name, 'r')
V = []


def main():
    for l in f:
        A = [int(x) for x in l.split()]
        # check if user input is in range
        try:
            V.append(A[col_num])
        except Exception:
            print('Col number out of bounds')
            sys.exit(1)

    mean = sum(V)/len(V)

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
