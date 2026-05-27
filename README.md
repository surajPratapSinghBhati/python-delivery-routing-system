# Delivery Routing System

## Overview

This project simulates a delivery routing system where packages are assigned to the nearest available delivery agent based on warehouse location.

The system calculates:
- Pickup distance
- Delivery distance
- Total travel distance
- Agent efficiency

Finally, a report is generated showing:
- Packages delivered by each agent
- Total distance travelled
- Efficiency score
- Best performing agent

---

## Technologies Used

- Python 3
- JSON

---

## Project Structure

```text
delivery-routing-system/
│
├── main.py
├── utils.py
├── input.json
├── report.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

### Step 1
Clone the repository

```bash
git clone <your-github-repo-link>
```

### Step 2
Navigate to project folder

```bash
cd delivery-routing-system
```

### Step 3
Run the project

```bash
python main.py
```

---

## Features

- Nearest agent assignment
- Distance calculation using Euclidean formula
- Agent efficiency tracking
- JSON report generation
- Modular code structure

---

## Assumptions

- Each package is assigned independently.
- Agents are always available.
- Euclidean distance is used for distance calculation.
- Warehouse locations and destinations are represented using Cartesian coordinates.
- One package is delivered at a time.
- Tie cases are resolved by selecting the first nearest agent found.

---

## Output

The system generates:

- Console simulation output
- `report.json` file containing delivery statistics

---

## Sample Concepts Used

- Functions
- Loops
- Dictionaries
- JSON handling
- Modular programming
- Distance calculations
- Basic optimization logic

---

## Author

Suraj Pratap Singh Bhati