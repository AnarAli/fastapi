# fastapi
Download or Clone repository

```bash
cd fastapi
```

#create environment
```bash
virtualenv -p /usr/bin/python3 Env
```

#activate environment
```bash
source Env/bin/activate
```

#download packages
```bash
pip install -r requirements.txt
```

#copy your hashfile.txt to project dir

#run app (make sure 8000 port is available)
```bash
uvicorn main:app --reload
```
