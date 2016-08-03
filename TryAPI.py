import urllib2
import json 

locu_api = '60b8d25b6e0b3c834aac7252fe7957ecd213c7b6'
url = 'https://jira.atlassian.com/rest/api/2/issue/JRA-9/worklog'
json_obj = urllib2.urlopen(url)

datq = json.load(json_obj)

print datq

