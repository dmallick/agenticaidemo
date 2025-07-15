from pydantic import BaseModel
class RequestData(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: list
    allow_search: bool

from fastapi import FastAPI, HTTPException
from ai_agent import get_response
app = FastAPI(title="Agentica Demo API", version="1.0")

ALLOWED_MODELS = ["llama3-70b-8192", "gpt-3.5-turbo", "groq-llama2-70b"]

@app.post("/chat")
def chat_endpoint(request_data: RequestData):
    print("Received request data:", request_data)
    try:
        # Here you would typically process the request_data
        # and return a response based on the model_name and messages.
        #return {"status": "success", "data": "Chat response goes here"}
        if request_data.model_name not in ALLOWED_MODELS:
            raise HTTPException(status_code=400, detail="Model not allowed")
        else:
            response = get_response(
                model_name=request_data.model_name,
                model_provider=request_data.model_provider,
                system_prompt=request_data.system_prompt,
                messages=request_data.messages,
                allow_search=request_data.allow_search
            )
            return {"status": "success", "data": response}  

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8090)   
 