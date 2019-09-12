# best-practices

## Purpose
style.py demonstrates proper coding style but is not useful for anything in particular.

get_column_stats.py: This code takes a .txt file of numbers and returns the standard deviation and mean of the user specified column in the txt file.  The user must specify the file name and the column number of interest in that order.  Column numbering starts at 0 NOT 1.

## Running
To run get_column_stats.py use the command
```
python get_column_stats.py file col_num
```
where file is your file of interest and col_num is the column you wish to specify.

You may also use the shell file basics_test.sh to run some simple tests on get_column_stats.py

Run the following command to make the .sh file executable.
```
chmod +x basics_test.sh
```

To run the tests on get_column_stats.py in the basics_test.sh file use

```
./basics_test.sh
```

The basics.text.sh file will show two successful tests - one on a file of random numbers and another on a file filled with 1's - and two unsuccessful tests.  The unsuccessful test are caused by inappropriate user input and the program will print a statement saying why the input was inappropriate.

## Example
if data.txt is the file of interest and the user want to know the statistics of the 3rd column (starting from 0 counting), the command to run get_column_stats.py is 

```
python get_column_stats.py data.txt 3
```

