# Calculates the frequency of tied matches at events worldwide from Sack Attach to Tower Takeover

from __future__ import print_function
import vexdb as v

print("WARNING: This script looks at every match from the last 8 season, it will take a while!")

tt_events = v.getEvents(season="Tower Takeover", get_all=True, region="West Virginia")
tt_matches = 0
tt_ties = 0
for event in tt_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tt_matches += 1
		if match["redscore"] == match["bluescore"]:
			tt_ties += 1
if tt_matches != 0:
    print("Tower Takeover: %s ties from %s matches (%s %%)" % (tt_ties, tt_matches, (100.0*float(tt_ties)/tt_matches)))
else:
    print("No matches for Tower Takeover")

tp_events = v.getEvents(season="Turning Point", get_all=True, region="West Virginia")
tp_matches = 0
tp_ties = 0
for event in tp_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tp_matches += 1
		if match["redscore"] == match["bluescore"]:
			tp_ties += 1
if tp_matches != 0:
    print("Turning Point: %s ties from %s matches (%s %%)" % (tp_ties, tp_matches, (100.0*float(tp_ties)/tp_matches)))
else:
    print("No matches for Turning Point")

itz_events = v.getEvents(season="In The Zone", get_all=True, region="West Virginia")
itz_matches = 0
itz_ties = 0
for event in itz_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		itz_matches += 1
		if match["redscore"] == match["bluescore"]:
			itz_ties += 1
if itz_matches != 0:
    print("In The Zone: %s ties from %s matches (%s %%)" % (itz_ties, itz_matches, (100.0*float(itz_ties)/itz_matches)))
else:
    print("No matches for In the Zone")

ss_events = v.getEvents(season="Starstruck", get_all=True, region="West Virginia")
ss_matches = 0
ss_ties = 0
for event in ss_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		ss_matches += 1
		if match["redscore"] == match["bluescore"]:
			ss_ties += 1
if ss_matches != 0:
    print("Starstruck: %s ties from %s matches (%s %%)" % (ss_ties, ss_matches, (100.0*float(ss_ties)/ss_matches)))
else:
    print("No matches for Starstruck")

nbn_events = v.getEvents(season="Nothing But Net", get_all=True, region="West Virginia")
nbn_matches = 0
nbn_ties = 0
for event in nbn_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		nbn_matches += 1
		if match["redscore"] == match["bluescore"]:
			nbn_ties += 1
if nbn_matches != 0:
    print("Nothing But Net: %s ties from %s matches (%s %%)" % (nbn_ties, nbn_matches, (100.0*float(nbn_ties)/nbn_matches)))
else:
    print("No matches for Nothing But Net")

sr_events = v.getEvents(season="Skyrise", get_all=True, region="West Virginia")
sr_matches = 0
sr_ties = 0
for event in sr_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		sr_matches += 1
		if match["redscore"] == match["bluescore"]:
		    sr_ties += 1
if sr_matches != 0:
    print("Skyrise: %s ties from %s matches (%s %%)" % (sr_ties, sr_matches, (100.0*float(sr_ties)/sr_matches)))
else:
    print("No matches for Skyrise")

tu_events = v.getEvents(season="Toss Up", get_all=True, region="West Virginia")
tu_matches = 0
tu_ties = 0
for event in tu_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tu_matches += 1
		if match["redscore"] == match["bluescore"]:
			tu_ties += 1
if tu_matches != 0:
    print("Toss Up: %s ties from %s matches (%s %%)" % (tu_ties, tu_matches, (100.0*float(tu_ties)/tu_matches)))
else:
    print("No matches for Toss Up")

sa_events = v.getEvents(season="Sack Attack", get_all=True, region="West Virginia")
sa_matches = 0
sa_ties = 0
for event in sa_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		sa_matches += 1
		if match["redscore"] == match["bluescore"]:
			sa_ties += 1
if sa_matches != 0:
    print("Sack Attack: %s ties from %s matches (%s %%)" % (sa_ties, sa_matches, (100.0*float(sa_ties)/sa_matches)))
else:
    print("No matches for Sack Attack")
