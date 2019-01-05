import vexdb as v

tmp = v.getSeasonRankings(vrating_rank=1)

for r in tmp:
# 	team = v.getTeams(team=r["team"])[0]
	print "%s: %s(vRating %s)" % (r["season"], r["team"], r["vrating"])