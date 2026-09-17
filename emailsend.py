import smtplib
from email.message import EmailMessage
msg=EmailMessage()
msg["subject"]="proposal for gyarmi"
msg["from"]="shaikarifa5350@gmail.com"
msg["to"]="basireddysushma8@gmail.com"
msg.set_content("""
dear sushma,
greeting from affu...
welcome to gyarmi festival 
best regards,
affu
""")
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("shaikarifa5350@gmail.com","yyimrrewuxkqdmjc")
server.send_message(msg)
print("email send successfully")
server.quit()
