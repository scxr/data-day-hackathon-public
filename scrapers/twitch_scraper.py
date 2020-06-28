import requests, json
def twtich_scrape(username):
    headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': 'redacted',
    }

    params = (
        ('login', username),
    )

    response = requests.get('https://api.twitch.tv/kraken/users', headers=headers, params=params)
    resp_json = json.loads(response.content)
    if 'error' in resp_json or resp_json["_total"] == 0:
        return "User not found"
    useful_resp = resp_json["users"][0]
    data = {}
    data['name'] = useful_resp["display_name"]
    data['bio'] = useful_resp["bio"]
    data['pfp_url'] = useful_resp["logo"]
    data['id'] = useful_resp["_id"]
    data['url'] = f'https://www.twitch.tv/{username}'
    return data
