#!/bin/bash/

filename="/etc/hosts"
while read -r line
do
echo "$line"
done < $filename