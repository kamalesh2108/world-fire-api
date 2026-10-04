from fastapi import FastAPI
import pandas as pd

app = FastAPI()

MAP_KEY = "REPLACE_WITH_YOUR_NASA_KEY"
API_URL = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{8e35be548dcbdab8b227c62946102da5}/VIIRS_SNPP_NRT/world/1"

@app.get("/")
def home():
    return {"status": "World Fire API Running"}

@app.get("/world_fires")
def get_fires():
    try:
        df = pd.read_csv(API_URL)
        fires = df[['latitude','longitude']].head(500).to_dict(orient="records")
        return {"total": len(df), "fires": fires}
    except Exception as e:
        return {"error": str(e)}
