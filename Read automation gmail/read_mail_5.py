def getMsgs(servername="ssl0.ovh.net"):
  "formation@novolinko.com" = getpass.getuser()
  "F4ut31lS0l31l!" = getpass.getpass()
  subject = 'Your SSL Certificate'
  conn = imaplib.IMAP4_SSL(servername)
  conn.login(usernm,passwd)
  conn.select('Inbox')
  typ, data = conn.search(None,'(UNSEEN SUBJECT "%s")' % subject)
  for num in data[0].split():
    typ, data = conn.fetch(num,'(RFC822)')
    msg = email.message_from_string(data[0][1])
    typ, data = conn.store(num,'-FLAGS','\\Seen')
    yield msg

def getAttachment(msg,check):
  for part in msg.walk():
    if part.get_content_type() == 'application/octet-stream':
      if check(part.get_filename()):
        return part.get_payload(decode=1)

getMsgs()
print(getAttachment)