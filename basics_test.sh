#!/bin/bash


#below is assignment 1 code
pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py data.txt 2


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py data.txt 2

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py data.txt 5


(for i in `seq 1 10`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py data.txt a

#above is assigment 1 code



#below is assigment 2 code

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# the below tests use file full of random numbers

#use bash to calculate column mean
mean=$(awk '{ total += $1; count++} END { print total/count }' data.txt)

#use bash to calculates column std
std=$(awk '{sum+=$1; sumsq+=$1*$1} END {print sqrt(sumsq/NR - (sum/NR)^2)}' data.txt)

#exclude so many digits
stdtrim=${std::-2}

#test if the mean function works
run mean_test python get_column_stats.py data.txt 0
assert_in_stdout $mean

#test if the std function works
run std_test python get_column_stats.py data.txt 0
assert_in_stdout $stdtrim

#test for error raised by bad col value, non int val
run std_test python get_column_stats.py data.txt 0.5
assert_exit_code 1

#test for error raised by bad col value, non in col range
run std_test python get_column_stats.py data.txt 500
assert_exit_code 1
