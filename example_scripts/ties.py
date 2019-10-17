# Calculates the frequency of tied matches at events in WV in each of the last two seasons.

from __future__ import print_function
import vexdb as v

wv_tp_events = v.getEvents(season="Turning Point", region="West Virginia")
wv_itz_events = v.getEvents(season="In The Zone", region="West Virginia")

tp_matches = 0
tp_ties = 0
for event in wv_tp_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tp_matches += 1
		if match["redscore"] == match["bluescore"]:
			tp_ties += 1

itz_matches = 0
itz_ties = 0
for event in wv_itz_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		itz_matches += 1
		if match["redscore"] == match["bluescore"]:
			itz_ties += 1

print("In The Zone: %s ties from %s matches (%s %%)" % (itz_ties, itz_matches, (100.0*float(itz_ties)/itz_matches)))
print("Turning Point: %s ties from %s matches (%s %%)" % (tp_ties, tp_matches, (100.0*float(tp_ties)/tp_matches)))