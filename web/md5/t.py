import requests
from bs4 import BeautifulSoup
import hashlib

# requests.Session() keeps session open
session = requests.Session()
r = session.get('http://docker.hackthebox.eu:37818')
soup = BeautifulSoup(r.content, 'html.parser')
# print soup.prettify()
# print '\n'

# print type(soup.h3)
# convert bs4.element.tag to string type
headerFlag = str(soup.h3)

# isolate the string that needs to be encrypted with md5
unencryptedFlag = headerFlag.split('>')[1].split('<')[0]
# print hashedFlag

# use hashlib to create an md5 object
encFlag = hashlib.md5(unencryptedFlag).hexdigest()
print encFlag
print '\n'

#print r.headers
#print '\n'

# session.cookies returns a RequestsCookieJar object
print type(session.cookies)
print '\n'

# returns the cookies hash { 'PHPSESSID': 'abcd' } 
cookies = session.cookies.get_dict()
print cookies

# makes a post request to open session using cookie from earlier GET
# submits MD5 encrypted string to form
sender = session.post('http://docker.hackthebox.eu:37818', cookies=cookies, data={'hash':encFlag})
print sender.content
