__author__ = 'thatcher'

from django import template
from base.utils import TwitterClient
import json
from django.core.cache import get_cache


cache = get_cache('database_cache')

# from django.core.urlresolvers import reverse
# import re

register = template.Library()

CONSUMER_KEY = 'aEtFq69wvzUAjlzwh9Tw'
CONSUMER_SECRET = 'o6mcmOLtp35loXfUbRBOVpyfzenFdOSwBV3jd4MMFSM'
TWEETS_LIST_TIMEOUT = 300  # Caching timeout in seconds
NUM_TWEETS = 60  # Total number of the tweets_list
USERS_LIST = ['rhashioka',  # List of users considered during the fetching process
              'docker',
              'julienbarbier42',
              'dhr_p',
              'golubbe']



# @register.tag(name="list_tweets")

@register.tag
def list_tweets(parser, token):
    """
    Fetch tweets from favorites list from the 'USERS_LIST'. The number of tweets from each user is split evenly among
    all the users -> int(NUM_TWEETS / len(USERS_LIST))

    ~rogaha
    """
    nodelist = parser.parse(('end_list_tweets',))
    parser.delete_first_token()
    tweets = TweetNode(nodelist)
    return tweets

class TweetNode(template.Node):
    def __init__(self, nodelist):
        self.twitter_client = TwitterClient(CONSUMER_KEY, CONSUMER_SECRET)

    def render(self, context):

        html = ""
        num_tweets_per_user = int(NUM_TWEETS / len(USERS_LIST))

        try:

            tweets_list = cache.get(CONSUMER_KEY)

            if tweets_list is None:
                tweets_list = []
                for screen_name in USERS_LIST:
                    user_tweets_list = json.loads(self.twitter_client.request(
                    'https://api.twitter.com/1.1/favorites/list.json?count={0}&screen_name={1}'.format(
                        num_tweets_per_user,
                        screen_name)))
                    tweets_list.extend(user_tweets_list)
                cache.set(CONSUMER_KEY, tweets_list, TWEETS_LIST_TIMEOUT)

            for data in tweets_list:
                html += """
                <div class="tweet" onClick="window.open('http://twitter.com/{2}/status/{4}/')" >
                    <img src="{0}">
                    <span class="username">{1}</span>
                    <span class="handle" ><a onClick="window.open('http://twitter.com/{2}'); event.preventDefault();" href="https://twitter.com/{2}/" title="users twitter page">@{2}</a></span>
                    <p><span class="text">{3}</span></p>
                </div>

                """.format(
                    data['user']['profile_image_url'].replace("http://a0", "https://si0").replace("http://abs", "https://abs"),
                    data['user']['name'].encode('utf-8').strip(),
                    data['user']['screen_name'].encode('utf-8').strip(),
                    data['text'].encode('utf-8').strip(),
                    data['id']
                )
        except:
            html = "oops.. we failed to get some tweets from the api, but believe us, it's all good. :-)"

        return html