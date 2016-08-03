#!/usr/bin/python
import json
from urllib2 import urlopen

url = 'https://shraddha12.atlassian.net/rest/api/2/status' #url with json
response = urlopen(url) #
string = str(response.read())
data = json.loads(string)
#string = '[{"self":"https://shraddha12.atlassian.net/rest/api/2/status/3","description":"This issue is being actively worked on at the moment by the assignee.","iconUrl":"https://shraddha12.atlassian.net/images/icons/statuses/inprogress.png","name":"In Progress","id":"3","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10000","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"To Do","id":"10000","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/2","id":2,"key":"new","colorName":"blue-gray","name":"To Do"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10001","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"In Review","id":"10001","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10002","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"Done","id":"10002","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/3","id":3,"key":"done","colorName":"green","name":"Done"}}]'
# print response 

def parsing(parsed_json):

	format = '['

	for i in range(len(parsed_json)):

		format += '{"list": [{"listItem": ' + parsed_json[i]['id'] + " : " + parsed_json[i]['id'] + '},'  

	format += ']}'

	output = json.dumps(format)

	return output

parsing(data)