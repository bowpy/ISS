import json
import urllib
import urllib.request

print("       _____   _____                _____   ______  ") 
print("      / ____| |  __ \      /\      / ____| |  ____| ")
print("     | (___   | |__) |    /  \    | |      | |__    ") 
print("      \___ \  |  ___/    / /\ \   | |      |  __|   ")
print("      ____) | | |       / ____ \  | |____  | |____  ") 
print("     |_____/  |_|      /_/    \_\  \_____| |______| ")

print("")
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
people = result['people']

print("There are currently", result['number'],"people in space")
for p in people:
    print("")
    print("- ",p['name'])

req = ("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)
result = json.loads(response.read())
print("")
print ("The space station is currently at Longitude:",result['iss_position']['longitude'], "and Latitude:",result['iss_position']['latitude'], "\nThis data was collected at the timestamp",result['timestamp'], "with the message:", result['message'])
