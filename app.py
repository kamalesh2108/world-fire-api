from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

MAP_KEY = "8e35be548dcbdab8b227c62946102da5"

@app.get("/")
def home():
    return {"status": "World Fire API Running"}

@app.get("/world_fires")
def get_fires():
    try:
        url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/VIIRS_SNPP_NRT/world/1"
        df = pd.read_csv(url)
        
        # Return first 2000 fires for performance
        sample = df.head(2000)
        fires = []
        for _, row in sample.iterrows():
            fires.append({
                "latitude": float(row['latitude']),
                "longitude": float(row['longitude'])
            })
            
        return {"total": len(df), "fires": fires}
        
    except Exception as e:
        return {"error": str(e), "message": "NASA key may need 10-30 mins to activate if newly created"}
