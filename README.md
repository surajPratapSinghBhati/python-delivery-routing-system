# Delivery Routing System

## Overview

This project simulates a delivery routing system that assigns packages to the nearest available delivery agent based on warehouse location and generates delivery performance reports.

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
Navigate to the project folder

```bash
cd delivery-routing-system
```

### Step 3
Run the project

```bash
python main.py
```

Make sure Python 3 is installed on your system.

---

## Features

- Automatic nearest agent assignment
- Distance calculation using Euclidean formula
- Agent efficiency tracking
- JSON report generation
- Modular code structure
- Delivery performance analysis

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

## Sample Console Output

```text
Package ID: P1
Assigned Agent: A1
Pickup Distance: 2.24
Delivery Distance: 5.83
Total Distance: 8.07

Package ID: P2
Assigned Agent: A2
Pickup Distance: 1.41
Delivery Distance: 4.12
Total Distance: 5.53

Report generated successfully!
```

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

## Future Enhancements

- Real-time agent tracking
- Traffic-aware route optimization
- Multiple package batching
- REST API integration
- Database support

---

## Author

Suraj Pratap Singh Bhati
