# Tesla Vehicles API

This is a Flask application that runs a local JSON API serving hardcoded data about the evolution of Tesla vehicles.

---

## Setup

**Requirements:** Python 3+, pip, virtual environment

### Installation

1. Clone this repository to your local machine.

2. Install the required dependencies:
   `pip install flask`


---

## Usage

Run the program from your terminal using the following command:
`python app.py`

Once the server is running, open your web browser and navigate to the following URLs to view your data:
- `http://127.0.0.1:5000/` (Home/Endpoints List)
- `http://127.0.0.1:5000/api/vehicles` (All Vehicles)
- `http://127.0.0.1:5000/api/vehicles/random` (Random Vehicle)
---

## Available Endpoints

- **GET /** — Welcome message and a JSON list of all available endpoints.
- **GET /api/vehicles** — Returns a list of all 8 Tesla vehicles along with a total count.
- **GET /api/vehicles/random** — Returns a single, randomly selected Tesla vehicle.

---

## Notes

This API uses hardcoded data stored as a Python list of dictionaries. No external database or API keys are required.