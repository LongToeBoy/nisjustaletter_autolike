import tweepy
import config
import time

def main():
    try:
        client=tweepy.Client(
            config.BEARER_TOKEN,
            config.API_KEY,
            config.API_SECRET,
            config.ACCESS_TOKEN,
            config.ACCESS_TOKEN_SECRET,
            wait_on_rate_limit=True
        )
        with open("tags.txt","r") as f:
            tags=[x.strip() for x in f]
    except Exception as e:
        print(e)
        exit()
    
    myId=client.get_me().data.id
    likedTweets=[liked.id for liked in client.get_liked_tweets(myId).data]
    print("Started autoliker for Nisjustaletter")
    print("To turn off program press Ctrl + Z and Ctrl + C")
    while(True):
        for tag in tags:
            tweets=client.search_recent_tweets(tag).data
            for tweet in tweets:
                if tweet.id in likedTweets:
                    continue
                client.like(tweet.id)
                likedTweets.append(tweet.id)
                print(f"tweet id:{tweet.id} liked")
                time.sleep(15*60/50)


if __name__ == "__main__":
    main()
