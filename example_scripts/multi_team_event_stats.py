# Displays information about one or more teams at a given event
# (in this case, teams from WV at the "Night at the Museum" 
# signature event)

from __future__ import print_function
import vexdb as v

event_sku = "RE-VRC-18-6207"
subject_teams = ["3273B", "8330B", "8330H", "99075A"]

all_team_wins = 0
all_team_losses = 0
all_team_ties = 0


#Display every match involving one of the subject teams
for this_team_number in subject_teams:
	this_team_info = v.getTeams(team=this_team_number)[0]
	print("Individual match results for %s %s:" % (this_team_info["number"], this_team_info["team_name"]))
	#Get all scored qualification matches from this team at this event.
	this_team_matches = v.getMatches(sku=event_sku, team=this_team_number, scored="1", round="2")
	for match in this_team_matches:
		if this_team_number == match["red1"] or this_team_number == match["red2"]: #Team was red
			if match["redscore"] > match["bluescore"]: #Team was red and won
				all_team_wins += 1
				# print ("%s-%s-%s" % (all_team_wins, all_team_losses, all_team_ties))
				print("Won match %s, %s-%s" % (match["matchnum"], match["redscore"], match["bluescore"]))
			elif match["bluescore"] > match["redscore"]: #Team was red and lost
				all_team_losses += 1
				# print ("%s-%s-%s" % (all_team_wins, all_team_losses, all_team_ties))
				print("Lost match %s, %s-%s" % (match["matchnum"], match["bluescore"], match["redscore"]))
			else: #Team was red and tied
				all_team_ties += 1
				# print ("%s-%s-%s" % (all_team_wins, all_team_losses, all_team_ties))
				print("Tied match %s, %s-%s" % (match["matchnum"], match["bluescore"], match["redscore"]))

		elif this_team_number == match["blue1"] or this_team_number == match["blue2"]: #Team was blue
			if match["bluescore"] > match["redscore"]: #Team was blue and won
				all_team_wins += 1
				# print ("%s-%s-%s" % (all_team_wins, all_team_losses, all_team_ties))
				print("Won match %s, %s-%s" % (match["matchnum"], match["bluescore"], match["redscore"]))
			elif match["redscore"] > match["bluescore"]: #Team was blue and lost
				all_team_losses += 1
				# print ("%s-%s-%s" % (all_team_wins, all_team_losses, all_team_ties))
				print("Lost match %s, %s-%s" % (match["matchnum"], match["redscore"], match["bluescore"]))
			else: #Team was blue and tied
				all_team_ties += 1
				# print ("%s-%s-%s" % (all_team_wins, all_team_losses, all_team_ties))
				print("Tied match %s, %s-%s" % (match["matchnum"], match["bluescore"], match["redscore"]))
	print()

#Total record of all subject teams
win_rate = (float(all_team_wins))/(all_team_wins+all_team_losses+all_team_ties) * 100
print("Overall, teams from WV are %s-%s-%s (win rate of %s%%)." % (all_team_wins, all_team_losses, all_team_ties, win_rate))
print()

#Individual standings of each subject team
for this_team_number in subject_teams:
	this_team_info = v.getTeams(team=this_team_number)[0]
	ranking = v.getRankings(sku=event_sku, team=this_team_number)[0]
	print("%s %s has ranking %s (%s-%s-%s, %s WP, %s AP, %s SP)" %
		(this_team_info["number"], this_team_info["team_name"], ranking["rank"], ranking["wins"], 
			ranking["losses"], ranking["ties"], ranking["wp"], ranking["ap"], ranking["sp"]))














