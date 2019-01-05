import vexdb as v

tmp = v.getSkills(team="8768A", season="In The Zone")

for sr in tmp:
	print "Score: %s" % sr["score"]