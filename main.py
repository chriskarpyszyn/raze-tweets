import twitter
import os
from pathlib import Path
from dotenv import load_dotenv

# todo move into a config file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token_key = os.getenv('ACCESS_TOKEN_KEY')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


def delete(api):
    with open("tweets.csv") as file:
        count = 0

        #for each row, get tweet id and delete
        count += 1

    print("Deleted {} tweets!".format(count))

def main():
    # TODO use environment variables / .env file
    print("hello world")
    api = twitter.Api(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )


if __name__ == "__main__":
    main()
