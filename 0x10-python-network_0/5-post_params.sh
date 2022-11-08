#!/usr/bin/env bash
# displays the response of a POST request

curl -s "$1" -d "{email: test@gmail.com, subject: I will always be here for PLD}"
