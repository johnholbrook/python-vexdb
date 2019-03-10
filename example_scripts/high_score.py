#Finds the highest match score in the current season worldwide,
#as well as the highest match score in the current season in
#West Virginia

import vexdb as v

num_rankings = v.getNumRankings(season="current")
print("Getting all %s rankings in the current season..." % num_rankings)
all_rankings = v.getRankings(season="current", get_all=True)

highest_score = 0

for ranking in all_rankings:
	if ranking["max_score"] > highest_score:
		highest_score = ranking["max_score"]

print("Highest Score Worldwide: %s" % highest_score)

all_wv_events = v.getEvents(region="West Virginia", season="current")
all_wv_rankings = []
for event in all_wv_events:
	all_wv_rankings += v.getRankings(sku=event["sku"])

highest_wv_score = 0

for ranking in all_wv_rankings:
	if ranking["max_score"] > highest_wv_score:
		highest_wv_score = ranking["max_score"]

print("Highest Score in WV: %s" % highest_wv_score)