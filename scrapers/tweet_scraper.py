from twitter_scraper import Profile

def twitter_scrape(username):
    try:
        profile = Profile(username)
        data = profile.to_dict()
        data['pfp_url'] = data.pop('profile_photo')
        data['website'] = 'https://' + data['website'] if data['website'] else ''
        data['url'] = f'https://twitter.com/{username}'
        data.pop('username')
        return data
    except:
        return "User not found"
    # return profile.to_dict()