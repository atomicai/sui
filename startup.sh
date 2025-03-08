#!/bin/bash
source .env
# Define the name of JS file (in SAP application - there should only be one file!)
FILE_NAME="index-OIwwzTCI"

# Use sed to replace the value of RR in the JavaScript file
sed -i "s|const RR=\"[^\"]*\"|const RR=\"$GEN_TARGET_URL\"|" ./sui/dist/assets/$FILE_NAME.js