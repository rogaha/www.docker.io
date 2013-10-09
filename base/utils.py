import base64
import urllib2
import json
from django.core.cache import get_cache


cache = get_cache('database_cache')

API_ENDPOINT = 'https://api.twitter.com'
API_VERSION = '1.1'
REQUEST_TOKEN_URL =  '%s/oauth2/token' % API_ENDPOINT
REQUEST_RATE_LIMIT = '%s/%s/application/rate_limit_status.json' % (API_ENDPOINT, API_VERSION)
TWEETS_LIST_KEY = 'cache_key'
TWEETS_LIST_TIMEOUT = 300  # Caching timeout in seconds
NUM_TWEETS = 60  # Total number of the tweets_list
USERS_LIST = ['rhashioka',  # List of users considered during the fetching process
              'docker',
              'julienbarbier42',
              'dhr_p',
              'golubbe']


class ClientException(Exception):
    pass


class TwitterClient(object):
    """This class implements the Twitter's Application-only authentication."""

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = ''

    def request(self, url):
        """Send an authenticated request to the Twitter API."""
        if not self.access_token:
            self.access_token = self._get_access_token()

        request = urllib2.Request(url)
        request.add_header('Authorization', 'Bearer %s' % self.access_token)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            raise ClientException

        return response.read()

    def rate_limit_status(self):
        """Returns a dict of rate limits by resource."""
        json_response = self.request(REQUEST_RATE_LIMIT)
        return json.loads(json_response)

    def _get_access_token(self):
        """Obtain a bearer token."""
        encoded_bearer_token = base64.b64encode('%s:%s' % (self.consumer_key, self.consumer_secret))
        request = urllib2.Request(REQUEST_TOKEN_URL)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')
        request.add_header('Authorization', 'Basic %s' % encoded_bearer_token)
        request.add_data('grant_type=client_credentials')

        response = urllib2.urlopen(request)
        data = json.load(response)
        return data['access_token']

    def render_tweets_list(self):
        """
        Fetch tweets from favorites list from the 'USERS_LIST'. The number of tweets from each user is split evenly among
        all the users -> int(NUM_TWEETS / len(USERS_LIST))

        ~rogaha
        """
        html = ""
        num_tweets_per_user = int(NUM_TWEETS / len(USERS_LIST))

        try:

            tweets_list = cache.get(TWEETS_LIST_KEY)

            if tweets_list is None:
                tweets_list = []
                for screen_name in USERS_LIST:
                    user_tweets_list = json.loads(self.request(
                    'https://api.twitter.com/1.1/favorites/list.json?count={0}&screen_name={1}'.format(
                        num_tweets_per_user,
                        screen_name)))
                    tweets_list.extend(user_tweets_list)
                    cache.set(TWEETS_LIST_KEY, tweets_list, TWEETS_LIST_TIMEOUT)

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