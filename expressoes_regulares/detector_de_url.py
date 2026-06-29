from humre import *
import pyperclip
import re

site_url = re.compile(r'''(
                      http(s)?://
                      \S+
                      )''', re.VERBOSE)

# so preciso achar o final
