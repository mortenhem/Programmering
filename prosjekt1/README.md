nasa_api.py viser Astronomy Picture of the Day

få API-nøkkel her: https://api.nasa.gov/

Bash

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Lagre API-nøkkel i systemet ved hjelp av keyring

Bash

keyring set NASA_API_KEY brukernavn

---------------------------------------------------


NVE_request.py

Lag API-nøkkel: https://hydapi.nve.no/Users

Lag .env-fil og legg til:

NVE_API_KEY=Din API-nøkkel




