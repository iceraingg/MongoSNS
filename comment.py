# comment.py

from datetime import datetime
from pprint import pprint
import re

def see_comment(db, userid, post_id):
    try:
        res = db.post.find_one({"_id":post_id},{"comments":1})["comments"]
        pprint(res)
        write = input("Do you want to write comments? (Press y/Y if you want to): ")
        if write == 'y' or write == 'Y':
            write_comment(db, userid, post_id)
    except:
        print("Wrong post_id! Check again")

def write_comment(db, userid, post_id):
    try:
        res = list(db.post.aggregate([
            {"$match":{"_id":post_id}},
            {"$unwind":"$comments"},
            {"$sort":{"comments.id":-1}},
            {"$limit":1}]))
        if res == []:
            comment_id = 0
        else:
            comment_id = res[0]['comments']['id']+1
        
        comment = input("Write your comment: ")
        db.post.update({"_id":post_id}, {"$push":{"comments":{"id":comment_id, "user_id":userid, "text":comment, "time":datetime.now()}}})
        print("Your comment has been successfully published")
    except:
        print("Wrong post_id. Check Again")

def delete_comment(db, userid, post_ids, comment_ids):
    try:
        post_id = eval(input("Enter post_id : "))
        comment_id = eval(input("Enter comment_id : "))
        if (post_id, comment_id) in zip(post_ids, comment_ids):
            db.post.update({"_id":post_id},
                           {"$pull":{"comments":{"id":comment_id,"user_id":userid}}})
        else:
            print("no such comment")
    except:
        print("Check your post_id or comment_id")

def edit_comment(db, userid, post_ids, comment_ids):
    try:
        post_id = eval(input("Enter post_id : "))
        comment_id = eval(input("Enter comment_id : "))
        if (post_id, comment_id) in zip(post_ids, comment_ids):
            text = input("Enter your comment : ")
            db.post.update({"_id":post_id},
                           {"$pull":{"comments":{"id":comment_id,"user_id":userid}}})
            db.post.update({"_id":post_id},
                            {"$push":{"comments":{"id":comment_id,"user_id":userid,"text":text}}})
        else:
            print("no such comment")
    except:
        print("Check your post_id or comment_id")
#     try:
#         post_id = int(input("Enter post_id : "))
#         comment_id = int(input("Enter comment_id : "))
        
        

def manageComment(db, userid):
    print("=============<{:^21s}>=============".format("MANAGE COMMENT"))
    comments = db.post.aggregate([
        {"$match":{"comments.user_id":userid}},
        {"$unwind":"$comments"},
        {"$match":{"comments.user_id":userid}},
        {"$sort":{"post_id":1,"comments.id":1}}])
    post_ids = []
    comment_ids = []
    while True:
        for i in range(5):
            obj = next(comments, None)
            if obj: 
                post_ids.append(obj['_id'])
                comment_ids.append(obj['comments']["id"])
                print("post_id : ",obj['_id'])
                pprint(obj['comments'])
                print()
                      
#                     "comments : ",obj['comments'],'\n')
            else:
                print("{:^49}".format("---No more comments to display---"))
                break
        print('-'*49)
        print("""
{:^49}
{:^49}
{:^49}
{:^49}
{:^49}
        """.format("<CHOOSE YOUR MENU>","1. Delete comment","2. Edit comment","3. Next","Exit"))
        print('-'*49)
        choice = input("Your choice: ")
        if choice == '1':
            delete_comment(db, userid,post_ids, comment_ids)
            break
        elif choice == '2':
            edit_comment(db, userid,post_ids, comment_ids)
            break
        elif choice == '3':
            continue
        else:
            print("{:^49}".format("Exit Comment Management"))
            break