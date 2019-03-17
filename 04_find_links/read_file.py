import re

"""
read a text file
find all links
"""

with open("some.txt", 'r') as f:
	data = f.read()

	links = re.findall('"((http|ftp)s?://.*?)"', data)
	for i in links:
		print(i[0])
