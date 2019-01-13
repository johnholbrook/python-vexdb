#Finds the qualifying ranking instances with the
#best-ever WP, AP, SP, OPR, DPR, and CCWM

#Not too useful to compare most of these metrics across seasons since
#the average match score changes lots from game to game. But kinda
#fun to see this info nonetheless.

from __future__ import print_function
import vexdb as v

num_rankings = v.getNumRankings()
print("Getting data for all %s rankings" % num_rankings)
all_rankings = v.getRankings(get_all=True)
# all_rankings = v.getRankings(season="In The Zone")

first = all_rankings[0]

best_wp = first["wp"]
best_wp_data = first

best_ap = first["ap"]
best_ap_data = first

best_sp = first["sp"]
best_sp_data = first

best_opr = first["opr"]
best_opr_data = first

best_dpr = first["dpr"]
best_dpr_data = first

best_ccwm = first["ccwm"]
best_ccwm_data = first

for ranking in all_rankings[1:]:
	if ranking["wp"] > best_wp:
		best_wp = ranking["wp"]
		best_wp_data = ranking

	if ranking["ap"] > best_ap:
		best_ap = ranking["ap"]
		best_ap_data = ranking

	if ranking["sp"] > best_sp:
		best_sp = ranking["sp"]
		best_sp_data = ranking

	if ranking["opr"] > best_opr:
		best_opr = ranking["opr"]
		best_opr_data = ranking

	if ranking["dpr"] < best_dpr: #lower DPR is better
		best_spr = ranking["dpr"]
		best_dpr_data = ranking

	if ranking["ccwm"] > best_ccwm:
		best_ccwm = ranking["ccwm"]
		best_ccwm_data = ranking

wp_event = v.getEvents(sku=best_wp_data["sku"])[0]
wp_team = v.getTeams(team=best_wp_data["team"])[0]
print("Highest WP: %s by %s %s at %s (%s)" % (best_wp, best_wp_data["team"], wp_team["team_name"], wp_event["name"], wp_event["start"][:10]))

ap_event = v.getEvents(sku=best_ap_data["sku"])[0]
ap_team = v.getTeams(team=best_ap_data["team"])[0]
print("Highest AP: %s by %s %s at %s (%s)" % (best_ap, best_ap_data["team"], ap_team["team_name"], ap_event["name"], ap_event["start"][:10]))

sp_event = v.getEvents(sku=best_sp_data["sku"])[0]
sp_team = v.getTeams(team=best_sp_data["team"])[0]
print("Highest SP: %s by %s %s at %s (%s)" % (best_sp, best_sp_data["team"], sp_team["team_name"], sp_event["name"], sp_event["start"][:10]))

opr_event = v.getEvents(sku=best_opr_data["sku"])[0]
opr_team = v.getTeams(team=best_opr_data["team"])[0]
print("Highest OPR: %s by %s %s at %s (%s)" % (best_opr, best_opr_data["team"], opr_team["team_name"], opr_event["name"], opr_event["start"][:10]))

dpr_event = v.getEvents(sku=best_dpr_data["sku"])[0]
dpr_team = v.getTeams(team=best_dpr_data["team"])[0]
print("Lowest DPR: %s by %s %s at %s (%s)" % (best_dpr, best_dpr_data["team"], dpr_team["team_name"], dpr_event["name"], dpr_event["start"][:10]))

ccwm_event = v.getEvents(sku=best_ccwm_data["sku"])[0]
ccwm_team = v.getTeams(team=best_ccwm_data["team"])[0]
print("Highest CCWM: %s by %s %s at %s (%s)" % (best_ccwm, best_ccwm_data["team"], ccwm_team["team_name"], ccwm_event["name"], ccwm_event["start"][:10]))














