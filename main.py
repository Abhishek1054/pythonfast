from fastapi import FastAPI


app=FASTAPI()

@app.get("/home")
def home():
    return{"Success":True,"Message":"Hello world!"}