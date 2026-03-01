from flask import Flask, jsonify
import random

app = Flask(__name__)

tesla_vehicles = [
    {
        "id": 1,
        "model": "Original Roadster",
        "release_year": 2008,
        "vehicle_type": "Sports Car",
        "notable_feature": "First highway-legal serial production all-electric car to use lithium-ion cells."
    },
    {
        "id": 2,
        "model": "Model S",
        "release_year": 2012,
        "vehicle_type": "Luxury Sedan",
        "notable_feature": "Known for the ultra-fast 'Plaid' performance version with a sub 2 second 0-60."
    },
    {
        "id": 3,
        "model": "Model X",
        "release_year": 2015,
        "vehicle_type": "Luxury SUV",
        "notable_feature": "Features distinctive 'Falcon Wing' rear doors."
    },
    {
        "id": 4,
        "model": "Model 3",
        "release_year": 2017,
        "vehicle_type": "Compact Sedan",
        "notable_feature": "Tesla's first highly affordable, mass-market vehicle."
    },
    {
        "id": 5,
        "model": "Model Y",
        "release_year": 2020,
        "vehicle_type": "Compact Crossover",
        "notable_feature": "Shares its platform with the Model 3 and became the world's best-selling car."
    },
    {
        "id": 6,
        "model": "Tesla Semi",
        "release_year": 2022,
        "vehicle_type": "Commercial Truck",
        "notable_feature": "A Class 8 heavy-duty electric truck designed for commercial freight."
    },
    {
        "id": 7,
        "model": "Cybertruck",
        "release_year": 2023,
        "vehicle_type": "Pickup Truck",
        "notable_feature": "Highly controversial angular design with a bullet proof unpainted stainless steel exoskeleton."
    },
    {
        "id": 8,
        "model": "Roadster (Gen 2)",
        "release_year": "Concept/Upcoming",
        "vehicle_type": "Supercar",
        "notable_feature": "Promised to feature a SpaceX thruster package for unprecedented acceleration."
    }
]


@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Tesla Vehicles API",
        "endpoints": {
            "all_vehicles": "/api/vehicles",
            "random_vehicle": "/api/vehicles/random"
        }
    })

@app.route('/api/vehicles')
def get_all_vehicles():
    return jsonify({
        "count": len(tesla_vehicles),
        "vehicles": tesla_vehicles
    })


@app.route('/api/vehicles/random')
def get_random_vehicle():
    random_vehicle = random.choice(tesla_vehicles)
    return jsonify(random_vehicle)


if __name__ == "__main__":
    app.run(debug=True)