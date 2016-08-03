#!/usr/bin/python
import os
import json
from urllib2 import urlopen

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#


def get_reponse():

    url = 'http://finance.yahoo.com/webservice/v1/symbols/COALINDIA.NS/quote?format=json&view=detail' #url with json
    response = urlopen(url) 
    string = str(response.read())
#print string
    data = json.loads(string)
    parsing(data)

#print type(data)
#print data

#string = '[{"self":"https://shraddha12.atlassian.net/rest/api/2/status/3","description":"This issue is being actively worked on at the moment by the assignee.","iconUrl":"https://shraddha12.atlassian.net/images/icons/statuses/inprogress.png","name":"In Progress","id":"3","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10000","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"To Do","id":"10000","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/2","id":2,"key":"new","colorName":"blue-gray","name":"To Do"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10001","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"In Review","id":"10001","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/4","id":4,"key":"indeterminate","colorName":"yellow","name":"In Progress"}},{"self":"https://shraddha12.atlassian.net/rest/api/2/status/10002","description":"","iconUrl":"https://shraddha12.atlassian.net/","name":"Done","id":"10002","statusCategory":{"self":"https://shraddha12.atlassian.net/rest/api/2/statuscategory/3","id":3,"key":"done","colorName":"green","name":"Done"}}]'
# print response 


def parsing(parsed_json):


    #for i in range(len(parsed_json)):

        #year_high = parsed_json['list']['resources'][0]['resource']['fields']['year_high']
        #year_high_str = str(year_high)
        #print year_high
        #year_low = parsed_json['list']['resources'][0]['resource']['fields']['year_low']
        #year_low_str = str(year_low)
        #print year_low
        
    format = '''{ "x-axis": { "labels": ["year high", "year low"] }, "y_axis": { "unit": "USD" , "format": "currency"}, "series": [{"data":[ 45 , 50 ]}]}'''
        
    return format


def application(environ, start_response):

    ctype = 'text/plain'
    if environ['PATH_INFO'] == '/health':
        response_body = "1"
    elif environ['PATH_INFO'] == '/env':
        response_body = ['%s: %s' % (key, value)
                    for key, value in sorted(environ.items())]
        response_body = '\n'.join(response_body)
    else:
        ctype = 'text/html'
        response_body = get_response()

        status = '200 OK'
        response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
                #
        start_response(status, response_headers)
    return [response_body]

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()