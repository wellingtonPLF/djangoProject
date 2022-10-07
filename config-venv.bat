@ECHO OFF
ECHO Congratulations! Batch file was executed successfully.
START "" pip3 install virtualenv
START /W virtualenv .\venv
START "" .\venv\Scripts\pip3 install -r requirements.txt
PAUSE