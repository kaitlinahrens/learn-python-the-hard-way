from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# sarahs-mac:learn-python-the-hard-way SarahS$ python ex16.py test.txt
# We are going to erase 'test.txt'.
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# ?^CTraceback (most recent call last):
#   File "ex16.py", line 9, in <module>
#     raw_input("?")
# KeyboardInterrupt
# sarahs-mac:learn-python-the-hard-way SarahS$ python ex16.py test.txt
# We are going to erase 'test.txt'.
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# ?
# Opening the file...
# Truncating the file. Goodbye!
# Now I'm going to ask you for three lives.
# line 1: Mary had a little lamb
# line 2: Its fleece was white as snow
# line 3: It was also tasty
# I'm going to write these to the file.
# Traceback (most recent call last):
#   File "ex16.py", line 29, in <module>
#     target.write(line3)
# NameError: name 'line3' is not defined #accidentally wrote line2 again on line 21. i fixed it and ran it again though
# sarahs-mac:learn-python-the-hard-way SarahS$ python ex16.py test.txt
# We are going to erase 'test.txt'.
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# ?
# Opening the file...
# Truncating the file. Goodbye!
# Now I'm going to ask you for three lines.
# line 1: Mary had a little lamb
# line 2: Its fleece was white as snow
# line 3: It was also tasty
# I'm going to write these to the file.
# And finally, we close it.