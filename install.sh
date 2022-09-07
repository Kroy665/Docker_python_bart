#!/bin/sh

# read requirements.txt from modules directory and echo the module names
# to stdout
custom_req=$(cat modules/requirements.txt | grep -v '^#' | grep -v '^$' | cut -d'=' -f1)

# read requirements.txt
# for each line, echo the module name to stdout
auto_req=$(cat requirements.txt | grep -v '^#' | grep -v '^$' | cut -d'=' -f1)

# write custom_req auto_req to a file
echo "$custom_req\n$auto_req" > requirements.txt

