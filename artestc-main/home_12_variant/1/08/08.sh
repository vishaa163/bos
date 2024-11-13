#!/bin/bash

read -p "Login: " username
read -p "Password: " password
echo

if [[ "$username:$password" == "admin:123456" ]]; then
    echo "Authorized successful!"
else
    echo "Authorization error!"
fi