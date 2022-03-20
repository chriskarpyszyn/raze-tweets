import os
import time
from pathlib import Path
import twitter
from dotenv import load_dotenv

# todo move into a config file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token_key = os.getenv('ACCESS_TOKEN_KEY')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


def delete(api):
    # with open("tweets.csv") as file:
    count = 0

    # https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline
    # count is max 200, we'll just keep querying 200
    statuses = api.GetUserTimeline(count=200)
    while statuses.__len__() > 0:
        for status in statuses:
            try:
                print("Deleting tweet #{0}".format(status.id))
                api.DestroyStatus(status.id)
                count += 1
                time.sleep(0.5)
            except twitter.TwitterError as err:
                print("Exception: {0}\n".format(err.message))
        statuses = api.GetUserTimeline(count=200)

    print("Deleted {} tweets!".format(count))


def main():
    # TODO add args to restrict by date
    # TODO add args to restrict by replies and retweets only

    api = twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )

    delete(api)


if __name__ == "__main__":
    main()
