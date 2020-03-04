# how to fetch post in your blog or how to post in your blog
#
# post nam ka ek table add ho chuki hai database me and kch data dal denge database me or ab use isse connect krna hai
# and then if else loop se hum wo data apne blog me disply kr skte hai
#
# what is slug?
# koi website ke url pe last me / ke bad jo likhahota hai hyphen krke eg:
# www.facebook.com/mudit-tripathi-videos-january
# to slash ke bad wala jo b hai wo slug kelata hai
# iske likhne ke rules hote hai
# alpha numeric chars
# - use kr skte h
# slug is varchar
#
#
# @app.route('/post/<string:post_slug>', methods=['GET'])
# def post():
#     return render_template('post.html', params=params)
#
# you have to write this way like above
#
# ab post ko fetch krte hai means database se uthate hai
# syntax = post = Posts.query.filter_by(slug=post_slug).first()   ek naam ke do post na ho
#
#
# post naam ke ek class b bnani padegi like humne contact ki bnai thi
#
# phr hum post.html me jake {{post.content}} sb datbase se fetch kr skte hai
#
#
#
