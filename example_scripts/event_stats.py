#calculates and displays various statistics foskur
#a user-specified VRC event

from __future__ import print_function
import vexdb as v

this_event_sku = raw_input("Enter event SKU: ")
this_event = v.getEvents(sku=this_event_sku)[0]
this_event_season = this_event["season"]

# print("Event Statistics for %s:" % this_event["name"])
print(this_event["name"])
print("Held %s at %s" % (this_event["start"][:10], this_event["loc_venue"]))

num_teams = 