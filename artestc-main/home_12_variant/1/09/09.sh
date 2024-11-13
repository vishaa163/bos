#!/bin/bash

read -p "Vvedite slovo: " season
if [[ $season = "summer" || $season = "winter" || $season = "spring" || $season = "autumn" ]]; then
echo "Correct!"
else
echo "Incorrect!"
fi