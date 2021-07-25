import praw
import time
import math

reddit = praw.Reddit(
    client_id="[CLIENT ID]",
    client_secret="[CLIENT SECRET]",
    user_agent="[USER AGENT]",
    username="[USERNAME]",
    password="[PASSWORD]",
    check_for_async=False
)

survivors = []

for comment in reddit.subreddit("PeculiarMeerkatLair").comments(limit=10000):
    if time.time()-comment.created_utc > 604800:
        break
    print(str(comment.author)+" -- "+str(math.floor(time.time()-comment.created_utc)))
    print("")
    if comment.author not in survivors:
        survivors.insert(-1, comment.author)

for submission in reddit.subreddit("PeculiarMeerkatLair").new(limit=10000):
    if time.time()-submission.created_utc > 604800:
        break
    print(str(submission.author)+" -- "+str(math.floor(time.time()-submission.created_utc)))
    print("")
    if submission.author not in survivors:
        survivors.insert(-1, submission.author)

for survivor in survivors:
    print(survivor)

print(len(survivors))
print("\n")

#The Message is printed out into the console and is needed to be posted manually.
#The Standard Message would be:
#
#  Title: Goodbye!
#  Body: <The Printed Content after "The following have been cleansed due to inactivity:">

message = "The following have been cleansed due to inactivity:\n"

death_count = 0
for contributor in reddit.subreddit("PeculiarMeerkatLair").contributor(limit=5000):
    if contributor not in survivors:
        flair = next(reddit.subreddit("PeculiarMeerkatLair").flair(str(contributor)))
        message = message+str(flair["flair_text"])+" : "+str(contributor)+"\n"
        reddit.subreddit("PeculiarMeerkatLair").contributor.remove(contributor)
        death_count += 1
        print("processing:"+str(death_count))

print(message)

