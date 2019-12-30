#!/bin/bash
set -e
echo "Start parsing data..."
python python_scripts/data_parse.py 
echo "Parsing data complete!"
echo "Start retrospecting..."
python python_scripts/retrospect.py
echo "Retrospecting complete!"
echo "Start Server with port:8888"
python -m http.server 8888