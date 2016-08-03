#!/usr/bin/python
import json
from urllib2 import urlopen

url = 'http://finance.google.com/finance/info?client=ig&q=NASDAQ:NTDOY' #url with json
response = urlopen(url) 
#print type(response.read())
#print response.read()
string = str(response.read())
#print string
new_string = string.replace("/", "")
#print new_string
#print new_string
#print string
data = json.loads(new_string)
#print type(data)
#print data

#string = '[{"self":"https://shraddha12.atlassian.net/rest/api/2/status/3","description":"This issue is being actively worked on at the moment by the assignee.","iconUrl":"https://shraddha12.atlassian.net/images/icons/statuses/inprogress.png","name":"In Progress","id":"3","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10000","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"To Do","id":"10000","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/2","id":2,"key":"new","colorName":"blue-gray","name":"To Do"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10001","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"In Review","id":"10001","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10002","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"Done","id":"10002","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/3","id":3,"key":"done","colorName":"green","name":"Done"}}]'
# print response 


def parsing(parsed_json):


 	for i in range(len(parsed_json)):

 		last_price = parsed_json[i]["l"]
 		last_price_str = str(last_price)
 		# print type(last_price_str)
# 		#year_high_str = str(year_high)
# 		#print year_high
# 		#year_low = parsed_json['list']['resources'][0]['resource']['fields']['year_low']
# 		#year_low_str = str(year_low)
# 		#print year_low
		
 	format = '{ "x-axis": { "labels": ["last_price"] }, "y_axis": { "unit": "USD" , "format": "currency"}, "series": [{"data":[' + last_price + ']}]}'
 	
 	print type(format)
 	# print json.dumps(format)

parsing(data)

#     #new = str(format)
# 		#print type(new)
# 		#unquoted = urllib.unquote(format)
# 	#output = json.dumps(format)
# 	#print output
# 	#print type(format)