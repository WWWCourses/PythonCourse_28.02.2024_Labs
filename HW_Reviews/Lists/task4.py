# ================= Task 4 ================
# To create a program that reads integers entered by the user,
# until an empty line is entered. After all the numbers have been read, the program
# should display all negative numbers followed by zeros followed by alls
# positive numbers. In each group, the numbers must appear in the same order, c
# which are entered by the user.
# For example, if the user enters the values
# 3, -4, 1, 0, -1, 0, and -2,
# your program should output the values -4, -1, -2, 0, 0, 3, and 1 .
# Your program should display each value on a new line.
input_numbers = [3, -4, 1, 0, -1, 0, -2]
negatives  = [el for el in input_numbers if el<0 ]
zeros  =  [el for el in input_numbers if el==0 ]
positives  =  [el for el in input_numbers if el>0 ]

# unpack lists into output:
output = [*negatives, *zeros, *positives]
print(output)