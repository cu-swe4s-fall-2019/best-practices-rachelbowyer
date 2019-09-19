# best-practices

## Purpose
style.py: demonstrates proper coding style but is not useful for anything in particular.

get_column_stats.py: this code takes a .txt file of numbers and returns the standard deviation and mean of the user specified column in the txt file.  The user must specify the file name and the column number of interest in that order.  Column numbering starts at 0 NOT 1.

basics_test.py: this code runs various unit tests for functions in get_column_stats.py.  It tests for the following four things:
(1) the mean function is correct
(2) the standard deviation function is correct
(3) an error is raised if user inputs an integer for the column number
(4) the user inputs a column number that makes sense for the file size

basics_test.sh: this shell files runs rudimentary tests on get_column_stats.py (from assignment 0) and also runs functional tests on get_column_stats.py (from assignment 1)

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

To run the rudimentary and functional tests on get_column_stats.py in the basics_test.sh file use

```
./basics_test.sh
```

From assignment 0, The basics_test.sh file will show the following rudimentary tests: two successful tests - one on a file of random numbers and another on a file filled with 1's - and two unsuccessful tests.  The unsuccessful test are caused by inappropriate user input and the program will print a statement saying why the input was inappropriate.

From assigment 1, the basics_test.sh file will show four functional tests.  The four functional tests being run are:
(1) that the mean function is correct (using random file)
(2) that the standard deviation function is correct (using random file)
(3) that an error is raised if user inputs an integer for the column number  (using random file)
(4) that the user inputs a column number that makes sense for the file size  (using random file)


To run basics_test.py use the command
```
python basics_test.py
```


## Example
if data.txt is the file of interest and the user want to know the statistics of the 3rd column (starting from 0 counting), the command to run get_column_stats.py is 

```
python get_column_stats.py data.txt 3
```

