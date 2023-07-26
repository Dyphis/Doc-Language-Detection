#!/bin/bash
# Set the name of the virtual environment folder
ENV_FOLDER="venv"
script_name=$0
script_full_path=$(dirname "$0")
cd $script_full_path

if [ -d "$ENV_FOLDER" ]; then
  echo "Virtual environment folder found. Activating..."
  source $ENV_FOLDER/bin/activate
  if [ $? -eq 0 ]; then
    echo "Virtual environment activated."
    python main.py
    deactivate
  else
    echo "Failed to activate virtual environment. Please run initialization first."
  fi
else
  echo "Virtual environment not detected. Please run initialization first."
fi

exit 0