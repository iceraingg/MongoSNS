#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pymongo import MongoClient
from user import *
# from posts import *
# from wall import *
# from newsfeed import *

Client = MongoClient()
db = Client.sns
from pymongo import TEXT

def mainpage(db):
    '''
    call signup() or signin()
    '''
    while True:
        print("===========<MAIN PAGE>===========")
        print("1.Sign in\n2.Sign up\n3.Quit")
        sign = input("\tChoose number: ")
        if sign == '1': 
            signin(db)
        elif sign == '2':
            signup(db)
        elif sign == '3':
            break
        else:
            print('select again')

if __name__ == "__main__":
    '''
    call mainpage()
    '''
#     try:
#         db.post.create_index([("hashtags",TEXT)])
#     except:
#         print("Text index already exists")

    mainpage(db)

