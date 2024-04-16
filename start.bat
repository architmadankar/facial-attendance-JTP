@echo off
cd backend
::call python -m venv env
::call venv\Scripts\activate
call conda create --name env
call conda activate env
call pip install -r requirements.txt
start cmd /k "python api.py"


cd ..
cd frontend
call yarn install
start cmd /k "yarn start -o"


