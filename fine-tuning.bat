@echo off
set ENV_FOLDER=venv
Pushd "%~dp0"
REM Check if the virtual environment folder exists
if exist "%ENV_FOLDER%" (
  echo Virtual environment folder found. Activating...
  REM Activate the virtual environment
  call %ENV_FOLDER%\Scripts\activate
  python fine-tuning.py
  call deactivate
) else (
  echo Failed to activate venv, please run initialization first.
)
 exit /b 0