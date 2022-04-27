#!/usr/bin/env python3.10

## create a new form using the beaconstac api

import os
import sys

import httpx

from hardcoded_form import create_hardcoded_form

url = 'https://api.beaconstac.com/api/2.0/forms'
key = os.getenv('BEACONSTAC_KEY')

if key is None:
    print('Set your BEACONSTAC_KEY environment variable first.', file=sys.stderr)
    sys.exit(1)

headers = {'Authorization': f'Token {key}'}

my_form = create_hardcoded_form()

response = httpx.post(url, data=my_form, headers=headers, follow_redirects=True, timeout=60)

print()
print(f'{response.status_code}')
print()
print(f'{response.json = }')
print()
print(f'{response.text = }')
print()
