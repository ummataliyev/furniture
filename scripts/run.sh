#!/bin/bash

set -e

# Define colors
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
NC='\033[0m'

echo -e "${GREEN}Database is ready!${NC}"

echo -e "${YELLOW}Applying database migrations...${NC}"
python3 manage.py migrate

echo -e "${GREEN}Starting the server...${NC}"
python3 manage.py runserver 0.0.0.0:${SERVICE_PORT}
