import vexdb as v

n = v.getNumRankings(rank=1)
print n
tmp = v.getRankings(rank=1, get_all=True)

sum = 0.0
for ranking in tmp:
	numMatches = ranking["wins"] + ranking["losses"] + ranking["ties"]
	if numMatches != 0:
		sum += ranking["wins"]/numMatches
	else:
		n -= 1
	
print sum/n