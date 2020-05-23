#python
print("Project by PRAHLAD SHUKLA")
import smtplib  
form email.mime.multipart import MIME Multipart
from email.mime.text import MIMETEXT
sender="thecyberkiddie@gmail.com"
receiver="shuklaprahlad414@gmail.com"
msg MIME Multipart()
msg ['TO']=receiver
msg ['FROM']=sender
msg ['SUBJECT']='HTML MESSAGE'
html="""
<h1><u><I><b align="center">this is html message</h1></u></I></b></align>
msg.attach(MIME Text(html,'html'))
server=smtplib.SMTP(smtp.gmail.com,587)

