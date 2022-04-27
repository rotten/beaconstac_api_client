#!/bin/bash

# Get a specific form.  The id is passed at the command line:
#  ./get_a_form.bash 58128

# We've been using form 58128 as an example

http --follow https://api.beaconstac.com/api/2.0/forms/$1/ \
    "Authorization: Token ${BEACONSTAC_KEY}"

