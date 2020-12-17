#!/usr/bin/env python3
import imaplib
import base64
import os
import email

server = imaplib.IMAP4_SSL('imap.gmail.com')
server.login('documentio.novolinko@gmail.com', 'D0cum3nt10!')
# Print list of mailboxes on server
code, mailboxes = server.list()
for mailbox in mailboxes:
    print(mailbox.decode("utf-8"))
# Select mailbox
server.select("INBOX")

type, data = server.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

i = len(data[0].split())
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = server.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8', 'ignore')
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            print(body)

for num in data[0].split():
    typ, data = server.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8', 'ignore')
    # print(raw_email_string)
    email_message = email.message_from_string(raw_email_string)
    # print(email_message)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            if False:
                # Attention ! Il y a des virus dans les PJ des mails
                filePath = os.path.join('./', fileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            # print(f'Downloaded "{fileName}" from email titled "{subject}".')

# Cleanup
server.close()