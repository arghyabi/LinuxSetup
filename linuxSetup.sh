#!/bin/bash
# Define color variables
GREEN="\033[01;92m" # Bright green
BLUE="\033[01;94m"  # Bright blue
RED="\033[01;91m"   # Bright red
RESET="\033[00m"

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${GREEN}Git not found. Installing git...${RESET}"
    sudo apt-get update
    sudo apt-get install -y git
fi

# Clone the GitHub repository
REPO_URL="https://github.com/arghyabi/LinuxSetup.git"
CLONE_DIR="$HOME/LinuxSetup"

echo -e "${BLUE}Cloning repository from GitHub...${RESET}"
git clone "$REPO_URL" "$CLONE_DIR"

# Change to the repo directory
cd "$CLONE_DIR" || { echo -e "${RED}Failed to enter repo directory${RESET}"; exit 1; }

# Run the script
echo -e "${GREEN}Running configureLinux.sh...${RESET}"
source configureLinux.sh
