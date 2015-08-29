from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line +1 
print_a_line(current_line, current_file)

# Sarahs-Mac:learn-python-the-hard-way SarahS$ python ex20.py test.txt
# First let's print the whole file:

# Mary had a little lamb
# Its fleece was white as snow
# It was also tasty

# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 Mary had a little lamb

# 2 Its fleece was white as snow

# 3 It was also tasty