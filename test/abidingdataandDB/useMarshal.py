import fileinput, marshal, anydbm
wordPos = {}
for line in fileinput.input():
	pos = fileinput.filename(), fileinput.filelineno()
	for word in line.split():
		wordPos.setdefault(word,[]).append(pos)
dbmOut = anydbm.open('indexfilem', 'n')
for word in wordPos:
	dbnOut{word} = marshal.dumps(wordPos[word])
	dbmOut.close()
