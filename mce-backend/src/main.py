from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel
import logging
from src.mce import get_mce
from src.db_utils import open_db_connexion, verify_db_connection, insert_api_call
import psycopg2
from datetime import datetime

# Create the api
app = FastAPI()

# Global variable for the database connection
db_connection = None

# logs config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# create the input data model
class MCEInput(BaseModel):
    revenus_mensuels: float
    charges_mensuelles: float
    duree_annees: int = 20
    taux_endettement: float = 0.35
    taux_annuel: float = 0.01

# on start of api
@app.on_event("startup")
def startup_event():
    global db_connection
    try:
        db_connection = open_db_connexion()
        if db_connection:
            logging.info("Successfully connected to the database.")
        else:
            logging.warning("Database connection could not be established at startup.")
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        db_connection = None

# on shutdown of api
@app.on_event("shutdown")
def shutdown_event():
    global db_connection
    if db_connection:
        try:
            db_connection.close()
            logging.info("Database connection closed.")
        except:
            logging.warning("Unable to close the database connection.")

# Create /calculer-mce/ api
@app.post("/calculer-mce/")
def calculate_mce(input_data: MCEInput, request: Request):
    """_summary_

    Args:
        input_data (MCEInput): Modéle de données acceptées en entrée

    Returns:
        dict: dictionnaire contenant la mensualité maximale ainsi que la capacité d'emprunt estimée
    """
    # Get timestamp
    current_timestamp = datetime.now()

    # Get client IP address
    client_ip = request.client.host

    # Compute borrowing power & monthly payment
    mensualite_max, capacite = get_mce(
        revenus_mensuels=input_data.revenus_mensuels,
        charges_mensuelles=input_data.charges_mensuelles,
        duree_annees=input_data.duree_annees,
        taux_endettement=input_data.taux_endettement,
        taux_annuel=input_data.taux_annuel,
    )

    # log call api
    logging.info(f"API called by IP: {client_ip}")
    
    # save api call within database if available
    # Use the global database connection
    global db_connection
    if db_connection:
        try:
            insert_api_call(db_connection, current_timestamp, client_ip)
        except Exception as e:
            logging.error(f"Failed to log API call to the database: {e}")
    else:
        logging.warning("Database connection is unavailable; skipping logging.")

    return {
        "mensualite_max": mensualite_max,
        "capacite": capacite
    }