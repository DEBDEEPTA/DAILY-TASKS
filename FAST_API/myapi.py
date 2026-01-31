from fastapi import FastAPI
from starlette.responses import PlainTextResponse

# This FastAPI instance Can be ran on uvicorn server
app = FastAPI()
"""
    to run the instance on uvicorn :
            cmd ->
                -> uvicorn myapi:app --reload
        
    # myapi → filename
    # app → FastAPI instance
    # --reload → auto reload on code change
    # default port number to run 8000
"""


"""
    route_structure -> scheme://host/path?query
    
    PATH OPERATIONS (HTTP METHODS/ENDPOINTS)
    
    @app.get("route")       <- Read data
    @app.post("route")      <- Create
    @app.put("route")       <- Replace
    @app.patch("route")     <- partial Update
    @app.delete("route")    <- Remove
"""

"""
 ENDPOINT CONSTRUCTOR
"""

@app.get("/health")
@app.get("/")
def health():
    # DEFAULT RETURN TYPE IS JSON (IF NOT EXPLICITLY DECLARED)
    return "app is live!"