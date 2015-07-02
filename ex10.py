tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# sarahs-mac:learn-python-the-hard-way SarahS$ python ex10.py
# 	I'm tabbed in.
# I'm split
# on a line.
# I'm \ a \ cat.

# I'll do a list:
# 	* Cat food
# 	* Fishies
# 	* Catnip
# 	* Grass

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,

#^ that was really cool, but I can't copy and paste it. Do it yourself. ;)