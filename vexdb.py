"""Thin python wrapper for the VexDB API"""

import urllib, json

def urlToJSON(url):
	"""Makes a request to the specfied URL and returns a list of results.
	"""
	if type(url) != type("string"):
		raise TypeError("Parameter 'url' must be a string.")
	result = json.loads(urllib.urlopen(url).read())
	if (result["status"] == 1):
		return result["result"]
	else:
		raise RuntimeError("VexDB Server Error: %s" % result["error_text"])

def urlToSize(url):
	"""Makes a request to the specfied URL and returns the number of results.
	
	Useful mostly when making calls with the 'nodata' perameter set to true.
	"""
	if type(url) != type("string"):
		raise TypeError("Parameter 'url' must be a string.")
	result = json.loads(urllib.urlopen(url).read())
	if (result["status"] == 1):
		return result["size"]
	else:
		raise RuntimeError("VexDB Server Error: %s" % result["error_text"])

def getNumEvents(sku=None,
			 	 program=None,
			 	 date=None,
			 	 season=None,
				 city=None,
				 region=None,
				 country=None,
				 team=None,
				 status=None):
	"""Return the number of events matching the given criteria.
	"""
	
	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves
	params = "?nodata=true&"
	if (sku != None):
		params += "sku=%s&" % sku
	if (program != None):
		params += "program=%s&" % program
	if (date != None):
		params += "date=%s&" % date
	if (season != None):
		params += "season=%s&" % season
	if (city != None):
		params += "city=%s&" % city
	if (region != None):
		params += "region=%s&" % region
	if (country != None):
		params += "country=%s&" % country
	if (team != None):
		params += "team=%s&" % team
	if (status != None):
		params += "status=%s&" % status

	return urlToSize("https://api.vexdb.io/v1/get_events%s" % params)

def getEvents(sku=None,
			 program=None,
			 date=None,
			 season=None,
			 city=None,
			 region=None,
			 country=None,
			 team=None,
			 status=None,
			 get_all=False):
	"""Return a list of events matching the given criteria.
	
	For sets of criteria that match a large number of events (a few thousand or so),
	a single request to the API will return only a limited number of events.
	Passing get_all=True will ensure that all matching events are returned by making 
	multiple requests if necessary.
	"""
	#build list of parameters to specify
	params = "?"
	if (sku != None):
		params += "sku=%s&" % sku
	if (program != None):
		params += "program=%s&" % program
	if (date != None):
		params += "date=%s&" % date
	if (season != None):
		params += "season=%s&" % season
	if (city != None):
		params += "city=%s&" % city
	if (region != None):
		params += "region=%s&" % region
	if (country != None):
		params += "country=%s&" % country
	if (team != None):
		params += "team=%s&" % team
	if (status != None):
		params += "status=%s&" % status

	if not get_all:
		return urlToJSON("https://api.vexdb.io/v1/get_events%s" % params)
	else:
		num_events = getNumEvents(sku, program, date, season, city, region, country, team, status)
		result = []
		current = 0
		while (current < num_events):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += urlToJSON("https://api.vexdb.io/v1/get_events%s" % this_params)
			current += 2000
		return result

def getNumTeams(team=None,
				program=None,
				organisation=None,
				city=None,
				region=None,
				country=None,
				grade=None,
				is_registered=None,
				sku=None):
	"""Return the number of teams matching the given criteria"""
	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves
	params = "?nodata=true&"
	if team != None:
		params += "team=%s&" % team
	if program != None:
		params += "program=%s&" % program
	if organisation != None:
		params += "organisation=%s&" % organisation
	if city != None:
		params += "city=%s&" % city
	if region != None:
		params += "region=%s&" % region
	if country != None:
		params += "country=%s&" % country
	if grade != None:
		params += "grade=%s&" % grade
	if is_registered != None:
		params += "is_registered=%s&" % is_registered
	if sku != None:
		params += "sku=%s&" % sku
		
	return urlToSize("https://api.vexdb.io/v1/get_teams%s" % params)
				
def getTeams(team=None,
			 program=None,
			 organisation=None,
			 city=None,
			 region=None,
			 country=None,
			 grade=None,
			 is_registered=None,
			 sku=None,
			 get_all=False):
	"""Return a list of teams matching the given criteria.
	
	For sets of criteria that match a large number of teams (a few thousand or so),
	a single request to the API will return only a limited number of results.
	Passing get_all=True will ensure that all matching teams are returned by making 
	multiple requests if necessary.
	"""
	#build list of parameters to specify
	params = "?"
	if team != None:
		params += "team=%s&" % team
	if program != None:
		params += "program=%s&" % program
	if organisation != None:
		params += "organisation=%s&" % organisation
	if city != None:
		params += "city=%s&" % city
	if region != None:
		params += "region=%s&" % region
	if country != None:
		params += "country=%s&" % country
	if grade != None:
		params += "grade=%s&" % grade
	if is_registered != None:
		params += "is_registered=%s&" % is_registered
	if sku != None:
		params += "sku=%s&" % sku
		
	if not get_all:
		return urlToJSON("https://api.vexdb.io/v1/get_teams%s" % params)
	else:
		num_teams = getNumTeams(team, program, organisation, city, region, country, grade, is_registered, sku)
		result = []
		current = 0
		while (current < num_teams):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += urlToJSON("https://api.vexdb.io/v1/get_teams%s" % this_params)
			current += 2000
		return result
				
				
				
				
				
				
				
				
				
				