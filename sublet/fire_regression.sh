#!/bin/bash
#This script runs "dump2CSV.py",to export apartment features and matching price data from db;
#runs "regression.py" to take in .csv and outputs regression result to parameters.txt
#runs "load_parameters.py" to import parameters.txt to Parameters table
#this will be fired up every 30 minutes by crontab
echo "cron is working"
export DJANGO_SETTINGS_MODULE="sublet.settings"
python /Users/yehua/testing/sublet/sublet/regression.py

