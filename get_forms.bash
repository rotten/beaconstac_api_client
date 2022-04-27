#!/bin/bash

# list all of the forms currently saved at beaconstac

http --follow https://api.beaconstac.com/api/2.0/forms \
    "Authorization: Token ${BEACONSTAC_KEY}"

