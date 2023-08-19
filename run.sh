#!/bin/sh

# Run a simple HTTP server
nohup python3 -m http.server -b 127.0.0.1 8080 >& /dev/null &

# Run a test WS server
nohup python3 wsserver.py >& /tmp/wserver.log &
