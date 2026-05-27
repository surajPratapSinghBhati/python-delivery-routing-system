import math


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance

def find_nearest_agent(warehouse_location, agents):
    nearest_agent = None

    minimum_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = calculate_distance(
            warehouse_location,
            agent_location
        )

        if distance < minimum_distance:
            minimum_distance = distance
            nearest_agent = agent_id

    return nearest_agent, minimum_distance