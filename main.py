from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os
import requests

addr = os.getenv("OSRADDR")
print(addr)

headers = {"Content-Type": "application/json", "accept": "application/json"}

app = FastAPI(title = "Grammarify", 
              description = "Grammatical Error Correction tool", 
              version = "0.1")

async def check_grammar(payload):
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    response = requests.post(addr, json=payload, headers=headers).json()
    return response

        
@app.post("/starter_check")
async def grammar_checker(text: str = "the boys is playing"):
    try:
        if text.__len__() > 300:
            return JSONResponse(content = {"message": "Text with more than 300 characters leads to incorrect predictions. Consider breaking the text into smaller sentences or try using the other endpoints"})
        predictions = await check_grammar({"text": text})
        print(predictions)
        json_compatible_item_data = jsonable_encoder({"result": predictions})
        return JSONResponse(content=json_compatible_item_data)

    except Exception as e:
        print(e)
        return JSONResponse(content = {"result": "Invalid text or Consider providing only English text or contact Us for more information.."})

        
@app.post("/baby_check")
async def grammar_checker(text: str = "the boys is playing"):
    try:
        if text.__len__() > 600:
            return JSONResponse(content = {"message": "Text with more than 600 characters leads to incorrect predictions. Consider breaking the text into smaller sentences or try using the other endpoints"})
        predictions = await check_grammar({"text": text})
        print(predictions)
        json_compatible_item_data = jsonable_encoder({"result": predictions})
        return JSONResponse(content=json_compatible_item_data)

    except Exception as e:
        print(e)
        return JSONResponse(content = {"result": "Invalid text or Consider providing only English text or contact Us for more information.."})


@app.post("/deep_check")
async def grammar_checker(text: str = "the boys is playing"):
    try:
        if text.__len__() > 1000:
            return JSONResponse(content = {"message": "Text with more than 1000 characters leads to incorrect predictions. Consider breaking the text into smaller sentences or try using the other endpoints."})
        predictions = await check_grammar({"text": text})
        print(predictions)
        json_compatible_item_data = jsonable_encoder({"result": predictions})
        return JSONResponse(content=json_compatible_item_data)

    except Exception as e:
        print(e)
        return JSONResponse(content = {"result": "Invalid text or Consider providing only English text or contact Us for more information.."})


@app.post("/deep_check_v2")
async def grammar_checker(text: str = "the boys is playing"):
    try:
        if text.__len__() > 3000:
            return JSONResponse(content = {"message": "Consider breaking the text into smaller sentences. Text with more than 3000 characters leads to incorrect predictions."})
        predictions = await check_grammar({"text": text})
        print(predictions)
        json_compatible_item_data = jsonable_encoder({"result": predictions})
        return JSONResponse(content=json_compatible_item_data)

    except Exception as e:
        print(e)
        return JSONResponse(content = {"result": "Invalid text or Consider providing only English text or contact Us for more information.."})
