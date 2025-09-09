
@echo off
REM Create a virtual environment and install dependencies from requirements.txt

REM Set the name of the virtual environment folder
set VENV_NAME=.venv
REM Create the virtual environment
py -m venv %VENV_NAME%

REM Activate the virtual environment
call %VENV_NAME%\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

echo.
echo Virtual environment setup complete.
pause
