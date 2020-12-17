import imaplib
import email
from email.header import decode_header
import webbrowser
import os, sys


# def findUnreadMail():
#   for subeject in SUBJECTS:


# account credentials
username = "formation@novolinko.com"
password = "F4ut31lS0l31l!"

# create an IMAP4 class with SSL, use your email provider's IMAP server
imap = imaplib.IMAP4_SSL("ssl0.ovh.net")
# authenticate
imap.login(username, password)

# select a mailbox (in this case, the inbox mailbox)
# use imap.list() to get the list of mailboxes

imap.select("INBOX")
# (retcode, messages) = conn.search(None, '(UNSEEN)')

# OK (status, messages) = imap.search(None, '(UNSEEN)')

# SUBJECTS = '(SUBJECT "demande de renseignements")'
(status, messages) = imap.search(None, '(SUBJECT "demande de renseignements")','(UNSEEN)')

bytoint = str(messages[0]).split(" ")

frist_unread_message = ""
last_unread_message = ""
messages_not_read = []

for split in bytoint:
    if split == bytoint[0]:
        if len(bytoint) == 1:
            for letter in bytoint[0][2:-1]:
                frist_unread_message+= letter
        else:
            for letter in bytoint[0][2:]:
                frist_unread_message+= letter
        messages_not_read.append(frist_unread_message)

    elif split == bytoint[len(bytoint)-1]:
        for letter in bytoint[len(bytoint)-1][0:-1]:
            last_unread_message+= letter
        messages_not_read.append(last_unread_message)
    else:
        messages_not_read.append(split)

print(messages_not_read)

if messages_not_read == ['']:
    print("There is no mail to process, close the program")
    sys.exit(0)
    

for i in messages_not_read:
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    
    for response in msg:

        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
            # email sender
            from_ = msg.get("From")
            print("Subject:", subject)
            print("From:", from_)
            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        print(body)
                    elif "attachment" in content_disposition:
                        # download attachment
                        filename = part.get_filename()
                        if filename:
                            if not os.path.isdir(subject):
                                # make a folder for this email (named after the subject)
                                os.mkdir(subject)
                            filepath = os.path.join(subject, filename)
                            # download attachment and save it
                            open(filepath, "wb").write(part.get_payload(decode=True))
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    print(body)
            try:
                if content_type == "text/html":
                    # if it's HTML, create a new HTML file and open it in browser
                    if not os.path.isdir(subject):
                        # make a folder for this email (named after the subject)
                        os.mkdir(subject)
                    filename = f"{subject[:50]}.html"
                    filepath = os.path.join(subject, filename)
                    # write the file
                    open(filepath, "w").write(body)
                    # open in the default browser
                    webbrowser.open(filepath)
            except:
                "ouverture d'un message html refusé"

    imap.store(i, '+FLAGS', '(SEEN)')
    print("="*100)


# close the connection and logout
imap.close()
imap.logout()