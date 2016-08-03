#!/usr/bin/python
import json
from urllib2 import urlopen

url = 'http://finance.yahoo.com/webservice/v1/symbols/COALINDIA.NS/quote?format=json&view=detail' #url with json
response = urlopen(url) 
string = str(response.read())
data = json.loads(string)
#string = '[{"self":"https://shraddha12.atlassian.net/rest/api/2/status/3","description":"This issue is being actively worked on at the moment by the assignee.","iconUrl":"https://shraddha12.atlassian.net/images/icons/statuses/inprogress.png","name":"In Progress","id":"3","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10000","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"To Do","id":"10000","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/2","id":2,"key":"new","colorName":"blue-gray","name":"To Do"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10001","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"In Review","id":"10001","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10002","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"Done","id":"10002","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/3","id":3,"key":"done","colorName":"green","name":"Done"}}]'
# print response 

def parsing(parsed_json):


	for i in range(len(parsed_json)):

		format = '{"x-axis": { "labels": ["year high", "year low"]}, "y_axis": {"format": "currency", "unit": "USD"}, "series": [{"data": [' + parsed_json['list']['resources'][0]['resource']['fields']['year_high'] + ',' + parsed_json['list']['resources'][0]['resource']['fields']['year_low'] + ']}]'


	output = json.dumps(format)

	return output

parsing(data)

