from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on on line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# Sarahs-Mac:learn-python-the-hard-way SarahS$ cat test.txt
# Mary had a little lamb
# Its fleece was white as snow
# It was also tasty
# Sarahs-Mac:learn-python-the-hard-way SarahS$ python ex17.py test.txt new_file.txt
# Copying from test.txt to new_file.txt
# The input file is 70 bytes long
# Does the output file exist? False
# Ready, hit RETURN to continue, CTRL-C to abort.

# Alright, all done.