import json

from utils import (
    calculate_distance,
    find_nearest_agent
)

# Ask user for input JSON file
input_file = input("Enter JSON file name: ")

# Read input JSON
with open(input_file, "r") as file:
    data = json.load(file)

# Extract data
warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]

# Final report dictionary
report = {}

# Process each package
for package in packages:

    package_id = package["id"]

    warehouse_id = package["warehouse"]

    destination = package["destination"]

    # Get warehouse coordinates
    warehouse_location = warehouses[warehouse_id]

    # Find nearest agent
    nearest_agent, pickup_distance = find_nearest_agent(
        warehouse_location,
        agents
    )

    # Calculate delivery distance
    delivery_distance = calculate_distance(
        warehouse_location,
        destination
    )

    # Total travel distance
    total_distance = pickup_distance + delivery_distance

    # Print delivery simulation
    print(f"\nPackage ID: {package_id}")

    print(f"Assigned Agent: {nearest_agent}")

    print(f"Pickup Distance: {pickup_distance:.2f}")

    print(f"Delivery Distance: {delivery_distance:.2f}")

    print(f"Total Distance: {total_distance:.2f}")

    # Add agent to report if not already present
    if nearest_agent not in report:

        report[nearest_agent] = {
            "packages_delivered": 0,
            "total_distance": 0
        }

    # Update report values
    report[nearest_agent]["packages_delivered"] += 1

    report[nearest_agent]["total_distance"] += total_distance


# Find best performing agent
best_agent = None

best_efficiency = float("inf")

for agent_id, details in report.items():

    packages_count = details["packages_delivered"]

    efficiency = (
        details["total_distance"] / packages_count
    )

    # Round values
    details["total_distance"] = round(
        details["total_distance"],
        2
    )

    details["efficiency"] = round(
        efficiency,
        2
    )

    # Check best efficiency
    if efficiency < best_efficiency:

        best_efficiency = efficiency

        best_agent = agent_id


# Add best agent to report
report["best_agent"] = best_agent


# Save report file
with open("report.json", "w") as file:

    json.dump(report, file, indent=4)


print("\nReport generated successfully!")