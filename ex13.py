from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#  sarahs-mac:learn-python-the-hard-way SarahS$ python ex13.py first 2nd 3rd
# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd
# sarahs-mac:learn-python-the-hard-way SarahS$ python ex13.py stuff things that
# The script is called: ex13.py
# Your first variable is: stuff
# Your second variable is: things
# Your third variable is: that
# sarahs-mac:learn-python-the-hard-way SarahS$ python ex13.py apple orange grapefruit
# The script is called: ex13.py
# Your first variable is: apple
# Your second variable is: orange
# Your third variable is: grapefruit