#!/bin/bash

echo Enter any of seasons name
read season
case "$season" in
autumn ) echo "Correct! Comes after summer";;
winter ) echo "Correct! Comes after autumn";;
summer ) echo "Correct! Comes after spring";;
spring ) echo "Correct! Comes after winter";;
* ) echo "Incorrect!";;
esac