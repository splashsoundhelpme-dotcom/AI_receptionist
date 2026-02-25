from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="AI Receptionist Retail")

# Questa è la lista dove finiranno le prenotazioni di parrucchieri e ristoranti
db_appuntamenti = []

class Appuntamento(BaseModel):
    cliente: str
    servizio: str  # es. "Taglio", "Cena", "Manicure"
    data_ora: datetime
    categoria: str # "Parrucchiere", "Ristorante" o "Estetista"

@app.get("/")
def home():
    return {"status": "AI Receptionist Online", "target": "Retail & Beauty"}

@app.post("/prenota")
async def prenota(dati: Appuntamento):
    db_appuntamenti.append(dati)
    return {"messaggio": "Prenotazione registrata con mandato fiduciario"}