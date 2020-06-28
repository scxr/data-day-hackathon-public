from pyyoutube import Api
from pprint import pprint
from dateutil import parser
import re
def get_channel_info(username):
    api = Api(api_key='redacted')
    channel_by_name = api.get_channel_info(channel_name=username)
    try:
        response = channel_by_name.items[0].to_dict()
    except:
        return 'User doesnt exist'
    channel_name = response["snippet"]["localized"]["title"]
    created_at = response["snippet"]["publishedAt"]
    pfp_url = response["snippet"]["thumbnails"]["default"]["url"]
    view_count = response["statistics"]["viewCount"]
    subscribers = response["statistics"]["subscriberCount"]
    video_count = response["statistics"]["videoCount"]
    userid = response["id"]
    description = response["brandingSettings"]["channel"]["description"]
    match = re.findall(r'[\w\.-]+@[\w\.-]+', str(description))
    if len(match)>0:
        emails = ','.join(match)
    else:
        emails = "None found"
    data = {"name":channel_name,
            "created_at":parser.parse(created_at).timestamp(),
            "pfp_url":pfp_url,
            "total_views":view_count,
            "subsribers":subscribers,
            "video_count":video_count,
            "userid":userid,
            "emails":emails,
            "url": f'https://www.youtube.com/channel/{userid}'}
    return data
