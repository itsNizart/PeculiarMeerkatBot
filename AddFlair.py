import praw

reddit = praw.Reddit(
    client_id="[CLIENT ID]",
    client_secret="[CLIENT SECRET]",
    user_agent="[USER AGENT]",
    username="[USERNAME]",
    password="[PASSWORD]",
    check_for_async=False
)


count = 1

for contributor in reddit.subreddit("PeculiarMeerkatLair").contributor(limit=5000):
    if contributor != "PeculiarMeerkat":
        count += 1

number = count
for contributor in reddit.subreddit("PeculiarMeerkatLair").contributor(limit=5000):
    if contributor != "PeculiarMeerkat":
        number -= 1
        print(str(contributor)+" = "+str(number))
        reddit.subreddit("PeculiarMeerkatLair").flair.set(contributor, str(number), css_class="number")
