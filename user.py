# user.py

from posts import *
from wall import *
from newsfeed import *
from hashtagPost import *
from follow import *
from comment import *

def signup(db):
    users = db.users
    '''
    1. Get his/her information.
    '''
    user_id = input("Enter your ID: ")
    '''
    3. Check if the userid already exists.
    '''

    while True: 
        if not user_id.split():
            user_id = input("Enter your ID: ")
        elif users.find_one({"user_id":user_id}):
            user_id = input("Redundant. Enter another ID: ")
        else:
            break
    pw = input("Enter your password: ")
    
    while True:
        if not pw.split():
            pw = input("Enter your PW: ")
        else:
            break
    '''
    2. Check if his/her password is equal. Confirm the password.
    '''
    while True:
        check_pw = input("Check your password: ")
        if not check_pw.split():
            continue
        if check_pw == pw:
            break
    '''
    4. Make the user document.
    '''
    name = input("Insert your name: ")
    profile = input('Insert your profile: ')
    user = ({"user_id":user_id,"pw":pw,"profile":profile,"name":name,"followers":[],"followings":[], 'blacklist':[]})
    '''
    5. Insert the document into users collection.
    '''
    try: 
        users.insert_one(user)
        print("Thank you for signing up!")
    except:
        print("Failed to sign up. Try again please")
    
def signin(db):
    users = db.users
    '''
    1. Get his/her information.
    '''
    user_id = input("Enter your ID: ")
    pw = input("Enter your pw: ")
    '''
    2. Find him/her in users collection.
    '''
    users = db.users
    doc = users.find_one({"user_id":user_id,"pw":pw})
    '''
    3. If exists, print welcome message and call userpage()
    '''
    if doc:
        print("WELCOME FIRA!!")
        userpage(db, user_id)
    else:
        print("Please Check Again")
        
def mystatus(db, user):
    users = db.users
    '''
    print user profile, # followers, and # followings
    '''
    
    doc = users.find_one({"user_id":user})
    print("""=============<{:^21s}>=============
    MY PROFILE: {}
    # Followers: {}
    # Followings: {}""".format("MY STATUS",doc['profile'],len(doc['followers']),len(doc['followings'])))
    
#     print("MY PROFILE:", doc['profile'])
#     print("# Followers:", len(doc['followers']))
#     print("# Followings:", len(doc['followings']))

def userpage(db, user):
    '''
    user page
    '''
    
    while True:
        print("="*49)
        print("=============<{:^21s}>=============".format("USER PAGE"))
        print("1. MY STATUS\n2. NEWSFEED\n3. WALL\n4. POST\n5. FOLLOW\n6. UNFOLLOW\n7. HASHTAG SEARCH\n8. MANAGE COMMENT\n9. Blacklist\n10.LOGOUT\n")
        click = input("Enter Menu Number: ")
        print("="*49)
        if click == '1':
            mystatus(db, user)
            continue
        elif click == '2':
            getOtherPosts(db, user)
            continue
        elif click == '3':
            try:
                getPosts(db, user)
            except Exception as e:
                print(e)
                continue
        elif click == '4':
            try:
                postInterface(db, user)
            except Exception as e:
                print(e)
                continue
        elif click == '5':
            follow(db, user)
        elif click == '6':
            unfollow(db, user)
        elif click == '7':
            findpost(db, user)
            continue
        elif click == '8':
            manageComment(db, user)
            continue
        elif click == '9':
            manageBlack(db,user)
            continue
        elif click == '10':
            break
         
        else:
            print("Check Again Please")

