import argparse
import json
from snscrape.modules.twitter import TwitterProfileScraper


def get_args():
    parser = argparse.ArgumentParser(description='Get tweets of a twitter profile')
    parser.add_argument('--username', '-u', type=str, required=True, help='Username of the twitter profile')
    parser.add_argument('--limit', '-l', type=int, default=10, help='Number of tweet to dump')
    return parser.parse_args()

def main():
    args = get_args()
    tweets = []


    for count, tweet in enumerate(TwitterProfileScraper(args.username).get_items()):
        if count > args.limit:
            break
        if not tweet.retweetedTweet:
            coordinates = None
            if tweet.coordinates is not None:
                coordinates = {
                    "latitude": tweet.coordinates.latitude,
                    "longitude": tweet.coordinates.longitude
                }
            tweet_json = {
                "username": tweet.user.username,
                "tweet_id": tweet.id,
                "date": tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
                "RT_count": tweet.retweetCount,
                "view_count": tweet.viewCount,
                "Coordinates": coordinates,
                "raw_content": tweet.rawContent,



            }
            tweets.append(tweet_json)


    with open('tweets.json', 'w') as file:
        json.dump(tweets, file, indent=10)



if __name__ == '__main__':
    main()
