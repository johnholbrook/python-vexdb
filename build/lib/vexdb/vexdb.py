"""Thin python wrapper for the VexDB API"""

import urllib, json

def _urlToJSON(url):
	"""Makes a request to the specfied URL and returns a list of results.
	"""
	if type(url) not in [type("string"), type(u'unicode string')]:
		raise TypeError("Parameter 'url' must be a string.")
	result = json.loads(urllib.urlopen(url).read())
	if (result["status"] == 1):
		return result["result"]
	else:
		raise RuntimeError("VexDB Server Error: %s" % result["error_text"])

def _urlToSize(url):
	"""Makes a request to the specfied URL and returns the number of results.
	
	Useful mostly when making calls with the 'nodata' perameter set to true.
	"""
	if type(url) not in [type("string"), type(u'unicode string')]:
		raise TypeError("Parameter 'url' must be a string.")
	result = json.loads(urllib.urlopen(url).read())
	if (result["status"] == 1):
		return result["size"]
	else:
		raise RuntimeError("VexDB Server Error: %s" % result["error_text"])

def _buildParams(userInput):
	""" Takes a dictionary of user-inputted paramaters, where the keys are the names
	of the parameters in the URL and the values are either None or the value of the parameters
	in the URL."""
	params = "?"
	for key, value in userInput.items():
		if value != None:
			params += "%s=%s&" % (key, value)
	return params


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
	params = _buildParams({"nodata":"true", "sku":sku, "program":program, "date":date, "season":season,
	"city":city, "region":region, "country":country, "team":team, "status":status})

	return _urlToSize("https://api.vexdb.io/v1/get_events%s" % params)

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
	params = _buildParams({"sku":sku, "program":program, "date":date, "season":season,
	"city":city, "region":region, "country":country, "team":team, "status":status})

	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_events%s" % params)
	else:
		num_events = getNumEvents(sku, program, date, season, city, region, country, team, status)
		result = []
		current = 0
		while (current < num_events):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_events%s" % this_params)
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
	params = _buildParams({"nodata":"true", "team":team, "program":program, "organisation":organisation,
		"city":city, "region":region, "country":country, "grade":grade, "is_registered":is_registered,
		"sku":sku})

	return _urlToSize("https://api.vexdb.io/v1/get_teams%s" % params)
				
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
	params = _buildParams({"team":team, "program":program, "organisation":organisation,
		"city":city, "region":region, "country":country, "grade":grade, "is_registered":is_registered,
		"sku":sku})
		
	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_teams%s" % params)
	else:
		num_teams = getNumTeams(team, program, organisation, city, region, country, grade, is_registered, sku)
		result = []
		current = 0
		while (current < num_teams):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_teams%s" % this_params)
			current += 2000
		return result
	
	
def getNumMatches(sku=None,
				  division=None,
				  round=None,
				  instance=None,
				  matchnum=None,
				  scheduled=None,
				  field=None,
				  team=None,
				  scored=None,
				  season=None):
	"""Return the number of matches matching the given criteria"""
	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves
	params = _buildParams({"nodata":"true", "sku":sku, "division":division, "round":round, "instance":instance,
		"matchnum":matchnum, "scheduled":scheduled, "field":field, "team":team, "scored":scored, "season":season})

	return _urlToSize("https://api.vexdb.io/v1/get_matches%s" % params)
	
def getMatches(sku=None,
			   division=None,
			   round=None,
			   instance=None,
			   matchnum=None,
			   scheduled=None,
			   field=None,
			   team=None,
			   scored=None,
			   season=None,
			   get_all=False):
	"""Return a list of matches matching the given criteria.
	
	For sets of criteria that match a large number of matches (a few thousand or so),
	a single request to the API will return only a limited number of results.
	Passing get_all=True will ensure that all matching matches are returned by making 
	multiple requests if necessary.
	"""
	#build list of parameters to specify
	params = _buildParams({"sku":sku, "division":division, "round":round, "instance":instance,
		"matchnum":matchnum, "scheduled":scheduled, "field":field, "team":team, "scored":scored, "season":season})

	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_matches%s" % params)
	else:
		num_matches = getNumMatches(sku, division, round, instance, matchnum, scheduled, field, team, scored, season)
		result = []
		current = 0
		while (current < num_matches):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_matches%s" % this_params)
			current += 2000
		return result
	
def getNumRankings(sku=None,
				   division=None,
				   rank=None,
				   team=None,
				   season=None):
	"""Return the number of rankings matching the given criteria"""

	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves
	params = _buildParams({"nodata":"true", "sku":sku, "rank":rank, "team":team, "season":season})
		
	return _urlToSize("https://api.vexdb.io/v1/get_rankings%s" % params)
	
def getRankings(sku=None,
				division=None,
				rank=None,
				team=None,
				season=None,
				get_all=False):
	"""Return a list of rankings matching the given criteria.
	
	For sets of criteria that match a large number of rankings (a few thousand or so),
	a single request to the API will return only a limited number of results.
	Passing get_all=True will ensure that all matching rankings are returned by making 
	multiple requests if necessary.
	"""

	params = _buildParams({"sku":sku, "rank":rank, "team":team, "season":season})
	
	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_rankings%s" % params)
	else:
		num_rankings = getNumRankings(sku, division, rank, team, season)
		result = []
		current = 0
		while (current < num_rankings):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_rankings%s" % this_params)
			current += 2000
		return result
	
def getNumSeasonRankings(program=None,
						 season=None,
						 team=None,
						 vrating_rank=None):
	"""Return the number of season rankings matching the given criteria"""
	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves

	params = _buildParams({"nodata":"true", "program":program, "season":season, 
		"team":team, "vrating_rank":vrating_rank})
	
	return _urlToSize("https://api.vexdb.io/v1/get_season_rankings%s" % params)
	
def getSeasonRankings(program=None,
						 season=None,
						 team=None,
						 vrating_rank=None,
						 get_all=False):
	"""Return a list of season rankings matching the given criteria.
	
	For sets of criteria that match a large number of season rankings (a few thousand or so),
	a single request to the API will return only a limited number of results.
	Passing get_all=True will ensure that all matching season rankings are returned by making 
	multiple requests if necessary.
	"""
	
	#build list of parameters to specify
	params = _buildParams({"program":program, "season":season, "team":team, "vrating_rank":vrating_rank})
	
	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_season_rankings%s" % params)
	else:
		num_season_rankings = getNumSeasonRankings(sku, division, rank, team, season)
		result = []
		current = 0
		while (current < num_season_rankings):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_season_rankings%s" % this_params)
			current += 2000
		return result
	
def getNumAwards(sku=None,
				 name=None,
				 team=None,
				 season=None):
	"""Return the number of season rankings matching the given criteria"""
	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves

	params = _buildParams({"nodata":"true", "sku":sku, "name":name, "team":team, "season":season})

	return _urlToSize("https://api.vexdb.io/v1/get_awards%s" % params)
	
def getAwards(sku=None,
			  name=None,
			  team=None,
			  season=None,
			  get_all=False):
	"""Return a list of awards matching the given criteria.
	
	For sets of criteria that match a large number of awards (a few thousand or so),
	a single request to the API will return only a limited number of results.
	Passing get_all=True will ensure that all matching awards are returned by making 
	multiple requests if necessary.
	"""
	
	#build list of parameters to specify
	params = _buildParams({"sku":sku, "name":name, "team":team, "season":season})

	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_awards%s" % params)
	else:
		num_awards = getNumAwards(sku, name, team, season)
		result = []
		current = 0
		while (current < num_awards):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_awards%s" % this_params)
			current += 2000
		return result
	
def getNumSkills(sku=None,
				 program=None,
				 type=None,
				 team=None,
				 season=None,
				 season_rank=None,
				 rank=None):
	"""Return the number of skills records matching the given criteria"""
	#build list of parameters to specify
	#'nodata=true' tells the API to return the number of results
	#rather than the results themselves
	
	params = _buildParams({"nodata":"true", "sku":sku, "program":program, "type":type, "team":team,
		"season":season, "season_rank":season_rank, "rank":rank})
	
	return _urlToSize("https://api.vexdb.io/v1/get_skills%s" % params)
	
def getSkills(sku=None,
			  program=None,
			  type=None,
			  team=None,
			  season=None,
			  season_rank=None,
			  rank=None,
			  get_all=False):
	"""Return a list of skills records matching the given criteria.
	
	For sets of criteria that match a large number of skills records (a few thousand or so),
	a single request to the API will return only a limited number of results.
	Passing get_all=True will ensure that all matching skills records are returned by making 
	multiple requests if necessary.
	"""
	#build list of parameters to specify
	params = _buildParams({"sku":sku, "program":program, "type":type, "team":team,
		"season":season, "season_rank":season_rank, "rank":rank})
	
	if not get_all:
		return _urlToJSON("https://api.vexdb.io/v1/get_skills%s" % params)
	else:
		num_skills = getNumSkills(sku, program, type, team, seacon, season_rank, rank)
		result = []
		current = 0
		while (current < num_skills):
			this_params = params + ("limit_start=%s&limit_number=2000" % current)
			result += _urlToJSON("https://api.vexdb.io/v1/get_skills%s" % this_params)
			current += 2000
		return result
	
		