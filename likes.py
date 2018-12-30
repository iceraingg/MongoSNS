def add_like(db, userid, post_id):
    db.post.update({"_id":post_id},{"$addToSet":{"likes":userid}})
    print("You liked this post")

def cancel_like(db, userid, post_id):
    db.post.update({"_id":post_id},{"$pull":{"likes":userid}})
    print("You disliked this post")
