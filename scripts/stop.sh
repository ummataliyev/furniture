#!/bin/bash

RED='\033[0;31m'
NC='\033[0m'

PROCESS_NAME="runserver"

PID=$(ps aux | grep "manage.py runserver" | grep -v grep | awk '{print $2}')

if [ -n "$PID" ]; then
    echo -e "${RED}Stopping the Django server with PID: $PID${NC}"
    kill $PID
    echo -e "${RED}Django server stopped successfully.${NC}"
else
    echo -e "${RED}No Django server is running.${NC}"
fi
