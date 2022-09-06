from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os
import requests

addr = os.getenv("OSRADDR")

headers = {"Content-Type": "application/json", "accept": "application/json"}

app = FastAPI(title = "Grammarify", 
              description = "Grammatical Error Correction tool", 
              version = "0.1")

async def check_grammar(payload):
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    response = requests.post(addr, json=payload, headers=headers).json()
    return response

        
@app.post("/checkGrammar")
async def grammar_checker(text: str):
    try:
        if text.__len__() > 500:
            
            return JSONResponse(content = {"message": "Consider breaking the text into smaller sentences. Large sentences leads to incorrect predictions"})
        predictions = await check_grammar({"text":text})
        json_compatible_item_data = jsonable_encoder({"result": predictions})
        return JSONResponse(content=json_compatible_item_data)

    except Exception as e:
        print(e)
        return JSONResponse(content = {"result": "Internal Server error, Please mail us..! "})
