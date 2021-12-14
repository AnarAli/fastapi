from fastapi import FastAPI
from pydantic import BaseModel
import time

class HashList(BaseModel):
    hashes: list

app = FastAPI()


def find_hash(hashList):
    result = []
    with open('hashfile.txt','r') as file:
        for line in file:
            if len(result) == len(hashList):
                break
            else:
                if str(line).strip() in hashList:
                    result.append(str(line).strip())
    return result

@app.post('/')
def index(jsList:HashList):
    result =  find_hash(jsList.hashes)
    return {"result":result}

