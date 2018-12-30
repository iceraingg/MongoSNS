#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load post.py
from datetime import *
from user import *
from wall import *
from newsfeed import *
from comment import *

def postInterface(db, user):

    while True:
        print("=============<{:^21s}>=============".format("POST"))
        print("1. Insert post\n2. DeletePost\n3. Exit\n")

        click = input("\tEnter Post Menu Number: ")
        if click == '1':
            insertPost(db, user)
        elif click == '2':
            deletePost(db, user)
        elif click == '3':
            break
        else:
            print('select again')
            # go main page
    
    """
    Implementing the interface to post your text.
    There are three or more items to choose functions such as inserting and deleting a text.
    """

def insertPost(db, userid):
    print("=============<{:^21s}>=============".format("INSERT POST"))
    users = db.users
    post = db.post
    username = users.find_one({'user_id': userid})['name']

    if len(list(post.find())) != 0:
        last_post_id = list(post.find().sort([('_id', -1)]))[0]['_id']
    else:
        last_post_id = 0
        
    while True:
        post_time = datetime.now()
        post_title = input('Type in Post Title : ')
        post_text = input('Write down your context : ')

        if len(list(post.find())) != 0:
            last_post_id = list(post.find().sort([('_id', -1)]))[0]['_id']
        else:
            last_post_id = 0
        
        while True:
            double_check = input('Are you sure to want to insert(y/n) : ').lower()

            if double_check =='y':
                hashtags = []
                temp = list(map(lambda x: x.split(), post_text.split('#')))[1:]
                for t in temp:
                    try: 
                        hashtags.append(t[0])
                    except:
                        continue
                post.insert_one({'_id': last_post_id+1,'user_id' : userid, 
                                 'name' : username, 
                                 'post_time' : post_time,'post_title' : post_title, 
                                 'post_text' : post_text, 'likes': [], 'comments':[],
                                 'hashtags' : hashtags})
                print('post inserted')
                break
            elif double_check =='n':
                break
            else:
                print('please check again')
            
        cont = input("Continue?(Press y if you wnat to continue): ").lower()
        if cont == 'y':
            continue
        else:
            break

    """
    Insert user's text. You should create the post schema including,
    for example, posting date, posting id or name, and comments.
    
    You should consider how to delete the text.
    """
	

def deletePost(db, userid):
    
    post = db.post
    comment = db.comment
    getPosts(db,userid)
    print("=============<{:^21s}>=============".format("DELETE POST"))
    while True:
        try:
            delete = eval(input('Post id to delete(int) : '))
            double_check = input('Are you sure to delete(y/n) : ').lower()
            delete1 = post.find({'_id' : delete})
        except:
            print('input correct post_id')
        
        if len(list(delete1)) == 0:
            print('there are no post')
            break
            
        else:
            if double_check == 'y':
                post.delete_one({'_id': delete})
                comment.delete_one({'post_id':delete})
                print('post deleted')
                break

            else:
                break

    """
    Delete user's text.
    With the post schema, you can remove posts by some conditions that you specify.
    """

    """
    Sometimes, users make a mistake to insert or delete their text.
    We recommend that you write the double-checking code to avoid the mistakes.
    """

