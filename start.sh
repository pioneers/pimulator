#!/bin/bash
docker run -p 5000:5000 -v /$(pwd):/code --rm pie-bot-simulator-dev

# Create a new container running the web-server image

# Breaking down the command

# Run within docker
# docker run

# Map the containers port 5000 to the local port 5000
# -p 5000:5000

# Mount the volume of the current directory to the folder /code inside the 
# container
# -v /$(pwd):/code

# Delete the container after use to make clean up easier
# --rm

# Use the image web-server
# pie-bot-simulator-dev
