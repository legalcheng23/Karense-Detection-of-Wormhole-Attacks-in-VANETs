import networkx as nx
import time
import math

# Set the speed of light (m/s)
speed_of_light = 3 * 10**8

# Create a VANET environment
def create_vanet():
    G = nx.Graph()
    vehicles = ['A', 'B', 'C', 'D', 'E']
    locations = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (2, 2),
        'D': (3, 3),
        'E': (4, 4)
    }
    for vehicle in vehicles:
        G.add_node(vehicle, location=locations[vehicle])
    
    # Add normal links
    G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('A', 'E')])
    
    return G

# Add Wormhole Attack link
def add_wormhole(G, node1, node2):
    G.add_edge(node1, node2, wormhole=True)

# Create a packet
def create_packet(source, destination, G):
    packet = {
        'source': source,
        'destination': destination,
        'timestamp': time.time(),
        'location': G.nodes[source]['location']
    }
    return packet

# Verify the packet
def verify_packet(packet, current_location, max_travel_distance):
    current_time = time.time()
    travel_time = current_time - packet['timestamp']
    travel_distance = travel_time * speed_of_light
    
    print(f"Verifying packet from {packet['source']} to {packet['destination']}:")
    print(f" - Current time: {current_time}")
    print(f" - Packet timestamp: {packet['timestamp']}")
    print(f" - Travel time: {travel_time} seconds")
    print(f" - Travel distance: {travel_distance} meters")
    
    if travel_distance > max_travel_distance:
        print(f" - Failed: Travel distance exceeds the maximum travel distance of {max_travel_distance} meters")
        return False
    
    if packet['location']:
        distance = calculate_distance(packet['location'], current_location)
        print(f" - Packet location: {packet['location']}")
        print(f" - Current node location: {current_location}")
        print(f" - Calculated distance: {distance} meters")
        
        if distance > max_travel_distance:
            print(f" - Failed: Calculated distance exceeds the maximum travel distance of {max_travel_distance} meters")
            return False
    
    print(" - Success")
    return True

# Calculate the distance between two geographic locations
def calculate_distance(location1, location2):
    return math.sqrt((location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)

# Simulate packet transmission and verification
def simulate_packet_transmission(G, source, destination, max_travel_distance):
    packet = create_packet(source, destination, G)
    if verify_packet(packet, G.nodes[destination]['location'], max_travel_distance):
        print(f"Packet from {source} to {destination} successfully transmitted.")
    else:
        print(f"Packet from {source} to {destination} was intercepted, suspected Wormhole Attack.")

# Main program
def main():
    G = create_vanet()
    add_wormhole(G, 'A', 'D')

    print("VANET network nodes and edges:")
    print(G.nodes(data=True))
    print(G.edges(data=True))

    max_travel_distance = 500  # Set the maximum travel distance, e.g., 500 meters
    
    # Simulate packet transmission
    simulate_packet_transmission(G, 'A', 'D', max_travel_distance)  # Transmission through Wormhole link
    simulate_packet_transmission(G, 'A', 'B', max_travel_distance)  # Normal transmission

if __name__ == "__main__":
    main()
