import json

from utils import (
    calculate_distance,
    find_nearest_agent
)

# Read input JSON
with open("input.json", "r") as file:
    data = json.load(file)

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]

# report dictionary
report = {}

for package in packages:

    package_id = package["id"]

    warehouse_id = package["warehouse"]

    destination = package["destination"]

    warehouse_location = warehouses[warehouse_id]

    nearest_agent, pickup_distance = find_nearest_agent(
        warehouse_location,
        agents
    )

    delivery_distance = calculate_distance(
        warehouse_location,
        destination
    )

    total_distance = pickup_distance + delivery_distance

    print(f"\nPackage ID: {package_id}")

    print(f"Assigned Agent: {nearest_agent}")

    print(f"Pickup Distance: {pickup_distance:.2f}")

    print(f"Delivery Distance: {delivery_distance:.2f}")

    print(f"Total Distance: {total_distance:.2f}")

    if nearest_agent not in report:

        report[nearest_agent] = {
            "packages_delivered": 0,
            "total_distance": 0
        }

    report[nearest_agent]["packages_delivered"] += 1

    report[nearest_agent]["total_distance"] += total_distance


best_agent = None

best_efficiency = float("inf")

for agent_id, details in report.items():

    packages_count = details["packages_delivered"]

    efficiency = (
        details["total_distance"] / packages_count
    )

    details["total_distance"] = round(
        details["total_distance"],
        2
    )

    details["efficiency"] = round(
        efficiency,
        2
    )

    if efficiency < best_efficiency:

        best_efficiency = efficiency

        best_agent = agent_id


report["best_agent"] = best_agent


# Save report.json
with open("report.json", "w") as file:

    json.dump(report, file, indent=4)


print("\nReport generated successfully!")