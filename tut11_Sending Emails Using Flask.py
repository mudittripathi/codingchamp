# email kaise bhjna hai
# powershell me pip install flask-mail
# documentation
#
# from flask_mail import Mail
# usk bad
# app.config.update(
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = '465',
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = ''
#     MAIL_PASSWORD = ''


# )   (gmail id ki help se email bhjna)
#
# mail send krne ke lie ek function hota hai mail.send_message
# mail = Mail(app)
#
# commit krne ke bad email send krunga
# mail.send_message('New message from' + name,
#                   sender = email,
#                   recipients = [params[hotmail_user]],
#                   body = message + '\n' + phone )
