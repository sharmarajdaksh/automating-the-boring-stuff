import sys
import webbrowser
import pyperclip
import re

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

address.replace('/', '\/')

webbrowser.open('https://www.google.com/maps/place/' + address)

