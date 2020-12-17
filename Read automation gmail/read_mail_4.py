import imaplib
import email
from email.header import decode_header
import webbrowser
import os, sys

conn = imaplib.IMAP4_SSL("ssl0.ovh.net")

try:
    (retcode, capabilities) = conn.login("formation@novolinko.com", "F4ut31lS0l31l!")
except:
    print sys.exc_info()[1]
    sys.exit(1)

conn.select(readonly=1) # Select inbox or default namespace
(retcode, messages) = conn.search(None, '(UNSEEN)')
if retcode == 'OK':
    for num in messages[0].split(' '):
        print 'Processing :', message
        typ, data = conn.fetch(num,'(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        typ, data = conn.store(num,'-FLAGS','\\Seen')
        if ret == 'OK':
            print data,'\n',30*'-'
            print msg

conn.close()