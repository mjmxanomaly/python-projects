from fastapi import FastAPI
import reactions
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/new_endpoint")
def read_new_endpoint():
    reactions.greet("Alice")
    reactions.reject("Alice")
    return {"message": "Hello from the new endpoint!"}
