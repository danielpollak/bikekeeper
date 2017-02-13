#!/usr/bin/python


import sys 
# Access command line arguments with sys.argv[n], n=0 is script name
# $ python test.py arg1 arg2 arg3
# Argument List: ['test.py', 'arg1', 'arg2', 'arg3']
# browser.open(sys.argv[1]) could be useful
import json
from subprocess import call
from robobrowser import RoboBrowser

browser = RoboBrowser()

browser.open('http://api.openweathermap.org/data/2.5/forecast/city?id=%s&APPID=%s' % (sys.argv[1], sys.argv[2]))
print browser.find
if not browser.find.__str__().__contains__('error'):
	fullhtml=browser.find('p') # json should be between the paragraph tags.
	content=str(fullhtml)[3:-4] # need to chop and screw to get <p>json</p> to be json
	myjson=json.loads(content)

	# myjson['list'] # returns list item from dictionary key u'list', referred to as 'list'
	# this is confusingly a list of dictionaries.
	# myjson['list'][INDEX] INDEX is the forcast. so every three hours there is another INDEX. returns a dict.
	# myjson['list'][INDEX]['dt_txt'] returns something like u'2017-02-13 09:00:00'
	precip = False
	weatherSet = set()

	for i in range(8):
		weather = myjson['list'][i]['weather'][0]['description']

		# Can be clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow, mist
		mylambda = lambda input: weather.__contains__(input)
		if mylambda('rain') or mylambda('thunder') or mylambda('snow') or mylambda('mist'):
			precip = True
			weatherSet.add(weather)


	prettySet = ', '.join(weatherSet) # formatted set for printing
	print prettySet
	call(["notify-send", "Bicycle-unfriendly precipitation alert", "%s is predicted in the next day, make sure your bike is safe" % prettySet])

 
			

else:
	call(["notify-send", "Scrape error", "There was an error with your scrape.py function"])
