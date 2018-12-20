import urllib, json

def urlToJSON(url):
	if type(url) != type("string"):
		raise TypeError("Parameter 'url' must be a string.")
	return json.loads(urllib.urlopen(url).read())

def getEventBySKU(sku):
	if type(sku) != type("string"):
		raise TypeError("Parameter 'sku' must be a string.")
	result = urlToJSON("https://api.vexdb.io/v1/get_events?sku=%s" % sku)
	if result["status"] == 1:
		return result["result"]
	# else:
		#TODO: Raise the appropriate error

def getEventName(sku):
	if type(sku) != type("string"):
		raise TypeError("Parameter 'sku' must be a string.")
	try:
		return getEventBySKU(sku)[0]["name"]
	except 