#!/bin/bash
# Set the name of the virtual environment folder
ENV_FOLDER="venv"
# Check if the virtual environment folder exists
apt install python3-venv

script_name=$0
script_full_path=$(dirname "$0")
cd $script_full_path

if [ -d "$ENV_FOLDER" ]; then
  echo "Virtual environment folder found. Activating..."
  # Activate the virtual environment
  source $ENV_FOLDER/bin/activate
  if [ $? -eq 0 ]; then
    echo "Virtual environment activated."
    #checking requirements
    pip install -r requirements.txt
  else
    echo "Failed to activate virtual environment. Creating a new one..."
    # Create the virtual environment
    python -m venv $ENV_FOLDER
    # Activate the virtual environment
    source $ENV_FOLDER/bin/activate
    echo "Virtual environment created and activated."
    #checking requirements
    pip install -r requirements.txt
  fi
else
  echo "Virtual environment folder not found."
  # Create the virtual environment
  python -m venv $ENV_FOLDER
  # Activate the virtual environment
  source $ENV_FOLDER/bin/activate
  echo "Virtual environment created and activated."
  #checking requirements
  pip install -r requirements.txt
fi

deactivate
exit 0