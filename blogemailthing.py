import imaplib2, email, quopri, re
#import pprint,  lxml
from bs4 import BeautifulSoup

num_test_msgs = 14

password = ""
with open('pwd_file.txt', 'r') as f:
    password = f.read()

imapObj = imaplib2.IMAP4_SSL("imap.gmail.com")
imapObj.login('exampleblogupdatingemail@gmail.com', password)
imapObj.select('INBOX')#, readonly=True)

#tmp, data = imapObj.search(None, 'ALL')
tmp, data = imapObj.search(None, 'UNSEEN')
for num in data[0].split():
        typ, email_data = imapObj.fetch(num, '(RFC822)')
        email_num = int(num) - num_test_msgs
        print('\nMessage: {0}\n'.format(email_num)) #label
        #pprint.pprint(email_data[0][1])
        # email_data[1] gets you a string with a closing parenthesis in it
        # email_data[0] gets you a tuple with [0] "5 (RFC822 {720}" and [1] email html
        

        #msg = email.message_from_string(email_data[0][1].decode())
        msg = email.message_from_bytes(email_data[0][1])
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                quoted_printables_regex = re.compile(r"=[0-9A-F][0-9A-F]")
                if len(quoted_printables_regex.findall(part.get_payload())) > 0:
                    if (part.get_payload().isascii()):
                        email_html = BeautifulSoup(quopri.decodestring(part.get_payload()), 'html.parser')
                    else:
                        print("not handled yet")
                else:
                    email_html = BeautifulSoup(part.get_payload(), 'html.parser')
                print(email_html.prettify())
                temp_file = open('priority-blog/articles/email-'+str(email_num)+'.html', 'w', encoding='utf-8')
                temp_file.write(email_html.prettify())
                temp_file.close()
        

if (len(data[0].split()) == 0):
    print('No unread emails found.')

imapObj.logout()













'''
        #some code i used for testing, was between comments and the line that starts msg =
        
        #email_html = BeautifulSoup(email_data[0][1], 'html.parser')
        #print(email_html.prettify())
        #email_content = email_html.div
        #print("\n")
        #print(email_content)
        
        if (int(num) == 6):
            print("hi")
            #pprint.pprint(email_data[0][1])
            email_html = BeautifulSoup(email_data[0][1], 'html.parser')
            print(email_html.prettify())
            print(email.message_from_string(email_data[0][1].decode()))
            print("bye")
'''


'''
HERE IS SOME STUFF IGNORE IT


UIDs = imapObj.search(['SINCE 04-Aug-2021'])
UIDs

rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])


import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')
message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)
'''
