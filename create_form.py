#!/usr/bin/env python3.10

## create a new form using the beaconstac api

import datetime
import os
import sys

import httpx

from hardcoded_form import create_hardcoded_form

url = 'https://api.beaconstac.com/api/2.0/forms/'  # trailing slash is essential!
key = os.getenv('BEACONSTAC_KEY')

if key is None:
    print('Set your BEACONSTAC_KEY environment variable first.', file=sys.stderr)
    sys.exit(1)

headers = {'Authorization': f'Token {key}'}

my_form = create_hardcoded_form()

## Because httpx needs a dictionary to post json, we need to serialize these datetime values
#  explicitly.  Pydantic doesn't really have a dictionary encoder to do it automatically
if isinstance(my_form.get('created'), datetime.datetime):
    my_form['created'] = my_form['created'].isoformat()

if isinstance(my_form.get('updated'), datetime.datetime):
    my_form['updated'] = my_form['updated'].isoformat()

response = httpx.post(url, json=my_form, headers=headers, follow_redirects=True, timeout=60)

print()
print(f'{response.status_code}')
print()
print(f'{response.json = }')
print()
print(f'{response.text = }')
print()
