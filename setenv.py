import os
import json


def GetAndSetEnv():
    isOnline = os.environ.get('ONLINE_MODE')
    if isOnline is None:
        file = open('local_data.json')
        loc_data = json.loads(file.read())
        
        os.environ['USER'] = loc_data['USER']
        os.environ['PASSWORD'] = loc_data['PASSWORD']
        os.environ['SECRET'] = loc_data['SECRET']
        os.environ['RUN_TIME'] = loc_data['RUN_TIME']
        os.environ['LATITUDE'] = loc_data['LATITUDE']
        os.environ['LONGITUDE'] = loc_data['LONGITUDE']

    print(isOnline)

