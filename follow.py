# follow.py

from user import *
from pprint import pprint

def follow(db, userid):
    print("=============<{:^21s}>=============".format("Follow"))
    users = db.users
    following = users.find_one({'user_id': userid})['followings']
    if following:
        print('Your follow list')
        pprint(following)
    else:
        print('You are not following anyone')
        
    fol = input("Input id to follow : ")
    check = users.find_one({'user_id':fol})
    if check:
        if check['user_id'] in following:
            print('you already followed')
        else:
            b_check = list(users.find({'user_id': fol, 'blacklist': userid}))
            if len(b_check) == 0:
                users.update_one({'user_id':userid}, {'$addToSet':{'followings':fol}})
                users.update_one({'user_id':fol},{'$addToSet':{'followers':userid}})
                print('Follow completed')
            else:
                print('You are blocked')

    else:
        print('there is no such id')
    
        
"""
This function updates information that is user's followers
or followings.
 Note that if a user asks following to someone, the
follower's information should be also updated.
 Remember, you may regard duplicates and the situation
that the follower does not exists.
"""
        
def unfollow(db, userid):
    print("=============<{:^21s}>=============".format("Unfollow"))
    users = db.users
    unfollowing = users.find_one({'user_id': userid})['followings']
    if unfollowing:
        print('Your follow list')
        pprint(unfollowing)
    else:
        print('You are not following anyone')
        return
        
    unfol = input("Input id to unfollow : ")

    if unfol in unfollowing:
        users.update_one({'user_id':userid}, {'$pull':{'followings':unfol}})
        users.update_one({'user_id':unfol},{'$pull':{'followers':userid}})
        print('Unfollow completed')
    else:
        print("No such id on your following list")

        
def manageBlack(db, userid):
    print("=============<{:^21s}>=============".format("BLACKLIST MANAGEMENT"))
    print("-"*49)
    print("""
    
{:^49}
{:^49}
{:^49}
{:^49}

""".format("<CHOOSE YOUR MENU>","1. ADD BLACKLIST","2. CANCEL BLACKLIST","EXIT"))
    print("-"*49)
    while True:
        blackmenu = input('Your choice : ')
        if blackmenu == '1':
            blacklist(db,userid)
            break
        elif blackmenu == '2':
            unblack(db,userid)
            break
        else:
            break

def blacklist(db, userid):
    print("=============<{:^21s}>=============".format("Blacklist"))
    users = db.users
    black_check = users.find_one({'user_id':userid})['blacklist']
    print("Your black list : ", black_check)
   
    black = input('ID to add on your black list (\\n: quit): ')
    
    if black == '':
          print("Quit")
    else:
        user_check = users.find_one({'user_id':black})
        if not user_check:
            print('No such userid')
        elif black in black_check:
            print('Already Blacked')
        else:
            users.update_one({'user_id':userid}, {'$addToSet' :{'blacklist': black}})

            if users.find({'user_id': black, 'followings':userid}):
                users.update_one({'user_id':black}, {'$pull': {'followings': userid}})
            print('complete')
            
        
def unblack(db, userid):
    print("=============<{:^21s}>=============".format("UnBlacklist"))
    users = db.users
    black_check = users.find_one({'user_id':userid}, {'blacklist':1, '_id':0})['blacklist']
    print("Your Blacklist : ",list(black_check))
    
    unblack = input('Write ID to unblock (\\n:quit): ')
          
    if unblack == '':
          print("Quit")
    else:  
        if unblack in black_check:
            users.update_one({'user_id':userid}, {'$pull' :{'blacklist':unblack}})

        else: 
            print('Not on your blacklist')
