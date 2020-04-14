#!/usr/bin/env python

import re

if __name__ == "__main__":
    content = open('setup.py').read()
    pattern = re.compile('version="(.*)"')
    matches = pattern.search(content)
    if matches and len(matches.groups()) >= 1:
        version = matches.group(1)
        print(version)
