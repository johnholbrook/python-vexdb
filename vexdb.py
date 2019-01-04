import urllib, json

def urlToJSON(url):
	if type(url) != type("string"):
		raise TypeError("Parameter 'url' must be a string.")
	result = json.loads(urllib.urlopen(url).read())
	if (result["status"] == 1):
		return result["result"]
	else:
		raise RuntimeError("VexDB Server Error: %s" % result["error_text"])

def getEvent(sku=None,
			 program=None,
			 date=None,
			 season=None,
			 city=None,
			 region=None,
			 country=None,
			 team=None,
			 status=None):
	#check for correct  

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

	# print "https://api.vexdb.io/v1/get_events%s" % params
	try:
		return urlToJSON("https://api.vexdb.io/v1/get_events%s" % params)
	except Exception as e:
		print e
		raise
	# event = urlToJSON("https://api.vexdb.io/v1/get_events%s" % params)


def getEventBySKU(sku):
	if type(sku) != type("string"):
		raise TypeError("Parameter 'sku' must be a string.")
	try:
		return urlToJSON("https://api.vexdb.io/v1/get_events?sku=%s" % sku)[0]
	except Exception as e:
		print e
	
def getEventName(sku):
	if type(sku) != type("string"):
		raise TypeError("Parameter 'sku' must be a string.")
	try:
		return getEventBySKU(sku)["name"]
	except Exception as e:
		print e