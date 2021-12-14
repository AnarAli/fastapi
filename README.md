# fastapi
Download or Clone repository

cd fastapi

#create environment
virtualenv -p /usr/bin/python3 Env

#activate environment
source Env/bin/activate

#download packages
pip install -r requirements.txt

#copy your hashfile.txt to project dir

#run app (make sure 8000 port is available)
uvicorn main:app --reload
