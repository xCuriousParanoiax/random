



with open(targetFile) as f:	# Counts all lines
	numberOfLines = len([l for l in f.readlines()])

print(numberOfLines)






with open(targetFile) as f:	# Excludes empty lines only
	numberOfLines = len([l for l in f.readlines() if l.strip()])

print(numberOfLines)






with open(targetFile) as f:	# Excludes empty lines and lines who's first none empty character is a hashtag
	numberOfLines = len([l for l in f.readlines() if l.strip() and not l.strip().startswith("#")])

print(numberOfLines)






