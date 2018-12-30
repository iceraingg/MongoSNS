# hashtagPost.py

from pprint import pprint
import re

def findpost(db, user):
    hashtags = input("Enter hash tags (only one hash tag): ")
    posts = db.post.find({"$text":{"$search":hashtags}},
                         {"score":{"$meta":"textScore"}}).sort([("score",{"$meta":"textScore"})])
    while True:
        for i in range(5):
            obj = next(posts, None)
            if obj: 
                print("post_id : ",obj["_id"],'\n'
                  "post_time : ",obj["post_time"],'\n'
                  "title : ",obj["post_title"], '\n'
                  "text : ",obj["post_text"],'\n'
                  "comment : ",obj["comments"], '\n'
                  "like : ",obj["likes"], '\n'
                  "hashtags : ",obj["hashtags"])
            else:
                print("{:^49}".format("No more posts to display"))
                break
        if obj:
            cont = input("Enter 'next' if you want to continue: ")
            if re.match(r'next',cont,re.IGNORECASE):
                continue
            else:
                print("{:^49}".format("Exit Hashtag Search"))
                break
        break
