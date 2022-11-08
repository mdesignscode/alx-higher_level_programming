#!/usr/bin/env bash
# displays the response of a GET request

curl -s -X GET "$1" -d "X-School-User-Id: 98"
