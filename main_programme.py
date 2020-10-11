# An Application to Retrieve Latitude and Longitude Data of a Place from google API:

# Importing necessary Libraries(urllib, json, ssl).
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# My API Key is not enabled for billing But I can put my own API key here after enabling billing.
# api_key = 'AIzaSyC_JquO072WUxZ3Uft0UgAtr5g9qrI07Dg'

# Using another API key I found on Internet which is free
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# For ignoring SSL certificate errors.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Running a loop for accessing different locations in a single run.
while True:
    # Taking input from user.
    address = input('Enter location Name: ')   # Example Ann Arbor
    if len(address) < 1:
        break
    # Creating a dictionary with the location name for encoding
    parms = dict()
    parms['address'] = address

    if api_key is not False:
        parms['key'] = api_key

    # Now encoding the url and adding it with the service url
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)

    # Now requesting to open the url and save it to a variable. In this process we decode the data from UTF-8 to UNICODE.
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # We try to load the data and save it.
    try:
        js = json.loads(data)
    except:
        js = None

    # Checking the status or checking if there is any data to retrieve
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)   # Prints out an error.
        continue

    # If we want to print out the retrieved data
    #print(json.dumps(js, indent=4))   # re distribute the code with 4 times space indetation.

    # Now digging into the data and getting the necessary data(latitude and longitude).
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']

    # Printing the Latitude and Longitude:
    print('lat', lat, 'lng', lng)
    # Printing The address.
    location = js['results'][0]['formatted_address']
    print(location)
