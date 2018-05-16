# Question:
# Write a Python program that accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting
# them alphabetically.
#
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.
#
#
# Solution:

# Didn't specify the python version, so:
try:
	# required to make it work in both python2 and python3.
	input = raw_input
except:
	pass

words = input("input words: ")
seq = words.split(",")
seq.sort()
print(",".join(seq))
