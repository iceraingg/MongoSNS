from user import *
from posts import *
from comment import *
from likes import *
import re

def getOtherPosts(db,userid):
    followings = db.users.find_one({"user_id":userid},\
                                    {"_id":0, "followings":1})['followings']
    posts = db.post.find({"user_id":{"$in":followings}})\
            .sort([("post_time",-1)])
    post_ids = []
    while True:
        for i in range(5):
            obj = next(posts, None)
            if obj: 
                post_ids.append(obj['_id'])
                print("post_id : ",obj['_id'],'\n'
                    "id : ",obj['user_id'],'\n'
                    "name : ",obj["name"], '\n'
                  "post_time : ",obj["post_time"],'\n'  
                  "title : ",obj["post_title"], '\n'
                  "text : ",obj["post_text"],'\n'
                  "comment : ",len(obj["comments"]), '\n'
                  "like : ",len(obj["likes"]), '\n'
                  "hashtags : ",obj['hashtags'], '\n')
            else:
                print("{:^49}".format("---No more posts to display---"))                
                while True:
                    print('-'*49)
                    print("""
{:^49}
{:^49}
{:^49}
{:^49}
{:^49}
{:^49}
                    """.format("<CHOOSE YOUR MENU>","1. See comment","2. Write comment",
                               "3. Add like","4. Cancel like","Exit"))
                    print('-'*49)

                    choice = input("Your choice? :")
                    if choice == '1':
                        while True:
                            post_id = input("Enter post_id you want to see comments (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    see_comment(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")

                    elif choice == '2':
                        while True:
                            post_id = input("Enter post_id you want to write comments (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    write_comment(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")
                    elif choice == '3':
                        while True:
                            post_id = input("Enter post_id you want to add like (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    add_like(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")
                    elif choice == '4':
                        while True:
                            post_id = input("Enter post_id you want to cancel like (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    cancel_like(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")
                    else:
                        print("{:^49}".format("Exit My Newsfeed"))
                        break
                break
        if obj:
            cont = input("Enter 'next' if you want to continue: ")
            if re.match(r'next',cont,re.IGNORECASE):
                continue
            else:
                while True:
                    print('-'*49)
                    print("""
{:^49}
{:^49}
{:^49}
{:^49}
{:^49}
{:^49}
                    """.format("<CHOOSE YOUR MENU>","1. See comment","2. Write comment",
                               "3. Add like","4. Cancel like","Exit"))
                    print('-'*49)

                    choice = input("Your choice? :")
                    if choice == '1':
                        while True:
                            post_id = input("Enter post_id you want to see comments (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    see_comment(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")

                    elif choice == '2':
                        while True:
                            post_id = input("Enter post_id you want to write comments (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    write_comment(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")
                    elif choice == '3':
                        while True:
                            post_id = input("Enter post_id you want to add like (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    add_like(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")
                    elif choice == '4':
                        while True:
                            post_id = input("Enter post_id you want to cancel like (Enter q or Q to quit): ")
                            try: 
                                post_id = eval(post_id)
                                if post_id in post_ids:
                                    cancel_like(db, userid, post_id)
                                else:
                                    print("No such post on your current Newsfeed")
                            except:
                                if post_id == 'q' or post_id == 'Q':
                                    break
                                else:
                                    print("Wrong post_id! Please check again")
                    else:
                        print("{:^49}".format("Exit My Newsfeed"))
                        break        
        break
