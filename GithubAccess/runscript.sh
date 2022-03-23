#! /bin/sh
python3 GitHubAccess.py 
python3 DataProcessing.py
python3 ClearDatabase.py
python3 -m http.server
python3 ClearCSVFiles.py