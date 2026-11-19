from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "gb-load-calc starter"}

def calc_basic_load(area, outlets):
    # placeholder for GB load calc
    return area * 25 + outlets * 180
