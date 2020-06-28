import requests, json, datetime
def toconv(time):
    date = datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')
    return date
def so_scraper(username):
    try:
        to_fetch = f'https://api.stackexchange.com/2.2/users?order=desc&sort=reputation&inname={username}&site=stackoverflow'
        r = requests.get(to_fetch)
        user = json.loads(r.content)
        main_user = user["items"][0]
        data = {}
        data['creation_date'] = toconv(main_user["creation_date"])
        data["username"] = main_user["display_name"]
        data["reputation"] = main_user["reputation"]
        data["profile_link"] = main_user["link"]
        data["profile_picture"] = main_user["profile_image"]
        data["user_id"] = main_user["user_id"]
        data["website_url"] = main_user["website_url"]
        data['url'] = f'https://stackoverflow.com/users/{main_user["user_id"]}/{username}'
        return data
    except:
        return("User is not found")
