@echo off
REM Set the name of the virtual environment folder
set ENV_FOLDER="venv"
Pushd "%~dp0"
REM Check if the virtual environment folder exists
if exist %ENV_FOLDER% (
  echo Virtual environment folder found. Activating...
  REM Activate the virtual environment
  call %ENV_FOLDER%\Scripts\activate
  if %errorlevel% equ 0 (
    echo Virtual environment activated.
    REM Checking requirements
    pip install -r requirements.txt
  ) else (
    echo Failed to activate virtual environment. Creating a new one...
    REM Create the virtual environment
    py -m venv %ENV_FOLDER%
    REM Activate the virtual environment
    call %ENV_FOLDER%\Scripts\activate
    echo Virtual environment created and activated.
    REM Checking requirements
    pip install -r requirements.txt
  )
) else (
  echo Virtual environment folder not found.
  REM Create the virtual environment
  py -m venv %ENV_FOLDER%
  REM Activate the virtual environment
  call %ENV_FOLDER%\Scripts\activate
  echo Virtual environment created and activated.
  REM Checking requirements
  pip install -r requirements.txt
)
call deactivate
exit /b 0