from sys import argv #standard - adds features to the script & holds the arguments

script, filename = argv #"unpacks" the argv so that i can work with the variables script & filename

txt = open(filename) #reads the file

print "Here's your file %r:" % filename #prints a little line, adds a little variable to spice things up
print txt.read() #read the file, but with no parameters

print "Type the filename again:" #duh
file_again = raw_input("> ") #prompts you to enter the file name in again

txt_again = open(file_again) #uses txt_again as a variable which allows the next line to work

print txt_again.read() #reads the file again

# sarahs-mac:learn-python-the-hard-way SarahS$ python ex15.py ex15_sample.txt
# Here's your file 'ex15_sample.txt':
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# Type the filename again:
# > ex15_sample.txt
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.