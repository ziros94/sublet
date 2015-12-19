#!/bin/bash
echo "cron is working"
python dump2CSV.py
python regression.py
python load_parameters.py
