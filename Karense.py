import math
import random
import time
import networkx as nx
import pandas as pd

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def distance_to(self, other_node):
        return math.sqrt((self.x - other_node.x) ** 2 + (self.y - other_node.y) ** 2)

    def __repr__(self):
        return f"Node({self.id}, x={self.x:.2f}, y={self.y:.2f})"

def generate_random_nodes(num_nodes, area_size):
    nodes = []
    for i in range(num_nodes):
        x = random.uniform(0, area_size)
        y = random.uniform(0, area_size)
        nodes.append(Node(i, x, y))
    return nodes

def simulate_wormhole_attack(node1, node2):
    return (node1, node2)

def detect_wormhole_general(nodes, wormhole_link, communication_range):
    node1, node2 = wormhole_link
    distance = node1.distance_to(node2)
    if distance > communication_range:
        return f"[General] Wormhole attack detected between Node {node1.id} and Node {node2.id} with distance {distance:.2f}!"
    else:
        return f"[General] Direct communication between Node {node1.id} and Node {node2.id} is normal."

# Detect wormhole attack - Karen Defense
def detect_wormhole_karen(nodes, wormhole_link, communication_range, G):
    results = []
    
    # GPS-based detection
    node1, node2 = wormhole_link
    distance = node1.distance_to(node2)
    if distance > communication_range:
        results.append(f"[GPS] Wormhole attack detected between Node {node1.id} and Node {node2.id} with distance {distance:.2f}!")
    else:
        results.append(f"[GPS] Direct communication between Node {node1.id} and Node {node2.id} is normal.")
    
    # Packet Transmission Verification
    packet = create_packet(node1.id, node2.id, G)
    packet_result = verify_packet(packet, G.nodes[node2.id]['location'], 500)
    results.append(packet_result)

    # DPHI detection
    vanet = VANET(len(nodes))
    dphi_result = vanet.simulate_communication_with_DPHI()
    results.append(dphi_result)
    
    return results

# Create VANET environment
def create_vanet(num_nodes, area_size):
    G = nx.Graph()
    nodes = generate_random_nodes(num_nodes, area_size)
    for node in nodes:
        G.add_node(node.id, location=(node.x, node.y))
    
    for i in range(len(nodes) - 1):
        G.add_edge(nodes[i].id, nodes[i + 1].id)
    
    return G, nodes

# Add wormhole attack link
def add_wormhole(G, node1_id, node2_id):
    G.add_edge(node1_id, node2_id, wormhole=True)

# Create packet
def create_packet(source, destination, G):
    packet = {
        'source': source,
        'destination': destination,
        'timestamp': time.time(),
        'location': G.nodes[source]['location']
    }
    return packet

# Verify packet - Packet Transmission Verification
def verify_packet(packet, current_location, max_travel_distance):
    current_time = time.time()
    travel_time = current_time - packet['timestamp']
    travel_distance = travel_time * 3 * 10**8
    
    if travel_distance > max_travel_distance:
        return f"[Packet] Travel distance exceeds the maximum travel distance of 500 meters"
    
    distance = calculate_distance(packet['location'], current_location)
    if distance > max_travel_distance:
        return f"[Packet] Calculated distance exceeds the maximum travel distance of 500 meters"
    
    return f"[Packet] Packet from {packet['source']} to {packet['destination']} successfully transmitted."

# Calculate the distance between two geographic locations
def calculate_distance(location1, location2):
    return math.sqrt((location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)

# Delay per hop indicator - DPHI
class Vehicle:
    def __init__(self, id):
        self.id = id
        self.position = 0
        self.speed = random.uniform(10, 25)

    def move(self):
        self.position += self.speed

    def get_position(self):
        return self.position

class VANET:
    def __init__(self, num_vehicles):
        self.vehicles = [Vehicle(i) for i in range(num_vehicles)]
        self.hop_delay_threshold = 2

    def simulate_communication_with_DPHI(self):
        sender = random.choice(self.vehicles)
        receiver = random.choice(self.vehicles)

        while sender == receiver:
            receiver = random.choice(self.vehicles)

        sender.move()
        receiver.move()

        hop_delay = abs(receiver.get_position() - sender.get_position()) / sender.speed

        if hop_delay > self.hop_delay_threshold:
            return f"[DPHI] Possible wormhole attack! Delay too large: {hop_delay}"
        else:
            return f"[DPHI] Communication normal. Delay: {hop_delay}"

def main():
    COMMUNICATION_RANGE = 100.0
    NUM_NODES = 20
    NUM_TESTS = 100
    WORMHOLE_ATTACKS = 50

    results_without_karen = []
    results_with_karen = []

    detected_without_karen = 0
    detected_with_karen = 0

    for _ in range(NUM_TESTS):
        G, nodes = create_vanet(NUM_NODES, 500)
        
        wormhole_attacks = random.sample([(node1, node2) for node1 in nodes for node2 in nodes if node1 != node2], WORMHOLE_ATTACKS)
        
        for attack in wormhole_attacks:
            node1, node2 = attack
            add_wormhole(G, node1.id, node2.id)

            general_result = detect_wormhole_general(nodes, (node1, node2), COMMUNICATION_RANGE)
            status = "Abnormal" if "Wormhole attack detected" in general_result else "Normal"
            results_without_karen.append({
                "Communication Range": COMMUNICATION_RANGE,
                "Num Nodes": NUM_NODES,
                "Result": general_result,
                "Status": status
            })
            if status == "Abnormal":
                detected_without_karen += 1

            karen_results = detect_wormhole_karen(nodes, (node1, node2), COMMUNICATION_RANGE, G)
            for result in karen_results:
                status = "Abnormal" if "Wormhole attack detected" in result or "exceeds the maximum travel distance" in result else "Normal"
                results_with_karen.append({
                    "Communication Range": COMMUNICATION_RANGE,
                    "Num Nodes": NUM_NODES,
                    "Result": result,
                    "Status": status
                })
                if status == "Abnormal":
                    detected_with_karen += 1

    total_attacks = NUM_TESTS * WORMHOLE_ATTACKS
    percentage_without_karen = (detected_without_karen / total_attacks) * 100
    percentage_with_karen = (detected_with_karen / total_attacks) * 100

    summary = {
        "Total Attacks": total_attacks,
        "Detected Without Karen Defense": detected_without_karen,
        "Detection Percentage Without Karen Defense": percentage_without_karen,
        "Detected With Karen Defense": detected_with_karen,
        "Detection Percentage With Karen Defense": percentage_with_karen
    }

    df_without_karen = pd.DataFrame(results_without_karen)
    df_with_karen = pd.DataFrame(results_with_karen)
    df_summary = pd.DataFrame([summary])

    

    print("Results Summary:")
    print(df_summary)

if __name__ == "__main__":
    main()
