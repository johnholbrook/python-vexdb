#Computes the average win rate of all #1 seeds across all tournaments ever

from __future__ import print_function
import vexdb as v

num_top_seeds = v.getNumRankings(rank=1)
print("Getting data for all %s top seeds..."  % num_top_seeds)

all_top_seeds = v.getRankings(rank=1, get_all=True)


win_rate_sum = 0

for ranking in all_top_seeds:
	if (ranking["wins"]) != 0:
		num_matches = ranking["wins"] + ranking["losses"] + ranking["ties"]
		win_rate_sum += float(ranking["wins"])/num_matches
		# print(float(ranking["wins"])/num_matches)
	else:
		#exclude #1 seeds with 0 wins (likely from events that haven't happened yet)
		num_top_seeds -= 1

avg_win_rate = (win_rate_sum / num_top_seeds) * 100

print("Average win rate of a #1 seed: %s percent." % avg_win_rate)