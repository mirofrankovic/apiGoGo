from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello and welcome to my API!!!"}

@app.get("/posts")
def get_posts():
    return {"data": "This is my post"}