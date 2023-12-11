# get data from api
def get_data():
    import requests 
    
    res = requests.get("https://randomuser.me/api/")
    res = res.json() # printing this gives results and info
    res = res['results'][0] # meanwhile we only need the result
    return res


def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    return data

def stream_data():
    import json
    res = get_data()
    res = format_data(res)
    print(json.dumps(res, indent=3))
    
    
stream_data()