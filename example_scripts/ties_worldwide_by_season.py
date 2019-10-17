# Calculates the frequency of tied matches at events worldwide from Sack Attach to Tower Takeover

from __future__ import print_function
import vexdb as v

print("WARNING: This script looks at every match from the last 8 season, it will take a while!")

tt_events = v.getEvents(season="Tower Takeover", get_all=True)
tt_matches = 0
tt_ties = 0
for event in tt_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tt_matches += 1
		if match["redscore"] == match["bluescore"]:
			tt_ties += 1
print("Tower Takeover: %s ties from %s matches (%s %%)" % (tt_ties, tt_matches, (100.0*float(tt_ties)/tt_matches)))

tp_events = v.getEvents(season="Turning Point", get_all=True)
tp_matches = 0
tp_ties = 0
for event in tp_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tp_matches += 1
		if match["redscore"] == match["bluescore"]:
			tp_ties += 1
print("Turning Point: %s ties from %s matches (%s %%)" % (tp_ties, tp_matches, (100.0*float(tp_ties)/tp_matches)))

itz_events = v.getEvents(season="In The Zone", get_all=True)
itz_matches = 0
itz_ties = 0
for event in itz_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		itz_matches += 1
		if match["redscore"] == match["bluescore"]:
			itz_ties += 1
print("In The Zone: %s ties from %s matches (%s %%)" % (itz_ties, itz_matches, (100.0*float(itz_ties)/itz_matches)))

ss_events = v.getEvents(season="Starstruck", get_all=True)
ss_matches = 0
ss_ties = 0
for event in ss_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		ss_matches += 1
		if match["redscore"] == match["bluescore"]:
			ss_ties += 1
print("Starstruck: %s ties from %s matches (%s %%)" % (ss_ties, ss_matches, (100.0*float(ss_ties)/ss_matches)))

nbn_events = v.getEvents(season="Nothing But Net", get_all=True)
nbn_matches = 0
nbn_ties = 0
for event in nbn_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		nbn_matches += 1
		if match["redscore"] == match["bluescore"]:
			nbn_ties += 1
print("Nothing But Net: %s ties from %s matches (%s %%)" % (nbn_ties, nbn_matches, (100.0*float(nbn_ties)/nbn_matches)))

sr_events = v.getEvents(season="Skyrise", get_all=True)
sr_matches = 0
sr_ties = 0
for event in sr_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		sr_matches += 1
		if match["redscore"] == match["bluescore"]:
		    sr_ties += 1
print("Skyrise: %s ties from %s matches (%s %%)" % (sr_ties, sr_matches, (100.0*float(sr_ties)/sr_matches)))

tu_events = v.getEvents(season="Toss Up", get_all=True)
tu_matches = 0
tu_ties = 0
for event in tu_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		tu_matches += 1
		if match["redscore"] == match["bluescore"]:
			tu_ties += 1
print("Toss Up: %s ties from %s matches (%s %%)" % (tu_ties, tu_matches, (100.0*float(tu_ties)/tu_matches)))

sa_events = v.getEvents(season="Sack Attack", get_all=True)
sa_matches = 0
sa_ties = 0
for event in sa_events:
	matches = v.getMatches(sku=event["sku"])
	for match in matches:
		sa_matches += 1
		if match["redscore"] == match["bluescore"]:
			sa_ties += 1
print("Sack Attack: %s ties from %s matches (%s %%)" % (sa_ties, sa_matches, (100.0*float(sa_ties)/sa_matches)))