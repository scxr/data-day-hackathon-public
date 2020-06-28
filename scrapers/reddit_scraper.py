import json,requests, praw
def reddit_scrape(username):
    try:
        reddit = praw.Reddit(client_id='redacted',client_secret='redacted',user_agent='testscript by /u/GoldArrow997')
        redditor = reddit.redditor(username)
        data = {}
        data["created"] = redditor.created_utc
        data["verified"] = redditor.has_verified_email
        data["pfp_url"] = redditor.icon_img
        data["premium"] = redditor.is_gold
        data["name"] = redditor.name
        data["comment_karma"] = redditor.comment_karma
        data['url'] = f'https://reddit.com/u/{redditor.name}'
        return data
    except:
        return "User not found"
